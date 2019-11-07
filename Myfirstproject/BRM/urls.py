from django.conf.urls import url
from BRM import views

urlpatterns=[
    url('view_book',views.viewBooks),
    url('edit_book',views.editBook),
    url('delete_book',views.deleteBook),
    url('search_book',views.searchBook),
    url('view_book',views.viewBooks),
    url('new_book',views.newBook),
    url('add',views.add),
    url('search',views.search),
    url('view_book',views.viewBooks),
    url('edit',views.edit),

   
]