from django.core.mail.message import EmailMessage, EmailMultiAlternatives


def to_dict(email_message):
    """
    Converts the specified email message to a dictionary representation.
    """
    if type(email_message) not in [EmailMessage, EmailMultiAlternatives]:
        return email_message
    email_message_data = {
        'subject': email_message.subject,
        'body': email_message.body,
        'from_email': email_message.from_email,
        'to': email_message.to,
        'bcc': email_message.bcc,
        'attachments': email_message.attachments,
        'headers': email_message.extra_headers,
        'cc': None,
        'reply_to': None,
    }
    if isinstance(email_message, EmailMultiAlternatives):
        email_message_data['alternatives'] = email_message.alternatives
        email_message_data['content_subtype'] = getattr(email_message, 'content_subtype', None)
    return email_message_data


def from_dict(email_message_data):
    """
    Creates an EmailMessage or EmailMultiAlternatives instance from the
    specified dictionary.
    """
    kwargs = dict(email_message_data)
    alternatives = kwargs.pop('alternatives', None)
    content_subtype = kwargs.pop('content_subtype', None)
    email = (
        EmailMessage(**kwargs) if not alternatives else
        EmailMultiAlternatives(alternatives=alternatives, **kwargs))
    if content_subtype:
        email.content_subtype = content_subtype
    return email
