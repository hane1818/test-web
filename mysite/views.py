from django.shortcuts import render
import random

# Create your views here.
def home(request):
    sentence = ['Random '+str(i) for i in range(50)]
    return render(request, 'index.html', {
        'sentence': random.choice(sentence),
    })
