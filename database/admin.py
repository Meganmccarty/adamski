from django.contrib import admin
from .models import Publication, Presentation, Travel, Grant

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

@admin.register(Travel)
class TravelAdmin(admin.ModelAdmin):
    list_display = ('year', 'travel_details')
    search_fields = ('year', 'travel_details')
    fields = ('year', 'travel_details')

@admin.register(Grant)
class GrantAdmin(admin.ModelAdmin):
    list_display = ('year', 'amount', 'grant_details')
    search_fields = ('year', 'amount', 'grant_details')
    fields = ('year', 'amount', 'grant_details')