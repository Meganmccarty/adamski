from django.shortcuts import render
from django.views import generic
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Publication, Presentation

def home(request):
    return render(request, 'database/home.html')
"""
def publications(request):
    pub_list = Publication.objects.filter(status='Published').order_by('year', 'letter')
    accepted_list = Publication.objects.filter(status='Accepted').order_by('author')
    submitted_list = Publication.objects.filter(status='Submitted').order_by('author')
    prep_list = Publication.objects.filter(status='In prep').order_by('author')

    paginator = Paginator(pub_list, 100)

    page = request.GET.get('page')
    try:
        publications = paginator.page(page)
    except PageNotAnInteger:
        publications = paginator.page(1)
    except EmptyPage:
        publications = paginator.page(paginator.num_pages)

    context = {
        'pub_list': pub_list,
        'accepted_list': accepted_list,
        'submitted_list': submitted_list,
        'prep_list': prep_list,
        'page': page,
        'publications': publications,
    }
    
    return render(request, 'database/publications.html', context=context)
"""

class PublicationListView(generic.ListView):
    model = Publication
    template_name = 'database/publications.html'

    def get_context_data(self, **kwargs):
        context = super(PublicationListView, self).get_context_data(**kwargs)
        context['pub_list'] = Publication.objects.filter(status='Published').order_by('year', 'letter')
        context['accepted_list'] = Publication.objects.filter(status='Accepted').order_by('author')
        context['submitted_list'] = Publication.objects.filter(status='Submitted').order_by('author')
        context['prep_list'] = Publication.objects.filter(status='In prep').order_by('author')
        context['pub_count'] = Publication.objects.filter(status='Published').count()
        context['accepted_count'] = Publication.objects.filter(status='Accepted').count()
        context['submitted_count'] = Publication.objects.filter(status='Submitted').count()
        context['prep_count'] = Publication.objects.filter(status='In prep').count()
        return context

class PresentationListView(generic.ListView):
    model = Presentation
    template_name = 'database/presentations.html'

    def get_context_data(self, **kwargs):
        context = super(PresentationListView, self).get_context_data(**kwargs)
        context['pres_list'] = Presentation.objects.order_by('year', 'month', 'day')
        context['pres_count'] = Presentation.objects.all().count()
        return context

