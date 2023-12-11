from rest_framework import serializers
from django.utils import timezone
from django.core.validators import validate_email
from .models import Pacjent, PersonelMedyczny, RejestracjaWizyt, OddzialSzpitalny

class PacjentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacjent
        fields = '__all__'

    def validate_imie(self, imie):
        if not imie.isalpha():
             raise serializers.ValidationError('Imię może zawierać tylko litery.')
        return imie
    
    def validate_nazwisko(self, nazwisko):
        if not nazwisko.isalpha():
             raise serializers.ValidationError('Nazwisko może zawierać tylko litery.')
        return nazwisko

    def validate_pesel(self, pesel):
        if not pesel.isdigit():
            raise serializers.ValidationError('Numer PESEL może zawierać tylko cyfry')
        if len(pesel) != 11:
            raise serializers.ValidationError('Numer PESEL musi mieć dokładnie 11 cyfr')
        return pesel
    
    def validate_data_urodzenia (self, data_urodzenia):
        if data_urodzenia > timezone.now().date():
            raise serializers.ValidationError('Data urodzenia nie może być większa niż dzisiejsza data.')
        return data_urodzenia
    
    def validate_numer_telefonu (self, numer_telefonu):
        if not numer_telefonu.isdigit():
            raise serializers.ValidationError('Numer telefonu może zawierać tylko cyfry')
        return numer_telefonu
    
    def validate_adres_email (self, adres_email):
        try:
            validate_email(adres_email)
        except serializers.ValidationError:
            raise serializers.ValidationError('To pole musi zawierać poprawny adres email.')
        return adres_email

class PersonelMedycznySerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonelMedyczny
        fields = '__all__'

    def validate_imie(self, imie):
        if not imie.isalpha():
             raise serializers.ValidationError('Imię może zawierać tylko litery.')
        return imie
    
    def validate_nazwisko(self, nazwisko):
        if not nazwisko.isalpha():
             raise serializers.ValidationError('Nazwisko może zawierać tylko litery.')
        return nazwisko
    
    def validate_specjalizacja (self, specjalizacja):
        if not specjalizacja.isalpha():
             raise serializers.ValidationError('Specjalizacja może zawierać tylko litery.')
        return specjalizacja 

    def validate_numer_identyfikacyjny (self, numer_identyfikacyjny):
        if not numer_identyfikacyjny.isdigit():
            raise serializers.ValidationError('Numer identyfikacyjny może zawierać tylko cyfry')
        if len(numer_identyfikacyjny) <= 10:
            raise serializers.ValidationError('Numer identyfikacyjny może zawierać max 10 cyfr')
        return numer_identyfikacyjny 
    
    def validate_numer_telefonu (self, numer_telefonu):
        if not numer_telefonu.isdigit():
            raise serializers.ValidationError('Numer telefonu może zawierać tylko cyfry')
        return numer_telefonu
    
    def validate_adres_email (self, adres_email):
        try:
            validate_email(adres_email)
        except serializers.ValidationError:
            raise serializers.ValidationError('To pole musi zawierać poprawny adres email.')
        return adres_email

class RejestracjaWizytSerializer(serializers.ModelSerializer):
    class Meta:
        model = RejestracjaWizyt
        fields = '__all__'

class OddzialSzpitalnySerializer(serializers.ModelSerializer):
    class Meta:
        model = OddzialSzpitalny
        fields = '__all__'