from django.contrib import admin
from .models import Appointment, Doctor, Profession, ContactMessage, BlogPost, Izoh


admin.site.register(Profession)
admin.site.register(Doctor)
admin.site.register(BlogPost)
admin.site.register(Izoh)


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'doctor', 'date']
    list_filter = ['doctor', 'date']

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'subject', 'email', 'phone', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('created_at',)