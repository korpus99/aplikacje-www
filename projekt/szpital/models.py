from django.db import models
from rest_framework.authtoken.models import Token

class Pacjent(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    pesel = models.CharField(max_length=11, unique=True)
    data_urodzenia = models.DateField()
    adres = models.TextField()
    numer_telefonu = models.CharField(max_length=15)
    adres_email = models.EmailField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class PersonelMedyczny(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    specjalizacja = models.CharField(max_length=100)
    numer_identyfikacyjny = models.CharField(max_length=10, unique=True)
    adres = models.TextField()
    numer_telefonu = models.CharField(max_length=15)
    adres_email = models.EmailField()

    def __str__(self):
        return f"{self.imie} {self.nazwisko}"

class RejestracjaWizyt(models.Model):
    data_wizyty = models.DateField()
    godzina_wizyty = models.TimeField()
    lekarz = models.ForeignKey(PersonelMedyczny, on_delete=models.CASCADE)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
    opis_wizyty = models.TextField()
    status_wizyty = models.CharField(
        max_length=20,
        choices=[('p', 'Planowana'), ('o', 'Odwołana'), ('z', 'Zakończona')],
        default='p'
    )

    def __str__(self):
        return f"Wizyta {self.data_wizyty} {self.godzina_wizyty} - {self.pacjent}"

class OddzialSzpitalny(models.Model):
    nazwa_oddzialu = models.CharField(max_length=100, unique=True)
    opis = models.TextField()
    personel = models.ManyToManyField(PersonelMedyczny)

    def __str__(self):
        return self.nazwa_oddzialu

def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)