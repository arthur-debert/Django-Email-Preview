from base64 import b64encode
from django import template
from emailreader.models import DbEmailMessage


register = template.Library()

@register.inclusion_tag('admin/emailreader/db_email_detail.html')
def render_email_preview(object_id):
    from django.conf import settings
    db_email_message = DbEmailMessage.objects.get(pk=object_id)
    return {
        'object' : db_email_message,
        'escaped_html': b64encode(db_email_message.body_html.encode('utf-8')),
        'MEDIA_URL': settings.MEDIA_URL,
    }
