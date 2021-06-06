from django.shortcuts import render
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
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
not_found_message = "not found"

# Create your views here.

def index(request):
    months = list(months_tasks.keys())
    return render(request, "challenges/index.html", {
        "months":months
    })


def months_n(request, month):
    months = list(months_tasks.keys())
    if month >= 1 and month <= len(months_tasks):
        redirect_path = reverse("month-challenge",args=[months[month-1]])
        return HttpResponseRedirect(redirect_path)
    else:
        raise Http404()
def months_s(request, month):
    if month in months_tasks.keys():
        return render(request, "challenges/challenge.html", {
            "text": months_tasks[month],
            "header": month
        })
    else:
        raise Http404()