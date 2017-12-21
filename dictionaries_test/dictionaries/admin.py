from django.contrib import admin
from dictionaries.models import Dictionary, Word


class DictionaryAdmin(admin.ModelAdmin):
    pass


class WordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Word, WordAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
