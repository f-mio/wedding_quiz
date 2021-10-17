from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
#from django.urls import reverse

from .models import Quiz, Invitees, Comments
from .forms import AnswerForm
import datetime



def index(request):
    '''
    This method is used for index page.
    When the invitee presses the button in index page,
    it moves to the answer page.
    '''
    if (request.method == 'POST'):
        try:
            comment = Comments()
            comment.name     = request.POST['comment-name']
            comment.comment  = request.POST['comment-text']
            comment.pub_date = datetime.datetime.now()

            latest_question_list = Quiz.objects.order_by('-pub_date')[:10]
            context = {
                'latest_question_list': latest_question_list
            }
            comment.save()
            return render(request, 'quiz/index.html' ,context)

        except:
            raise Http404("Quiz does not exist, or comment can not posted.")

    else:
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
    This method is page that is used fore invitees to answer questions.
    '''
    try:
        quiz = Quiz.objects.order_by('pub_date')
        form = AnswerForm()
        context = {
            'quiz': quiz,
            'quiz_numbers': [i for i in range(1,11)],
            'form' : form,
        }

    except Quiz.DoesNotExist:
        raise Http404('Quiz does not exist.')

    return render(request, 'quiz/new.html', context)


def post(request):
    '''
    This method is used for post process.
    '''
    if request.method != 'POST':
        quiz = Quiz.objects.order_by('pub_date').filter
        form = AnswerForm()
        context = {
            'quiz': quiz,
            'quiz_numbers': [i for i in range(1,11)],
            'form' : form
        }
        return redirect('/new')

    try:
        form = AnswerForm(request.POST)
        point = 0
        for i in range(10):
            if int(request.POST['answer_{}'.format(i+1)]) == Quiz.objects.get(id=i+1).quiz_correct:
                point += 1
        invitee = Invitees()
        invitee.point       = point
        invitee.family_name = request.POST['family_name']
        invitee.first_name  = request.POST['first_name']
        invitee.email       = request.POST['email']
        invitee.answer_1    = request.POST['answer_1']
        invitee.answer_2    = request.POST['answer_2']
        invitee.answer_3    = request.POST['answer_3']
        invitee.answer_4    = request.POST['answer_4']
        invitee.answer_5    = request.POST['answer_5']
        invitee.answer_6    = request.POST['answer_6']
        invitee.answer_7    = request.POST['answer_7']
        invitee.answer_8    = request.POST['answer_8']
        invitee.answer_9    = request.POST['answer_9']
        invitee.answer_10   = request.POST['answer_10']
        invitee.pub_date    = datetime.datetime.now()
        invitee.save()
        return redirect('/corrects')

    except:
        form = AnswerForm(request.POST)
        quiz = Quiz.objects.all().order_by('pub_date')
        context = {
            'quiz': quiz,
            'form': form
        }
        return render(request, 'quiz/new.html', context)


def corrects(request):
    '''
    This method is used to show all corrects of quiz.
    '''
    quiz     = Quiz.objects.all()
    context = {
        'quiz': quiz,
        'quiz_numbers': [i for i in range(1,11)]
    }

    return render(request, 'quiz/corrects.html', context)


# Show all Invitees result.
def results(request):
    '''
    This meshod show all invitees name and points,
      and show correct rate graph about each questions.
    '''
    try:
        invitees = get_object_or_404(Invitees)
        context = {
            'invitees': invitees
        }

    except Invitees.DoesNotExist:
        raise Http404('Invitees do not exist.')

    return render(request, 'quiz/results.html', context)
