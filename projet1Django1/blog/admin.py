from django.contrib import admin

from .models import *
admin.site.register(Client)
admin.site.register(Commande)
admin.site.register(Plat)
admin.site.register(Restaurant)