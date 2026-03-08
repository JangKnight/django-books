from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import Book, Author
from django.shortcuts import render

# Create your views here.

def index(request):
    books = Book.objects.all()
    print(books)
    res = {"books": books}
    return render(request, "index.html", res)

def books(request):
    if request.method == "GET":
        return render(request, "add_book.html")
     
 
    btitle = request.POST["title"]
    bauthor = request.POST["author"]
    if " " in bauthor:
        bauthor = bauthor.split(" ")
    bauthor = Author(first_name=bauthor[0], last_name=bauthor[1])
    bauthor.save()
    brating = request.POST["rating"]
    book = Book(title=btitle, author=bauthor, rating=brating)
    book.save()
    return render(request, "book_submitted.html")

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect("index")

    