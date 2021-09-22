from django.shortcuts import render, redirect

# Create your views here.
from cohort.forms import NativeForm, CohortForm
from cohort.models import Cohort

#
# def home(request):
#     return render(request, "home.html")


# def cohort(request):
#     return render(request, "home.html")


def native(request):
    return render(request, "create-native.html")


def fetch(request):
    natives = NativeForm.objects.all()
    context = {
        "native": natives
    }
    return render(request, "fetch.html", context)


def create_cohort(request):
    print("this function ran")
    if request.method == "POST":
        cohorts = CohortForm(request.POST)
        if cohorts.is_valid():
            cohorts.save()
            return redirect('/')

    context = {
        "form": CohortForm
    }
    return render(request, "create-cohort.html", context)


def create_native(request):
    if request.method == "POST":
        natives = NativeForm(request.POST, request.FILES)
        if natives.is_valid():
            natives.save()
            return redirect('/')
    else:
        natives = NativeForm()

    context = {
        "form": natives
    }
    return render(request, "create-native.html", context)
