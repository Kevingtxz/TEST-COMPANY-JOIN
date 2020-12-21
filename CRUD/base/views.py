from django.shortcuts import render

from .forms import TargetForm
from .models import Target

def index(request, id=None):
    targets = Target.objects.all()
    form = TargetForm()
    context = {
        "targets":targets,
        "form":form, 
    }
    return render(request, "base/index.html", context)