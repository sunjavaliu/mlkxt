#coding=utf8
from django.shortcuts import render
from django.template import loader,Context
from django.http import HttpResponse
#from minglu.models import ssdata
from models import ssdata
from models import gssldata,gszxdata

from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.db.models import Q

import csv 
from .forms import PostForm
#from django.views.decorators.csrf import csrf_exempt
#from django.template import RequestContext
from django.shortcuts import render_to_response
from django.http import StreamingHttpResponse
from django.http import HttpResponseRedirect

import    StringIO 
 

def showindex(request):
    #print( request.session.get("sess_admin", False))
    if not request.session.get("dzm", False):
        return HttpResponseRedirect("admin/admin")
    else:
        return render(request, 'ml/default.html')

def show(request):
    #data=ssdata.objects.all()[:10]
    request.session.set_expiry(0)
    dzm=request.session.get("dzm", False)
    if not dzm:
        return HttpResponseRedirect("admin/admin")
    
    if dzm=="430100":
        data=ssdata.objects.exclude(qylx__icontains="个体")
    else:
        data=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).exclude(qylx__icontains="个体")
 
    #request.session['title'] = 'wuuw'
    
    #####ADD
    page_size=4  #每页记录数
    paginator = Paginator(data, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
        print page
     
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)         
    #####ADD
     
    t = loader.get_template('ml/index.html')
    c = {'posts': posts,'title':'长沙市商事登记平台企业信息','exportfiletype':'ssqy','user':request.session.get("sess_admin", False)["name"]}
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return HttpResponse(t.render(c))
    #return HttpResponse(t.render(c),content_type="text/xml")  



'''
下载大数据文件的原型方法
'''
def big_file_download(request):
    # do something...
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    
    the_file_name = "big_file.pdf"
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    
    return response



def exportfile(request):
    sio = StringIO.StringIO()
    writer = csv.writer(sio)  
    exportfiletype=request.GET.get('exportfiletype')
    if exportfiletype=='ssqy':
        data=ssdata.objects.exclude(qylx__icontains="个体")
        
        row=[u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围',u'统一社会信用代码 ']
        writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围'])
        for post in data: 
            #writer.writerow([post.zch, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw])
            zchstr='''\''''+post.zch  
            row=[zchstr, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw]
            writer.writerow([unicode(s).encode("utf-8") for s in row])
            
            
    def file_iterator(file_name, chunk_size=512):
        with open(file_name) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
                
    return 


def exportCSV(request):  
    #  
    
    
    sio = StringIO.StringIO()
    writer = csv.writer(sio)  
    
 
        
    #return response    
    
    
    #response = HttpResponse(content_type='text/csv')  
    #response['Content-Disposition'] = 'attachment; filename=my.csv'  
    #writer = csv.writer(response)  
    
    
    #djtype='ssgive'
    exportfiletype=request.GET.get('exportfiletype')
    if exportfiletype=='ssqy':
        
        
        data=ssdata.objects.exclude(qylx__icontains="个体")
        
        row=[u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围',u'统一社会信用代码 ']
        writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围'])
        for post in data: 
            #writer.writerow([post.zch, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw])
            zchstr='''\''''+post.zch  
            row=[zchstr, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw]
            writer.writerow([unicode(s).encode("utf-8") for s in row])

    if exportfiletype=='ssgt':
        data=ssdata.objects.filter(qylx__icontains="个体")
        
        row=[u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围',u'统一社会信用代码 ']
        writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围'])
        for post in data: 
            #writer.writerow([post.zch, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw])  
            zchstr='''\''''+post.zch
            row=[zchstr, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw]
            writer.writerow([unicode(s).encode("utf-8") for s in row])    


    if exportfiletype=='gszx':

        data=gszxdata.objects.all()
        
        row=[u'注册号',u'名称',u'核发日期',u'登记机关']
        writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围'])
        for post in data: 
            #writer.writerow([post.zch, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw])  
            zchstr='''\''''+post.zch  
            row=[zchstr, post.qiyename, post.hzriqi, post.djjg]
            writer.writerow([unicode(s).encode("utf-8") for s in row])
            
    if exportfiletype=='gsdj':
        data=gssldata.objects.all()
        
        row=[u'注册号',u'名称',u'核发日期',u'登记机关']
        writer.writerow([unicode(s).encode("utf-8") for s in row])
        #writer.writerow([u'注册号',u'名称',u'法定代表人',u'主营项目类别',u'住所(经营场所)',u'注册资本',u'商事主体类型',u'成立日期',u'营业期限',u'核发日期',u'登记机关',u'状态',u'经营范围'])
        for post in data: 
            #writer.writerow([post.zch, post.mcyename, post.fddbri, post.zyxmlb, post.dz, post.rjzczb, post.qylx,post.clrq,post.yyqx, post.hzrq, post.djjg, post.zt, post.jyfw])  
            zchstr='''\''''+post.zch  
            row=[zchstr, post.qiyename, post.hzriqi, post.djjg]
            writer.writerow([unicode(s).encode("utf-8") for s in row])
            

        #writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        #row = ['中国', '美国', '台湾', '马来西亚']
        #writer.writerow([unicode(s).encode("utf-8") for s in row])
    
    response = HttpResponse(sio.getvalue(),content_type='text/csv') 
    response['Content-Disposition'] = 'attachment; filename=my.csv'      
 
    return response 

    
def showgeti(request):
    #data=ssdata.objects.all()[:10]
    
    data=ssdata.objects.filter(qylx__contains="个体")
 
     
    #####ADD
    page_size=5
    paginator = Paginator(data, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
        print page
     
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)         
    #####ADD
     
    t = loader.get_template('ml/index.html')
    #c = Context({'posts': posts,'title':'长沙市商事登记平台个体户信息','exportfiletype':'ssgt'})
    #如果用上面的会出现以下错误   RemovedInDjango110Warning: render() must be called with a dict, not a Context.  return HttpResponse(t.render(c))
    c = {'posts': posts,'title':'长沙市商事登记平台个体户信息','exportfiletype':'ssgt'}
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return HttpResponse(t.render(c))
    #return HttpResponse(t.render(c),content_type="text/xml")  

    
def showzhuxiao(request):
    
    
    data=gszxdata.objects.all()
 
    #request.session['title'] = 'wuuw'
    
    #####ADD
    page_size=18
    paginator = Paginator(data, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
        print page
     
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)         
    #####ADD
     
    t = loader.get_template('ml/slzlx.html')
    c = {'posts': posts,'title':'工商局平台-注销企业信息','exportfiletype':'gszx'}
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return HttpResponse(t.render(c))
    #return HttpResponse(t.render(c),content_type="text/xml")  



def showsheli(request):
    
    
    data=gssldata.objects.all()
 
    #request.session['title'] = 'wuuw'
    
    #####ADD
    page_size=18
    paginator = Paginator(data, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
        print page
     
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)         
    #####ADD
     
    t = loader.get_template('ml/slzlx.html')
    c = {'posts': posts,'title':'工商局平台-新登记企业信息','exportfiletype':'gsdj'}
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return HttpResponse(t.render(c))
    #return HttpResponse(t.render(c),content_type="text/xml")  
    
    
def showqyxx(request):
    
    zch=request.GET.get('zch',1) 
    #data=ssdata.objects.filter(zch__iexact=zch)
    
    #data=ssdata.objects.filter(zch__contains=zch)
    print(zch)
    #data=ssdata.objects.filter(zch=zch)
    #ssdata.objects.get()
    #ssdata.objects.get(Q(zch=zch) | Q(xydm=zch))
    data=ssdata.objects.filter(Q(zch=zch) | Q(xydm=zch))
    #data=ssdata.objects.get(zch=zch.decode('raw_unicode_escape').encode('GBK'))
    
    #data=ssdata.objects.filter(zch='430105600434486')
    #print data.all()
    #print([c.zch for c in data])

    #####ADD
    '''
    page_size=6
    paginator = Paginator(data, page_size)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
        print page
     
    try:
        posts = paginator.page(page)
    except (EmptyPage, InvalidPage):
        posts = paginator.page(paginator.num_pages)         
    #####ADD
    '''
    
    t = loader.get_template('ml/qyxx.html')
    c = {'posts': data,'title':'企业（个体户）基本信息','exportfiletype':''}
    #return HttpResponse(u"欢迎光临 自强学堂!")
    return HttpResponse(t.render(c))


def querydata(request):
    
    
    #c = PostForm()
    
    if request.method == 'POST':# 当提交表单时
        form = PostForm(request.POST) # form 包含提交的数据

        if form.is_valid():# 如果提交的数据合法
            strzch = form.cleaned_data['zch']
             
            #strzch = request.POST['zch']  
            #zch=form.get('zch',1) 
            #strzch='431300000055183'
            #djjg=request.POST['djjg']  
            #data=ssdata.objects.filter(Q(zch=strzch) | Q(xydm=strzch)| Q(djjg=djjg))
            print strzch
            data=ssdata.objects.filter(Q(zch=strzch) | Q(xydm=strzch))
            #t = loader.get_template('query.html')
            c = Context({'posts': data})
            #return HttpResponse(u"欢迎光临 自强学堂!")
            #return HttpResponse(t.render(c))
            #return render(request, 'query.html', {'form': c})
            print '11111111111111111111'
            print data
        else:
            c = PostForm()
            print '22222222222222222'
    else:# 当正常访问时
        c = PostForm()
        print '333333333333333'
        #t = loader.get_template('query.html')
        
    
    t = loader.get_template('ml/query.html')
    #return render(request, 'query.html', {'form': c})
    #return render_to_response('query.html',{'form':c}, RequestContext(request) )

    #return HttpResponse(t.render(c))
    #return render(request, 'query.html', {'form': c})
    return render_to_response('ml/query.html', {'form': c})    





