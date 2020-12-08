from django.http.response import Http404
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.contrib.postgres.search import (SearchVector,
                                            SearchQuery,
                                            SearchRank)
from django.contrib.postgres.search import TrigramSimilarity
from django.conf import settings
import os
from .models import Book, Category
from .forms import AddBookForms, SearchForm

# View for the book details
def book(request,published_year,all_books):
    all_books = get_object_or_404(Book,
                                    slug=all_books,
                                    published_year=published_year)
    context = {"all_books":all_books}
    return render(request,'book_app/book.html',context)

# View for category display
def category_book(request,cat_book):
    cat_book = get_object_or_404(Category,
                                 slug = cat_book)
    context = {'cat_book':cat_book}
    return render(request,'book_app/category.html',context)

# View for Adding of Books to the database
def add_book(request):
    if request.method == 'POST':
        add_books = AddBookForms(request.POST)
        if add_books.is_valid():
            add_books.save()
            return redirect('home_page')
    else:
        add_books = AddBookForms()
    context = {"add_books":add_books}
    return render(request,'book_app/add_book.html',context)

# View For the book listing
def book_list(request):
    object_list = Book.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        book_list = paginator.page(page)
    except PageNotAnInteger:
        book_list = paginator.page(1)
    except EmptyPage:
        book_list = paginator.page(paginator.num_pages)
    context = {'page': page,'book_list':book_list}
    return render(request, 'book_app/book_list.html',context) 

def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT,path)
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response = HttpResponse(fh.read(), content_type="application/file_upload")
            response['Content-Disposition'] = 'inline;filename=' +os.path.basename(file_path)
            return response
    raise Http404 

# Function for book search functionality
def book_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Book.objects.annotate(
                similarity = TrigramSimilarity('book_name',query),
            ).filter(similarity__gt=0.1).order_by('-similarity')
    context = {"form":form,"query":query,"results":results}
    return render(request,'book_app/book_list.html',context)