from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    data ={
        'title':'HOME NEW',
        'BDATA':'IN WHICH OF THE COURSE DO YOU WANT TO ENROLL',
        'CLIST':['python','java','c++','django'],
        'STUDENT_DETAILS':[
            {'name': 'robin', 'age': 20},
            {'name': 'sita', 'age': 21},
            {'name': 'gita', 'age': 22},
        ]
    }
    return render(request,"index.html",data)
def aboutUs(request):
    return HttpResponse("hi my name is robin rawat")

def Course(request):
    return HttpResponse("<h1>hi</h1>")

def courseDetails(request,courseid):
    return HttpResponse(courseid)
    