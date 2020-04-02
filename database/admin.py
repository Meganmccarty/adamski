from django.contrib import admin
from .models import Publication, Presentation

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('author', 'year_and_letter', 'reference')
    search_fields = ('author', 'year_and_letter', 'reference')
    fields = ('author', 'year', 'letter', 'reference', 'pdf')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('day', 'month', 'year', 'presenter', 'title', 'symposium', 'meeting', \
                    'location')
    search_fields = ('year', 'presenter', 'title', 'symposium', 'meeting', 'location')
    fields = ('day', 'month', 'year', 'presenter', 'title', 'symposium', 'meeting', \
                    'location')