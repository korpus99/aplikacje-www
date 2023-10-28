from django.contrib import admin

from .models import *

class OsobaAdmin(admin.ModelAdmin):
    list_display = ['id', 'imie','plec','nazwisko','data_dodania','stanowisko_display']
    readonly_fields = ('data_dodania',)
    list_filter = ('data_dodania',)

    @admin.display(description='Stanowisko')
    def stanowisko_display(self, obj):
        return f'{obj.stanowisko.nazwa} ({obj.stanowisko.id})'

admin.site.register(Question)
admin.site.register(Osoba, OsobaAdmin)
admin.site.register(Stanowisko)