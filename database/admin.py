from django.contrib import admin
from .models import Publication, Presentation

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('author', 'year_and_letter', 'reference')
    search_fields = ('author', 'year_and_letter', 'reference')
    fields = ('author', 'year', 'letter', 'reference', 'pdf')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('year', 'title', 'location', 'presenter')
    search_fields = ('year', 'title', 'location', 'presenter')
    fields = ('year', 'title', 'location', 'presenter')