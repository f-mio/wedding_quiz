from django.http import Http404
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
    try:
        quiz = Quiz.objects.order_by('pub_date')
        context = {
            'quiz': quiz,
            'for_range': [i for i in range(1,5)]
        }
    except Quiz.DoesNotExist:
        raise Http404('Quiz does not exist.')
    return render(request, 'quiz/new.html', context)

def results(request):
    try:
        invitees = get_object_or_404(Invitees)
        context = {
            'invitees': invitees
        }
    except Invitees.DoesNotExist:
        raise Http404('Invitees do not exist.')
    return render(request, 'quiz/result', context)
#    return render(request, 'quiz/results.html', context)