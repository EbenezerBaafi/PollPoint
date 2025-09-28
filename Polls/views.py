from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Wlcome to Polls index page. Ready to cast your vote?")