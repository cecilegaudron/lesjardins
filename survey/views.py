from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from .forms import SurveyForm


def survey_create(request):
    """ Basic view for survey """
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("success.html")
    else:
        form = SurveyForm(initial={"key": "value"})

    return render(request, "survey/survey.html", {"form": form})


def success(request):
    """ Basic view for Succes page """
    return render(request, 'survey/success.html')
