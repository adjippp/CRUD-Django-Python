from django.forms import ModelForm
from django import forms
from .models import Book

class BookForm(ModelForm):

    class Meta:
        model = Book
        date_published = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
        fields = ['title', 'author', 'date_published','pages', 'type_of_book']