# from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Quote

def index(request):
    latest_quote_list = Quote.objects.order_by('-pub_date')[:5]
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'WICSApp/index.html', context)

def detail(request, quote_id):
    try:
        quote = Quote.objects.get(pk=quote_id)
    except Quote.DoesNotExist:
        raise Http404("Quote does not exist")
    return render(request, 'WICSApp/detail.html', {'quote': quote})

# remove this view later
def results(request, quote_id):
    response = "You're looking at the results of quote %s."
    return HttpResponse(response % quote_id)

# remove this view later
def vote(request, quote_id):
    return HttpResponse("You're voting on quote %s." % quote_id)
