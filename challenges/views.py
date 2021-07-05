from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls.base import reverse

# Create your views here.

monthDict = {
    "January": "Blaskf",
    "feburary": "gsdklsdd",
    "march": "dfgdsfsdgjksd",
    "april": "dsfdgjdfkgfdsg",
    "May": None,
    "june": "All is well",
    "july": "Awon omo wobe",
    "august":"lord of the rings",
    "september":"sam is all",
    "october":"Obelisk",
    "november":"skander newer",
    "december":"christmas"
}


def index(request):
    months = list(monthDict.keys())
    return render(request, "challenge/index.html", {"list_of_month": months})


def month_int(request, month):
    list_of_month = list(monthDict.keys())
    if(month < 0 or month > len(list_of_month)):
        return HttpResponseNotFound("reqest is errorneous")
    enteredMonth = list_of_month[month-1]
    return HttpResponseRedirect(enteredMonth)


def remaining_month(request, month):
    try:
        enteredMonth = monthDict[month]

        return render(request, "challenge/challenges.html", {"value": enteredMonth, "head": month})
    except:
        return render(request, "404.html")
        # or raise Http404();
