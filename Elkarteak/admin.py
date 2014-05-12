from django.contrib import admin

from .models import Elkartea

class ElkarteaAdmin(admin.ModelAdmin):
	list_display = ('nor','email','webgunea')

admin.site.register(Elkartea,ElkarteaAdmin)
