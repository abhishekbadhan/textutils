#THIS IS MY FIRST PROJECT HARE KRISHNA

from django.http import HttpResponse
from django.shortcuts import render


dict1 = {'name':'abhishek','god':'hare_krishna'}
def index(request):
    return render(request,'index.html')


def about(request):
    result=request.GET.get('text','default')
    if len(result)==0:
        return HttpResponse("<a href='http://127.0.0.1:8000/' style='background-color:green;'>GOBACK</a>")
    else:
        return HttpResponse(result)
        


