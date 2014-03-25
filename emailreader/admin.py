from django.contrib import admin
from emailreader.models import DbEmailMessage

class EmailMessageAdmin(admin.ModelAdmin):
    list_display = ('subject', 'to', 'sent_at', 'is_multipart')
    search_fields = ('subject', 'to')
    date_hierarchy = 'sent_at'
    list_filters = ('is_multipart',)

    class Media:
        css = {
            'all': ('emailreader/css/email_preview.css',),
        }

    def has_add_permission(self, request):
        return False

admin.site.register(DbEmailMessage, EmailMessageAdmin)

