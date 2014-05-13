from django.contrib import admin

from .models import Bloga

class BlogakAdmin(admin.ModelAdmin):
	list_display = ('izena', 'rss_link', )

admin.site.register(Bloga,BlogakAdmin)