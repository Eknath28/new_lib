from django.http import HttpResponse
from django.shortcuts import render
from book.models import Book

# Create your views here.

def homepage(request):
    print("Homepage")
    # return HttpResponse("<h3>hello<h3>")
    return render(request, "home.html")

def allbook(request):
    stud = Book.objects.all()
    data = {"data":stud}
    return render(request,"home.html", context=data)
