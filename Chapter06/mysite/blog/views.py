from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Post, Tag

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

# def list(request):
#     post_list = Post.objects.all()
#     titles = ''
#     for post in post_list:
#         titles += post.title

#     return HttpResponse(titles)

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
    # comment_list = post.comment_set.all()
    comment_list = post.comments.all()
    tag_list = post.tag.all()
    return render(request, 'blog/detail.html', {'post': post, 'comment_all':comment_list, 'tag_list':tag_list})

def list(request):
    post_list = Post.objects.all()    
    return render(request, 'blog/list.html', {'post_all':post_list})

def tag_list(request, id):
    tag = Tag.objects.get(id=id)
    post_list = tag.post_set.all()
    return render(request, 'blog/list.html', {'post_all':post_list})



def test5(request):
    return render(request, 'blog/test5.html')

def test6(request):
    var1 = None
    person_list = ['Amy','Josh','Tobey']
    var2 = 'Amy\n is a beautiful'
    var3 = '<span>django is <b>easy</b> to <i>learn</i></span>'
    var4 ='''
        Miracles happen to only those who believe in them.
        Think like a man of action and act like man of thought.
        Courage is very important. Like a muscle, it is strengthened by use.
        Life is the art of drawing sufficient conclusions from insufficient premises.
        By doubting we come at the truth.
        A man that has no virtue in himself, ever envies virtue in others.
        When money speaks, the truth keeps silent.
        Better the last smile than the first laughter.
        '''

    var5 = 'check out www.djangoproject.com and send questions to admin@mysite.com'
    
    date1 = timezone.now()
    date2 = timezone.datetime(2001,3,19)
    date3 = timezone.datetime(2007,6,20)
    date4 = timezone.datetime(2030,8,22)
    date5 = timezone.datetime(2025,8,22)

    return render(request, 'blog/test6.html',{'var1':var1, 'people':person_list, 'var2':var2, 'var3':var3,
                                              'var4':var4, 'var5':var5,
                                              'date1':date1, 'date2':date2,'date3':date3,'date4':date4,'date5':date5})
                                               





