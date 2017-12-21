from django.db import models


class Dictionary(models.Model):
    language = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.language


class Word(models.Model):
    word = models.CharField(max_length=64)
    dictionary = models.ManyToManyField(Dictionary)

    def __str__(self):
        return self.word
