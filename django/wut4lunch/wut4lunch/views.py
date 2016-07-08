from django.shortcuts import render, redirect

from .forms import LunchForm
from .models import Lunch


def index(request):
    lunches = Lunch.objects.all()
    form = LunchForm(auto_id=False)
    return render(request, 'wut4lunch/index.html', {'lunches': lunches, 'form': form})


def lunch_new(request):
    if request.method == "POST":
        form = LunchForm(request.POST)
        if form.is_valid():
            lunch = form.save(commit=False)
            lunch.save()
    return redirect('wut4lunch.views.index')
