from django.contrib import admin

# Register your models here.

from .models import FirstApp


class FirstAppAdmin(admin.ModelAdmin):
    """ Simple comment """

    model = FirstApp
    list_display = ('title', 'description', 'date') # list_display -> это кортедж отличается неизменяемостью данных например от list [ ... , ... ]


admin.site.register(FirstApp, FirstAppAdmin)