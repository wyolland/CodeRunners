
# from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Quote

def index(request):
    latest_quote_list = Quote.objects.order_by('-rank')
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'WICSApp/index.html', context)

def upvote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.rank += 1
    quote.save()
    latest_quote_list = Quote.objects.order_by('-rank')
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'WICSApp/index.html', context)

def downvote(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    quote.rank -= 1
    quote.save()
    latest_quote_list = Quote.objects.order_by('-rank')
    context = {'latest_quote_list': latest_quote_list}
    return render(request, 'WICSApp/index.html', context)

def random(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    context = {'quote': quote}
    return render(request, 'WICSApp/random.html', context)

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'WICSAppdetail.html', {'quote': quote})

# remove this view later
def results(request, quote_id):
    response = "You're looking at the results of quote %s."
    return HttpResponse(response % quote_id)

def random(request):
    return Quote.objects.filter(id=randint(1,Quote.objects.count()+1))

# remove this view later
def vote(request, quote_id):
    return HttpResponse("You're voting on quote %s." % quote_id)
