from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Publication, Presentation, Travel, Grant, Society

def home(request):
    society_list = Society.objects.order_by('society')
    return render(request, 'database/home.html', {'society_list' : society_list})

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

class GrantListView(generic.ListView):
    model = Grant
    template_name = 'database/grants.html'

    def get_context_data(self, **kwargs):
        context = super(GrantListView, self).get_context_data(**kwargs)
        context['grant_list'] = Grant.objects.order_by('-year', '-amount', 'grant_details')
        return context

class SocietyListView(generic.ListView):
    model = Society
    template_name = 'database/societies.html'

    def get_context_data(self, **kwargs):
        context = super(SocietyListView, self).get_context_data(**kwargs)
        context['society_list'] = Society.objects.order_by('society')
        return context
