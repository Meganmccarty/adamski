from django.contrib import admin
from .models import Publication, Presentation

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('pub_num', 'status', 'author', 'get_year_and_letter', 'journal_title', 
                    'journal', 'volume_num', 'issue_num', 'pages', 'editor', 'chapter_title', \
                    'book_title', 'edition', 'volume', 'publisher', 'publisher_country', \
                    'book_pages')
    search_fields = ('author', 'get_year_and_letter', 'journal_title', 'journal', \
                    'chapter_title', 'book_title')
    fields = ('pub_num', 'status', 'author', 'year', 'letter', 'journal_title', 'journal', \
                    'volume_num', 'issue_num', 'pages', 'editor', 'chapter_title', \
                    'book_title', 'edition', 'volume', 'publisher', 'publisher_country', \
                    'book_pages', 'pdf')

@admin.register(Presentation)
class PresentationAdmin(admin.ModelAdmin):
    list_display = ('day', 'month', 'year', 'presenter', 'title', 'symposium', 'meeting', \
                    'location')
    search_fields = ('year', 'presenter', 'title', 'symposium', 'meeting', 'location')
    fields = ('day', 'month', 'year', 'presenter', 'title', 'symposium', 'meeting', \
                    'location')