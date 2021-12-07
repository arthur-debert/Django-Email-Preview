from django.core.mail.backends.console import EmailBackend as BaseBackend
from django.utils import timezone

from emailreader.models import DbEmailMessage

import logging
logger = logging.getLogger(__name__)


class EmailBackend(BaseBackend):
    def send_messages(self, email_messages):
        """Write all messages to the stream in a thread-safe way."""
        if not email_messages:
            return
        try:
            for message in email_messages:
                logger.info("Caught email to {0}: '{1}'".format(message.to, message.subject))
                db_mail = DbEmailMessage(
                    from_email=message.from_email,
                    to=';'.join(message.to),
                    subject=message.subject,
                    body=message.body,
                    sent_at=timezone.now()
                )
                if hasattr(message, 'alternatives') and bool(message.alternatives):
                    body, content_type = message.alternatives[0]
                    if content_type == 'text/html':
                        db_mail.body_html = body
                        db_mail.is_multipart = True
                db_mail.save()
        except:
            if not self.fail_silently:
                raise
        return len(email_messages)
