from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *

# Create your views here.
def qu_ans(request):
    if not request.session.get('username'):
        return redirect('index')
    faq = QuestionAnswer.objects.all()
    # return HttpResponse(faq)
    return render(request, 'faq.html', context= {'faq':faq})
