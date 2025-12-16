from django.shortcuts import render
from .models import Author,Book,Store
# Create your views here.


def index(request):
    authors=Author.objects.all()
    books=Book.objects.all()
    stores=Store.objects.all()
    
    context={
        'authors':authors,
        'books':books,
        'stores':stores,
    }
    
    return render(request,'index.html',context)
    
    