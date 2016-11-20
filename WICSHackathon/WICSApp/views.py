# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Quote

def index(request):
    latest_quote_list = Quote.objects.order_by('-pub_date')
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'WICSApp/index.html', context)

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'WICSAppdetail.html', {'quote': quote})

# remove this view later
def results(request, quote_id):
    response = "You're looking at the results of quote %s."
    return HttpResponse(response % quote_id)

# remove this view later
def vote(request, quote_id):
    return HttpResponse("You're voting on quote %s." % quote_id)
