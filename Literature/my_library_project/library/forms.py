from django import forms
from django.core.exceptions import ValidationError
from .models import Book
import datetime

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genres', 'publication_date', 'summary']

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 2:
            raise ValidationError("Название должно быть не короче 2 символов.")
        return title

    def clean_publication_date(self):
        pub_date = self.cleaned_data['publication_date']
        if pub_date > datetime.date.today():
            raise ValidationError("Дата публикации не может быть в будущем.")
        return pub_date
