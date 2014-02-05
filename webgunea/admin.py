from django.contrib import admin
from webgunea.models import *

class EkintzaAdmin(admin.ModelAdmin):
    list_display = ('tituloa', 'egune', 'lekua', 'deskribapena','kartela',)
    list_filter = ('egune','sortzailea')
    filter_horizontal = ('sortzailea',)


class AutorAdmin(admin.ModelAdmin):
	list_display = ('nor','email','webgunea')

admin.site.register(Autor,AutorAdmin)
admin.site.register(Ekintza,EkintzaAdmin)
