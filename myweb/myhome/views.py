from django.shortcuts import render,reverse
from django.http import HttpResponse,JsonResponse
from . models import Citys
# Create your views here.

# 主页（访问 127.0.0.1:8000 直接跳到主页）
def index(request):
    return HttpResponse('index')

# 城市联动
def citys(request):
    return render(request,'citys.html')

# 获取城市信息
def getcitys(request):
    # 接收 城市id
    upid=request.GET.get('upid',0)
    # print(reverse('getcitys'))
    obs=Citys.objects.filter(upid=upid)
    # print(obs)
    data=[]
    for x in obs:
        # print(x) 
        # print(x.id)
        # print(x.name)

        data.append({'id':x.id,'name':x.name})
    # print(data)

    # return render(request,'citys.html')
    # return HttpResponse('1')
    
    # 返回json数据

    # JsonResponse是 HttpResponse 的一个子类 
    # 1. 它的默认Content-Type 被设置为： application/json
    # 2. 第一个参数，data应该是一个字典类型，当 safe 这个参数被设置为：False ,那data可以填入任何能被转换为JSON格式的对象，
    #    比如list, tuple, set。 默认的safe 参数是 True. 如果你传入的data数据类型不是字典类型，那么它就会抛出 TypeError的异常。
    
    return JsonResponse(data,safe=False)