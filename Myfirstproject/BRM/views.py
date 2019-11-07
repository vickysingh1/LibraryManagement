from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from BRM.forms import NewBookForm,SearchForm
from BRM.models import Book

def viewBooks(request):
    books=Book.objects.all()
    res=render(request,'BRM/view_book.html',{'books':books})
    return res

def editBook(request):
    book=Book.objects.get(id=request.GET['bookid'])
    fields={'title':book.title,'price':book.price,'author':book.author,'publisher':book.publisher}
    form=NewBookForm(initial=fields)
    res=render(request,'BRM/edit_book.html',{'form':form,'book':book})
    return res

def newBook(request):
    form=NewBookForm()
    res=render(request,'BRM/new_book.html',{'form':form})
    return res
def add(request):
    if request.method=='POST':
        form=NewBookForm(request.POST)
        book=Book()
        book.title=form.data['title']
        book.price=form.data['price']
        book.author=form.data['author']
        book.publisher=form.data['publisher']
        book.save()
    s="Recored stored successfully<br><a href='BRM/view_book'>View All Book</a>"
    return HttpResponse(s)

def edit(request):
        if request.method=='POST':
            form=NewBookForm(request.POST)
            book=Book()
            book.id=request.POST['bookid']
            book.title=form.data['title']
            book.price=form.data['price']
            book.author=form.data['author']
            book.publisher=form.data['publisher']
            book.save()
        return HttpResponseRedirect('BRM/view_book.html')
def deleteBook(request):
        bookid=request.GET['bookid']
        book=Book.objects.filter(id=bookid)
        book.delete()
        return HttpResponseRedirect('BRM/view_book.html')


def searchBook(request):
    form=SearchForm()
    res=render(request,'BRM/search_book.html',{'form':form})
    return res
def search(request):
    form=SearchForm(request.POST)
    books=Book.objects.filter(title=form.data['title'])
    res=render(request,'BRM/search_book.html',{'form':form,'books':books})
    return res