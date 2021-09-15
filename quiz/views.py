from typing import Awaitable
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from .models import Quiz, Invitees


def index(request):
    '''
    This method is used for index page.
    When the invitee presses the button in index page,
    it moves to the answer page.
    '''
    try:
        latest_question_list = Quiz.objects.order_by('-pub_date')[:10]
        context = {
            'latest_question_list': latest_question_list
        }
    except Quiz.DoesNotExist:
        raise Http404("Quiz does not exist.")
    return render(request, 'quiz/index.html' ,context)


def new(request):
    '''
    This method is 
    '''
    try:
        quiz = Quiz.objects.order_by('pub_date')
        context = {
            'quiz': quiz,
            'for_range': [i for i in range(1,5)]
        }
    except Quiz.DoesNotExist:
        raise Http404('Quiz does not exist.')
    return render(request, 'quiz/new.html', context)


def corrects(request):
    '''
    This method is used to show all corrects of quiz.
    '''
    try:
        invitees = get_object_or_404(Invitees)
        context = {
            'invitees': invitees
        }
    except Invitees.DoesNotExist:
        raise Http404('Invitees does not exist.')

    return render(request, 'quiz/corrects.html', context)


def post(request, quiz_answer):
    '''
    This method is used for post process.
    '''
    try:
        point = 0
        for i in range(10):
            if request.POST['answer-{}'.format(i+1)] == Quiz.objects.get(id=i+1).answer:
                point += 1
        input_value = Invitees({
            'family_name': request.POST['family_name'],
            'first_name':  request.POST['first_name'],
            'email':       request.POST['email'],
            'point':       point,
            'answer_1':    request.POST['1quiz-choice'],
            'answer_2':    request.POST['2quiz-choice'],
            'answer_3':    request.POST['3quiz-choice'],
            'answer_4':    request.POST['4quiz-choice'],
            'answer_5':    request.POST['5quiz-choice'],
            'answer_6':    request.POST['6quiz-choice'],
            'answer_7':    request.POST['7quiz-choice'],
            'answer_8':    request.POST['8quiz-choice'],
            'answer_9':    request.POST['9quiz-choice'],
            'answer_10':   request.POST['10quiz-choice']
            })
        input_value.save
        invitees = get_object_or_404(Invitees)
        context = {
            'invitees': invitees
        }
        return render(request, 'quiz/corrects.html', context)
    except:
        return render(request, 'quiz/new.html', {
            'family_name':   request.POST['family_name'],
            'first_name':    request.POST['first_name'],
            'email':         request.POST['email'],
            '1quiz-choice':  request.POST['1quiz-choice'],
            '2quiz-choice':  request.POST['2quiz-choice'],
            '3quiz-choice':  request.POST['3quiz-choice'],
            '4quiz-choice':  request.POST['4quiz-choice'],
            '5quiz-choice':  request.POST['5quiz-choice'],
            '6quiz-choice':  request.POST['6quiz-choice'],
            '7quiz-choice':  request.POST['7quiz-choice'],
            '8quiz-choice':  request.POST['8quiz-choice'],
            '9quiz-choice':  request.POST['9quiz-choice'],
            '10quiz-choice': request.POST['10quiz-choice']
        })


# Show all Invitees result.
def results(request):
    try:
        invitees = get_object_or_404(Invitees)
        context = {
            'invitees': invitees
        }
    except Invitees.DoesNotExist:
        raise Http404('Invitees do not exist.')

    return render(request, 'quiz/results.html', context)
