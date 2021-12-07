from django.db import models


class DbEmailMessage(models.Model):
    """docstring for EmailMessageMode"""

    sent_at = models.DateTimeField()
    from_email = models.CharField(max_length=512)
    to = models.CharField(max_length=2024)
    subject = models.CharField(max_length=2024)
    is_multipart = models.BooleanField(default=False)
    body = models.TextField()
    body_html = models.TextField(blank=True, null=True)
