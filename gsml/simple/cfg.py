#coding:utf-8

web_name = "长沙市统计局工商名录管理系统"
jquery = "http://ajax.useso.com/ajax/libs/jquery/2.1.1/jquery.min.js" #jquery2.0以上
page_size = 10
gs_Page_size=20
ss_Page_size=10
#后台菜单，只支持3级
admin_menu_list = [
	{ 
		"id": 1, 
		"name": "后台管理", 
		"selected": True, 
		"child_menu": [
			{
				"id": 2,
				"name": "用户维护",
				"child_menu": [
					{
						"id": 3,
						"name": "添加用户",
						"url": "admin_add.html",
					},					
					{
						"id": 4,
						"name": "用户列表",
						"url": "admin_list.html",
					},
					{
						"id": 5,
						"name": "修改密码",
						"url": "admin_pwd.html",
					},
				]
			},
			{
				"id": 6,
				"name": "商事平台数据浏览",
				"child_menu": [
					{
						"id": 7,
						"name": "浏览企业数据",
						"url": "ml_qyxx.html",
						"param":"qylx:qiye",
						#param是用于  /admin/ajax_ml_list?qylx=qiye  的参数  在js文件中写入
					},
					{
						"id": 8,
						"name": "浏览个体户数据",
						"url": "ml_qyxx.html",
						"param":"qylx:geti",
					},
				]
			},
			{
				"id": 9,
				"name": "工商数据浏览",
				"child_menu": [
					{
						"id": 10,
						"name": "新登记企业",
						"url": "ml_slzx.html",
						"param":"dengjileixin:sheli",
					},
					{
						"id": 11,
						"name": "注销企业",
						"url": "ml_slzx.html",
						"param":"dengjileixin:zhuxiao",
					},
				]
			},		
			{
				"id": 12,
				"name": "快速链接",
				"child_menu": [
					{
						"id": 13,
						"name": "长沙市商事平台",
						"url": "ml_slzx.html",
					},
					{
						"id": 14,
						"name": "长沙市工商局平台",
						"url": "ml_slzx.html",
					},
				]
			},				
		]
	},
	
]
