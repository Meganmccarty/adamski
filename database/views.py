from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Publication, Presentation, Travel

def home(request):
    return render(request, 'database/home.html')

class PublicationListView(generic.ListView):
    model = Publication
    template_name = 'database/publications.html'

    def get_context_data(self, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['pub_list'] = Publication.objects.all().order_by('year', 'letter', 'author')
        context['pub_count'] = Publication.objects.all().count()
        return context

class PresentationListView(generic.ListView):
    model = Presentation
    template_name = 'database/presentations.html'

    def get_context_data(self, **kwargs):
        context = super(PresentationListView, self).get_context_data(**kwargs)
        context['pres_list'] = Presentation.objects.order_by('-year', 'title')
        context['pres_count'] = Presentation.objects.all().count()
        return context

class TravelListView(generic.ListView):
    model = Travel
    template_name = 'database/travel.html'

    def get_context_data(self, **kwargs):
        context = super(TravelListView, self).get_context_data(**kwargs)
        context['travel_list'] = Travel.objects.order_by('-year', 'travel_details')
        return context

