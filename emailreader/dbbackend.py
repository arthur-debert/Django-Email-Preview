import datetime
from django.core.mail.backends.console import EmailBackend as BaseBackend

from emailreader.models import DbEmailMessage

class EmailBackend(BaseBackend):
    def send_messages(self, email_messages):
        """Write all messages to the stream in a thread-safe way."""
        if not email_messages:
            return
        try:
            for message in email_messages:
                db_mail = DbEmailMessage(
                    from_email = message.from_email,
                    to = ';'.join(message.to),
                    subject = message.subject.encode('utf-8'),
                    body = message.body.encode('utf-8'),
                    sent_at = datetime.datetime.now()
                )
                if hasattr(message, 'alternatives') and bool(message.alternatives):
                    body, content_type = message.alternatives[0]
                    if content_type == 'text/html':
                        db_mail.body_html = body.encode('utf-8')
                        db_mail.is_multipart = True
                db_mail.save()
        except:
            if not self.fail_silently:
                raise
        return len(email_messages)
    
