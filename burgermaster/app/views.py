from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#index: startseite


def index(request):
    # ditctionary context usually is used as parameter to give to frontendf etc.

    context = {
        'name': 'Patrick'
    }
    return render(request,'index.html', context)
