from django.contrib import admin

from .models import Ekintza

class EkintzaAdmin(admin.ModelAdmin):
    list_display = ('tituloa', 'ekintzanOrdue', 'ekintzanAmaieranOrdue', 'lekua', 'deskribapena', 'kartela',)
    list_filter = ('egune', 'sortzailea')
    filter_horizontal = ('sortzailea',)

admin.site.register(Ekintza, EkintzaAdmin)
