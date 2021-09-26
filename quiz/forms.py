from django import forms
from .models import Quiz

quiz = Quiz.objects.order_by('pub_date')
choice_1  = (
    ('1', quiz[0].choice_1), ('2', quiz[0].choice_2),
    ('3', quiz[0].choice_3), ('4', quiz[0].choice_4))
choice_2  = (
    ('1', quiz[1].choice_1), ('2', quiz[1].choice_2),
    ('3', quiz[1].choice_3), ('4', quiz[1].choice_4))
choice_3  = (
    ('1', quiz[2].choice_1), ('2', quiz[2].choice_2),
    ('3', quiz[2].choice_3), ('4', quiz[2].choice_4))
choice_4  = (
    ('1', quiz[3].choice_1), ('2', quiz[3].choice_2),
    ('3', quiz[3].choice_3), ('4', quiz[3].choice_4))
choice_5  = (
    ('1', quiz[4].choice_1), ('2', quiz[4].choice_2),
    ('3', quiz[4].choice_3), ('4', quiz[4].choice_4))
choice_6  = (
    ('1', quiz[5].choice_1), ('2', quiz[5].choice_2),
    ('3', quiz[5].choice_3), ('4', quiz[5].choice_4))
choice_7  = (
    ('1', quiz[6].choice_1), ('2', quiz[6].choice_2),
    ('3', quiz[6].choice_3), ('4', quiz[6].choice_4))
choice_8  = (
    ('1', quiz[7].choice_1), ('2', quiz[7].choice_2),
    ('3', quiz[7].choice_3), ('4', quiz[7].choice_4))
choice_9  = (
    ('1', quiz[8].choice_1), ('2', quiz[8].choice_2),
    ('3', quiz[8].choice_3), ('4', quiz[8].choice_4))
choice_10 = (
    ('1', quiz[9].choice_1), ('2', quiz[9].choice_2),
    ('3', quiz[9].choice_3), ('4', quiz[9].choice_4))


class AnswerForm(forms.Form):
    family_name = forms.CharField(label="family_name", max_length=10)
    first_name  = forms.CharField(label="first_name", max_length=10)
    email       = forms.EmailField(label="email", max_length=50)
    answer_1    = forms.ChoiceField(label="answer_1",  widget=forms.RadioSelect, choices=choice_1, required=True)
    answer_2    = forms.ChoiceField(label="answer_2",  widget=forms.RadioSelect, choices=choice_2, required=True)
    answer_3    = forms.ChoiceField(label="answer_3",  widget=forms.RadioSelect, choices=choice_3, required=True)
    answer_4    = forms.ChoiceField(label="answer_4",  widget=forms.RadioSelect, choices=choice_4, required=True)
    answer_5    = forms.ChoiceField(label="answer_5",  widget=forms.RadioSelect, choices=choice_5, required=True)
    answer_6    = forms.ChoiceField(label="answer_6",  widget=forms.RadioSelect, choices=choice_6, required=True)
    answer_7    = forms.ChoiceField(label="answer_7",  widget=forms.RadioSelect, choices=choice_7, required=True)
    answer_8    = forms.ChoiceField(label="answer_8",  widget=forms.RadioSelect, choices=choice_8, required=True)
    answer_9    = forms.ChoiceField(label="answer_9",  widget=forms.RadioSelect, choices=choice_9, required=True)
    answer_10   = forms.ChoiceField(label="answer_10", widget=forms.RadioSelect, choices=choice_10, required=True)
