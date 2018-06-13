from django.shortcuts import render, redirect
from .models import *
from django.http import *
# Create your views here.
def index(request):
    booklist = BookInfo.books1.all()
    content={'title':booklist}
    return render(request, 'booktest/dccloud.html',content)

def show(request,id):
    book = BookInfo.books1.get(pk=id)
    heroList = book.heroinfo_set.all()
    content = {'list':heroList}
    return render(request,'booktest/show.html',content)

#views 练习
def detail(request,p1,p2,p3):
    return HttpResponse(p1)

#
def getTest1(request):
    return render(request, 'booktest/getTest1.html')
def getTest2(request):
    a1 = request.GET['a']
    b1 = request.GET['b']
    c1 = request.GET['c']
    content = {'a':a1,'b':b1,'c':c1} 
    return render(request, 'booktest/getTest2.html',content)
def getTest3(request):
    a1 = request.GET.getlist('a')
    content = {'a':a1} 
    return render(request, 'booktest/getTest3.html',content)

#post测试
def postTest1(request):
    return render(request, 'booktest/postTest1.html')

def postTest2(request):
    uname = request.POST['uname']
    upasswd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    content = {'uname':uname,'upasswd':upasswd,'ugender':ugender,'uhobby':uhobby} 
    return render(request, 'booktest/postTest2.html',content)


#测试cookie
def cookieTest(request):
    response = HttpResponse()
    response.set_cookie('t1','abc')
    cookie = request.COOKIES
    if cookie['t1']:
        response.write(cookie['t1'])
    return response
    #跨域名访问不能共享cookie


#转向练习
def redTest(request):
    #return  HttpResponseRedirect('postTest1') #这里必须是url地址
    return redirect('/booktest/postTest1')

#session练习
def session1(request):
    uname = request.session.get('myname')
    content={'uname':uname}
    return render(request, 'booktest/session1.html',content)

def session2(request):
    return render(request, 'booktest/session2.html')

def sessionHandle(request):
    uname = request.POST['uname']
    request.session['myname'] = uname #设置
    request.session.set_expiry(0)   #设置过期时间，0表示关闭浏览器就过期
    return redirect('/booktest/session1')
def session3(request):
    del request.session['myname']
    return redirect('/booktest/session1')




