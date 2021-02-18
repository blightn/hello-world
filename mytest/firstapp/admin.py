from django.contrib import admin

# Register your models here.

from .models import FirstApp


class FirstAppAdmin(admin.ModelAdmin):
    """ Записи """

    model = FirstApp
    list_display = ('title', 'description', 'date')


admin.site.register(FirstApp, FirstAppAdmin)