from django.contrib import admin

from blog.models import Tickets, Contacts

# Register your models here.
admin.site.register((Tickets,Contacts))