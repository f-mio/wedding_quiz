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
    family_name = forms.CharField(
        label="family_name",
        max_length=10,
        widget=forms.TextInput(
            attrs={'placeholder':'名字', 'class':'new-name-inputbox'}))
    first_name  = forms.CharField(label="first_name", max_length=10,
        widget=forms.TextInput(
            attrs={'placeholder':'名前', 'class':'new-name-inputbox'}))
    email       = forms.EmailField(label="email", max_length=50, required=False,
        widget=forms.EmailInput(
            attrs={'placeholder':'(任意) email', 'class':'new-name-inputbox'}))

    answer_1    = forms.ChoiceField(
        label="answer_1",
        choices=choice_1,
        required=True,
        disabled=False,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_2    = forms.ChoiceField(
        label="answer_2",
        choices=choice_2,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_3    = forms.ChoiceField(
        label="answer_3",
        choices=choice_3,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_4    = forms.ChoiceField(
        label="answer_4",
        choices=choice_4,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_5    = forms.ChoiceField(
        label="answer_5",
        choices=choice_5,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_6    = forms.ChoiceField(
        label="answer_6",
        choices=choice_6,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_7    = forms.ChoiceField(
        label="answer_7",
        choices=choice_7,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_8    = forms.ChoiceField(
        label="answer_8",
        choices=choice_8,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_9    = forms.ChoiceField(
        label="answer_9",
        choices=choice_9,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))

    answer_10   = forms.ChoiceField(
        label="answer_10",
        choices=choice_10,
        required=True,
        disabled=True,
        widget=forms.RadioSelect(attrs={'class':'new-radio-select'}))
