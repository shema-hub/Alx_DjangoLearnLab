from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "published_date", "isbn"]
        widgets = {
            "published_date": forms.DateInput(attrs={"type": "date"}),
        }