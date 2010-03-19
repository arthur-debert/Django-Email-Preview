from django import template
from emailreader.models import DbEmailMessage


register = template.Library()

@register.inclusion_tag('admin/emailreader/db_email_detail.html')
def render_email_preview(object_id):
    from django.conf import settings
    return {
        'object' : DbEmailMessage.objects.get(pk=object_id),
        'MEDIA_URL': settings.MEDIA_URL,
    }
