from django.contrib.auth.views import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from app import forms


@login_required
def index(request):
    if request.method == "POST":
        form = forms.PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return HttpResponseRedirect(f'{reverse("index")}?id={person.id}')
    else:
        form = forms.PersonForm()

    context = {"form": form}
    return render(request, "app/index.html", context)
