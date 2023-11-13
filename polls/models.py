import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    
    def __str__(self):
            return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

class Stanowisko(models.Model):
    nazwa = models.CharField(max_length=200, unique=True)
    opis = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nazwa

class Osoba(models.Model):
    class Plec(models.IntegerChoices):
        Mężczyzna = 1
        Kobieta = 2
        Inna = 3

    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    plec = models.IntegerField(max_length=1, choices=Plec.choices)
    stanowisko = models.ForeignKey(Stanowisko,on_delete=models.CASCADE)
    data_dodania = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.imie} {self.nazwisko}'
    
    class Meta:
        ordering = ["nazwisko"]
        verbose_name_plural = "Osoba"