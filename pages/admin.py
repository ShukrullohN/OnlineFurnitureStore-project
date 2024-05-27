from django.contrib import admin
from pages.models import ContactModel

@admin.register(ContactModel)
class ContactModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created')
    search_fields = ('name', 'email', 'subject')
    list_filter = ('email', 'created')