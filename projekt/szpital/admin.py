from django.contrib import admin
from .models import Pacjent, PersonelMedyczny, RejestracjaWizyt, OddzialSzpitalny

class PacjentAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Pacjent._meta.fields]

class PersonelMedycznyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in PersonelMedyczny._meta.fields]

class RejestracjaWizytAdmin(admin.ModelAdmin):
    list_display = [field.name for field in RejestracjaWizyt._meta.fields]

class OddzialSzpitalnyAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OddzialSzpitalny._meta.fields]

admin.site.register(Pacjent, PacjentAdmin)
admin.site.register(PersonelMedyczny, PersonelMedycznyAdmin)
admin.site.register(RejestracjaWizyt, RejestracjaWizytAdmin)
admin.site.register(OddzialSzpitalny, OddzialSzpitalnyAdmin)
