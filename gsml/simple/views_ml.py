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

def ajax_ml_list(request):
    print("liu1")
    #需要登录才可以访问
    if not request.session.get("sess_admin", False):
        return commons.res_fail(1, "需要登录才可以访问")
    print("liuq1")
    #分页索引和每页显示数
    page = 1
    if request.GET.get("page"):
        page = int(request.GET.get("page"))
    page_size = cfg.page_size
    if request.GET.get("page_size"):
        page_size = int(request.GET.get("page_size"))

    res_data = ssdata.getList(page, page_size)
    print("haloo")
    print(res_data)
    return commons.res_success("请求成功", res_data)


def ajax_ml_list2(request):
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

    res_data = Admin.getList(page, page_size)
    
    return commons.res_success("请求成功", res_data)