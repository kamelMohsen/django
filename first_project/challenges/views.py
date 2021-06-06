from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
# Variables goes here

months_tasks = {
    "jan":"1",
    "feb":"2",
    "mar":"3",
    "apr":"4",
    "may":"5",
    "jun":"6",
    "jul":"7",
    "aug":"8",
    "sep":"9",
    "oct":"10",
    "nov":"11",
    "dec":"12"
}

# Create your views here.
def months_n(request, month):
    months = list(months_tasks.keys())
    if month >= 1 and month <= len(months_tasks):
        red_path = reverse("month-challenge",args=[months[month-1]])
        return HttpResponseRedirect(red_path)
    else:
        return HttpResponse("Wrong Month")

def months_s(request, month):
    if month in months_tasks.keys():
        return HttpResponse(months_tasks[month])
    else:
        return HttpResponse("Wrong Month")