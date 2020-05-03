from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created']
    search_fields = ['name', 'email', 'subject']
    list_filter = ['created', ]
    list_per_page = 20

admin.site.register(Contact, ContactAdmin)
