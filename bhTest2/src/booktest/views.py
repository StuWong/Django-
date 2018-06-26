from django.shortcuts import render
from booktest.models import *
from django.http.response import HttpResponse,JsonResponse

# Create your views here.
def index(request):
    return render(request,'booktest/index.html')

#省市区选择联系
def area(request):
    booklist = AreaInfo.objects.all().values()
    #return HttpResponse(booklist)
    return render(request,'booktest/area.html')
#获取省信息
def pro(request,tid):
    id1 = int(tid)
    if id1 == 0 :
        booklist = AreaInfo.objects.filter(parea=0).values()
    list1 = []
    for each in booklist:
        list1.append([each['id'],each['title']])
    content = {'data':list1}
    return JsonResponse(content)
#获取市信息
def city(request,cid):
    id1 = int(cid)
    booklist = AreaInfo.objects.filter(parea=id1).values()
    list1 = []
    for each in booklist:
        list1.append([each['id'],each['title']])
    content = {'data':list1}
    return JsonResponse(content)
#获取县信息
def dis(request,cid):
    id1 = int(cid)
    booklist = AreaInfo.objects.filter(parea=id1).values()
    list1 = []
    for each in booklist:
        list1.append([each['id'],each['title']])
    content = {'data':list1}
    return JsonResponse(content)






