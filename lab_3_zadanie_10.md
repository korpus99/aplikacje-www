from polls.models import Stanowisko, Osoba

1. Wyświetl wszystkie obiekty modelu Osoba:

Osoba.objects.all()

2. Wyświetl obiekt modelu Osoba z id = 3:

Osoba.objects.filter(id=3)

3. Wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik),

Osoba.objects.filter(imie__startswith="A")

4. Wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba,

Osoba.objects.distinct()

5. Wyświetl nazwy stanowisk posortowane alfabetycznie malejąco,

Stanowisko.objects.order_by("-nazwa")

6. Dodaj nową instancję obiektu klasy Osoba i zapisz w bazie.

wybrane_stanowisko = Stanowisko.objects.get(nazwa="Tester")
nowa_osoba = Osoba(imie='Czarek', nazwisko='Marecki', plec=1, stanowisko=wybrane_stanowisko)
nowa_osoba.save()
