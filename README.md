Django Q Email
==============

[![Current version on PyPI](http://img.shields.io/pypi/v/django-q-email.svg)][pypi]

`django-q-email` is a reusable Django app for queuing the sending of email with [Django Q][].


Installation
------------

Install the latest version with pip:

```bash
$ pip install django-q-email
```

Then in `settings.py`:

```python
EMAIL_BACKEND = 'django_q_email.backends.DjangoQBackend'
```

Then send email in the normal way, as per the [Django email docs](https://docs.djangoproject.com/en/1.10/topics/email/),
and they will be sent in a background task. [See Django Q for more info](https://github.com/Koed00/django-q).


Configuration
-------------

`DJANGO_Q_EMAIL_BACKEND` - Backend used in the background task (default: `django.core.mail.backends.smtp.EmailBackend`)


Requirements
------------

- [Django](https://www.djangoproject.com/) >= 1.8
- [Django Q](https://github.com/Koed00/django-q)


Contributing
------------

1. Check the open issues or open a new issue to start a discussion around
   your feature idea or the bug you found
2. Fork the repository and make your changes
3. Create a new pull request


[pypi]: http://pypi.python.org/pypi/django-q-email/
[django q]: https://github.com/Koed00/django-q
