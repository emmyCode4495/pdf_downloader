from django.urls import path

from . import views

app_name = 'book_app'

urlpatterns = [
    path('<slug:all_books>/<int:published_year>/',views.book,name="books"),
    path('books_list/',views.book_list,name="book_lists"),
    path('added_book/',views.add_book,name="add_book"),   
    path('search/',views.book_search, name='book_search'),
    path('<slug:cat_book>/',views.category_book, name="category")
]