from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def test(request):
    que="int is keyword in c language?"
    a="yes"
    b="no"
    c="sometimes"
    d="none"
    data={'que':que,'a':a,'b':b,'c':c,'d':d}
    return render(request,'exam/test.html',data)