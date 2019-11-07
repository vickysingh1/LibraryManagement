from django.shortcuts import render
from django.http import HttpResponse
from testapp.models import employee



def employees_info_view(request):
    employ=employee.objects.all()
    data={'employees':employ}
    return render(request,'testapp/Employe.html',data)
    

# Create your views here.
