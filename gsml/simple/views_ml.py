#coding:utf-8

import commons
import cfg
import json
import time
import sys
import os
import platform
import django
from DjangoCaptcha import Captcha
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from models import ssdata
from models import Admin
from models import gssldata

def ajax_ml_list(request):
    #需要登录才可以访问
    if not request.session.get("sess_admin", False):
        return commons.res_fail(1, "需要登录才可以访问")
    #分页索引和每页显示数
    page = 1
    if request.GET.get("page"):
        page = int(request.GET.get("page"))
    page_size = cfg.page_size
    if request.GET.get("page_size"):
        page_size = int(request.GET.get("page_size"))
    dzm=request.session.get("dzm", False)
    qylx=request.GET.get("qylx")
    print("企业类型")
    print(qylx)
    res_data = ssdata.getList(page, page_size,dzm,qylx)
    print("haahahahasdf")
    return commons.res_success("请求成功", res_data)

def ajax_ml_slzx_list(request):
    if not request.session.get("sess_admin", False):
        return commons.res_fail(1, "需要登录才可以访问")
    #分页索引和每页显示数
    page = 1
    if request.GET.get("page"):
        page = int(request.GET.get("page"))
    page_size = cfg.page_size
    if request.GET.get("page_size"):
        page_size = int(request.GET.get("page_size"))
    dzm=request.session.get("dzm", False)
    qylx=request.GET.get("qylx")
    res_data = gssldata.getList(page, page_size,dzm,qylx)
    return commons.res_success("请求成功", res_data)
