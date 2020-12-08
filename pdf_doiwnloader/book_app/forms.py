from django import forms

from .models import Book

class AddBookForms(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name','book_author','book_edition','file_type',
                  'file_size','published_year','publisher',
                  'book_language','book_pages','book_isbn','file_upload',
                  'book_image','book_summary','author_profile')

class SearchForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class':'search-field','placeholder':'search by book name...'}))
