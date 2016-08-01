#coding:utf-8

from django.conf.urls import patterns, include, url


from django.conf.urls import url
#from django.contrib import admin
#import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from minglu import views
from simple import views_site
from simple import views_admin
from simple import views
from django.views.static import  serve
#import xadmin                 # 添加该行
 


urlpatterns =[
	
	#后台页面部分
	url(r'^admin/index$', views_admin.index),
	url(r'^admin/admin$', views_admin.admin),
	
	#验证码
	url(r'^admin/get_code$', views_admin.get_code),

	#后台请求数据部分
	url(r'^admin/ajax_login$', views_admin.ajax_login),
	url(r'^admin/ajax_logout$', views_admin.ajax_logout),
	url(r'^admin/ajax_menu_list$', views_admin.ajax_menu_list),
	url(r'^admin/ajax_admin_list$', views_admin.ajax_admin_list),
	url(r'^admin/ajax_admin_add$', views_admin.ajax_admin_add),
	url(r'^admin/ajax_admin_del$', views_admin.ajax_admin_del),
	url(r'^admin/ajax_admin_updatepwd$', views_admin.ajax_admin_updatepwd),	
	url(r'^admin/ajax_art_single_get$', views_admin.ajax_art_single_get),
	url(r'^admin/ajax_art_single_update$', views_admin.ajax_art_single_update),	
	url(r'^admin/ajax_dataclass_list$', views_admin.ajax_dataclass_list),
	url(r'^admin/ajax_dataclass_get$', views_admin.ajax_dataclass_get),	
	url(r'^admin/ajax_dataclass_add$', views_admin.ajax_dataclass_add),
	url(r'^admin/ajax_dataclass_del$', views_admin.ajax_dataclass_del),	
	url(r'^admin/ajax_data_list$', views_admin.ajax_data_list),
	url(r'^admin/ajax_data_get$', views_admin.ajax_data_get),	
	url(r'^admin/ajax_data_add$', views_admin.ajax_data_add),
	url(r'^admin/ajax_data_del$', views_admin.ajax_data_del),
	
	#前台
	#url(r'^site/index$', views_site.index),
	
	
	
	
	
	
	
	
	
	url(r'^admin/ajax_logout/$', views_admin.ajax_login),
	url(r'^$', views.showindex),
	url(r'^qiye/$', views.show),
	url(r'^geti/$', views.showgeti),
	url(r'^zhuxiao/$', views.showzhuxiao),
	url(r'^sheli/$', views.showsheli),
	url(r'^qyxx$', views.showqyxx),	 
	#url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{ 'document_root': settings.STATIC_ROOT }),
	#url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
	#url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATICFILES_DIRS, 'show_indexes': True}),
	#url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_PATH}),
	#url(r'^static/(?P<path>.*)$',serve,{'document_root':settings.STATIC_ROOT}),  
	url(r'^exportcsv/$', views.exportCSV),
	url(r'^query/$', views.querydata),
	
	
	
	

]
