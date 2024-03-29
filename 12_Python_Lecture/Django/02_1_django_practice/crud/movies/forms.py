from django import forms
from .models import Movie, Comment

class MovieForm(forms.ModelForm):
    title = forms.CharField(
        label = '영화명',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title form-control',
                'placeholder' : 'Enter the title',
            }
        )
    )
    title_en = forms.CharField(
        label = '영화명(영문)',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-title_en form-control',
                'placeholder' : 'Enter the title_en',
            }
        )
    )
    audience = forms.IntegerField(
        label = '누적 관객수',
        widget = forms.NumberInput(
            attrs = {
                'class' : 'my-audience form-control',
                'placeholder' : 'Enter the audience',
            }
        )
    )
    open_date = forms.CharField(
        label = '개봉일',
        widget = forms.DateInput(
            attrs = {
                'class' : 'my-open-date form-control',
                'placeholder' : 'Enter the open_date',
            }
        )
    )
    genre = forms.CharField(
        label = '장르',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-genre form-control',
                'placeholder' : 'Enter the genre',
            }
        )
    )
    watch_grade = forms.CharField(
        label = '관람등급',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-watch-grade form-control',
                'placeholder' : 'Enter the watch_grade',
            }
        )
    )
    score = forms.FloatField(
        label = '평점',
        widget = forms.NumberInput(
            attrs = {
                'class' : 'my-score form-control',
                'placeholder' : 'Enter the score',
            }
        )
    )
    poster_url = forms.CharField(
        label = '포스터 URL',
        widget = forms.TextInput(
            attrs = {
                'class' : 'my-poster-url form-control',
                'placeholder' : 'Enter the poster_url',
            }
        )
    )
    description = forms.CharField(
        label = '세부내용',
        widget = forms.Textarea(
            attrs = {
                'class' : 'my-description form-control',
                'placeholder' : 'Enter the Description',
                'rows' : 10,
                'cols' : 9,
            }
        )
    )

    class Meta:
        model = Movie
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label = 'Comment',
        widget = forms.Textarea(
            attrs = {
                'class' : 'my-comment form-control',
                'placeholder' : 'Enter your comments about the movie',
                'rows' : 2,
                'cols' : 40,
            }
        )
    )
    class Meta:
        model = Comment 
        fields = '__all__'
        exclude = ('article',)