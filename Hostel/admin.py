from django.contrib import admin

from .models import Entry

class EntryAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Entry._meta.fields]
    list_filter = [f.name for f in Entry._meta.fields]



admin.site.register(Entry,EntryAdmin)