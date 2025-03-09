from django.db import models
from .forms import ExampleForm


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseForbidden
from .models import Book

# View for editing an book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(book, id=book_id)
    
    if request.method == "POST":
        book.title = request.POST.get("title")
        book.content = request.POST.get("content")
        book.save()
        return redirect("book_detail", book_id=book.id)
    
    return render(request, "edit_book.html", {"book": book})

# View for deleting an book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(book, id=book_id)
    book.delete()
    return redirect("book_list")

    