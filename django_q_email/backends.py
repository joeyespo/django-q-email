from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend
from django.utils.module_loading import import_string

from .utils import from_dict, to_dict

try:
    from django_q.tasks import async_task
except ImportError:
    # Django Q < 1.0
    from django_q import tasks
    # Use getattr to avoid SyntaxError: invalid syntax on Python 3.7+
    async_task = getattr(tasks, 'async')


DEFAULT_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_BACKEND = getattr(settings, 'DJANGO_Q_EMAIL_BACKEND', DEFAULT_BACKEND)
EMAIL_ERROR_HANDLER = getattr(settings, 'DJANGO_Q_EMAIL_ERROR_HANDLER', None)
DJANGO_Q_EMAIL_USE_DICTS = getattr(settings, 'DJANGO_Q_EMAIL_USE_DICTS', True)


class DjangoQBackend(BaseEmailBackend):
    use_dicts = DJANGO_Q_EMAIL_USE_DICTS

    def send_messages(self, email_messages):
        num_sent = 0
        for email_message in email_messages:
            if self.use_dicts:
                email_message = to_dict(email_message)
            async_task('django_q_email.backends.send_message', email_message)
            num_sent += 1
        return num_sent


def send_message(email_message):
    """
    Sends the specified email synchronously.

    See DjangoQBackend for sending in the background.
    """
    try:
        if isinstance(email_message, dict):
            email_message = from_dict(email_message)
        connection = email_message.connection
        email_message.connection = get_connection(backend=EMAIL_BACKEND)
        try:
            email_message.send()
        finally:
            email_message.connection = connection
    except Exception as ex:
        if not EMAIL_ERROR_HANDLER:
            raise
        email_error_handler = import_string(EMAIL_ERROR_HANDLER)
        email_error_handler(email_message, ex)
