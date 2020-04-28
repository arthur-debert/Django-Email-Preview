from base64 import b64encode
from django import template
from emailreader.models import DbEmailMessage

register = template.Library()


@register.inclusion_tag('admin/emailreader/db_email_detail.html')
def render_email_preview(object_id):
    db_email_message = DbEmailMessage.objects.get(pk=object_id)
    cxt = {'object': db_email_message}

    if db_email_message.is_multipart:
        cxt['escaped_html'] = b64encode(db_email_message.body_html.encode()).decode()

    return cxt
