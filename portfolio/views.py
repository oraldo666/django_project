from django.shortcuts import render
from .models import Project
from .forms import CustomerForm

def home(request):
    projects = Project.objects.all()

    form = CustomerForm()

    if request.method =="POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            form = CustomerForm()

    return render(request,"portfolio/home.html", {'projects': projects,"form":form})



