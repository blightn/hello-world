from django.contrib import admin

# Register your models here.

from .models import Note


class FirstAppAdmin(admin.ModelAdmin):
    # Записки

    model = Note
    list_display = ('author', 'title', 'text', 'creation_date', 'modify_date')


admin.site.register(Note, FirstAppAdmin)