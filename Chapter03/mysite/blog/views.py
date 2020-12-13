from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Post

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

def list(request):
    post_list = Post.objects.all()
    titles = ''
    for post in post_list:
        titles += post.title

    return HttpResponse(titles)

# def detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except:
#         return HttpResponse('존재하지 않는 데이타입니다')
#     return HttpResponse(post.title)


# def detail(request, id):
#     try:
#         post = Post.objects.get(id=id)
#     except Post.DoesNotExist :
#         raise Http404('존재하지 않는 데이타입니다')
#     return HttpResponse(post.title)


def detail(request, id):
    post = get_object_or_404(Post, id=id)
    return HttpResponse(post.title)


