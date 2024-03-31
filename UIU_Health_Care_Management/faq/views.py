from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def qu_ans(request):
    faq = QuestionAnswer.objects.all()
    # return HttpResponse(faq)
    return render(request, 'faq.html', context= {'faq':faq})
