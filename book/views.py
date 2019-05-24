from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BookForm
from .models import Book

def index(request):
    status = ''
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = BookForm()
    return render(request, 'book/index.html', {'form': form, 'books': Book.objects.all(), 'status': status })

def edit(request, pk):
    book = get_object_or_404(Book, pk=pk)
    status = 'success'
    titleValue = Book.objects.filter(pk=pk).values('title')[0]
    book_title = titleValue['title']
    
    if request.method == 'POST':
        post_form = BookForm(request.POST, instance=book)
        if post_form.is_valid():
            post_form.save()
            return render(request, 'book/edit.html', {'form': post_form, 'status': status, 'book_title': book_title })
    else:
        form = BookForm(instance=book)
    return render(request, 'book/edit.html', {'form': form, 'book_title': book_title })

def delete(request, pk):
    book = Book.objects.get(pk=pk)
    book.delete()
    return HttpResponseRedirect('/')