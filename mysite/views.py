from django.shortcuts import render
import random

# Create your views here.
def home(request):
    sentence = ['random1', 'random2', 'random3']
    return render(request, 'index.html', {
        'sentence': random.choice(sentence),
    })
