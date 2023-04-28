from django.contrib import admin

from blog.models import Tickets, Contacts, aviatickets

# Register your models here.
admin.site.register((Tickets,Contacts, aviatickets))