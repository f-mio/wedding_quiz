from django.http.response import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Quiz, Invitees


def index(request):
    try:
        latest_question_list = Quiz.objects.order_by('-pub_date')[:10]
        context = {
            'latest_question_list': latest_question_list
        }
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist.")
    return render(request, 'quiz/index.html' ,context)

def new(request):
    return HttpResponse('answer')

def results(request):
    invitees = get_object_or_404(Invitees)
    context = {
        'invitees': invitees
    }
    return HttpResponse('result')
#    return render(request, 'quiz/results.html', context)