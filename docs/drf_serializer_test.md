>>> from polls.models import Osoba
>>> from polls.models import Stanowisko
>>> from polls.serializers import OsobaSerializer
>>> from polls.serializers import StanowiskoSerializer
>>> from rest_framework.renderers import JSONRenderer
>>> from rest_framework.parsers import JSONParser

>>> osoba = Osoba(imie="Kamil", nazwisko="Kowalski", plec="2", stanowisko=Stanowisko.objects.get(id=1))
>>> osoba.save()
>>> serializer = OsobaSerializer(osoba)
{'id': 6, 'imie': 'Kamil', 'nazwisko': 'Kowalski', 'plec': 2, 'data_dodania': '2023-11-05T16:59:16.007195+01:00', 'stanowisko': 1}

>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":6,"imie":"Kamil","nazwisko":"Kowalski","plec":2,"data_dodania":"2023-11-05T16:59:16.007195+01:00","stanowisko":1}'

>>> stanowisko = Stanowisko(nazwa="Grafik", opis="Tworzy wizualne elementy")
>>> stanowisko.save()
>>>
>>> serializer = StanowiskoSerializer(stanowisko)
>>> serializer.data
{'id': 4, 'nazwa': 'Grafik', 'opis': 'Tworzy wizualne elementy'}

>>> content = JSONRenderer().render(serializer.data)
>>> content
b'{"id":4,"nazwa":"Grafik","opis":"Tworzy wizualne elementy"}'