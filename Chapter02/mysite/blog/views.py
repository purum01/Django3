from django.shortcuts import render
from django.http import HttpResponse

def test1(request):
    return HttpResponse("blog/test1 응답!")

def test2(request, no):
    print("no 타입 :", type(no))
    return HttpResponse(f"no : {no}")

def test3(request, year, month, day):
    return HttpResponse(f"년:{year}, 월:{month}, 일:{day}")


def test4(request, id):
    print("id 타입 :", type(id))
    return HttpResponse("path변수를 str->code로 변환!" )

