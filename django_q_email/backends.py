from django.conf import settings
from django.core.mail import get_connection
from django.core.mail.backends.base import BaseEmailBackend

try:
    from django_q.tasks import async_task
except ImportError:
    # Django Q < 1.0
    from django_q.tasks import async as async_task


EMAIL_BACKEND = getattr(
    settings, 'DJANGO_Q_EMAIL_BACKEND',
    'django.core.mail.backends.smtp.EmailBackend')


class DjangoQBackend(BaseEmailBackend):
    def send_messages(self, email_messages):
        num_sent = 0
        for email_message in email_messages:
            async_task('django_q_email.backends.send_message', email_message)
            num_sent += 1
        return num_sent


def send_message(email_message):
    """
    Sends the specified email immediately.

    Use DjangoQBackend to send in the background.
    """
    connection = email_message.connection
    email_message.connection = get_connection(backend=EMAIL_BACKEND)
    try:
        email_message.send()
    finally:
        email_message.connection = connection
