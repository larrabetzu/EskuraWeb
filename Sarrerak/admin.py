from django.contrib import admin

from .models import Sarrera

class SarreraAdmin(admin.ModelAdmin):
    list_display = ('tituloa', 'sarrera_data', 'sarrera_link', 'bloga',)

admin.site.register(Sarrera,SarreraAdmin)
