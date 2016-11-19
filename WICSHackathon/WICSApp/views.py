from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the WICSApp index.")

def detail(request, quote_id):
    return HttpResponse("You're looking at the results of question %s." % question_id)
