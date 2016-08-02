#coding:utf-8

web_name = "长沙市统计局工商名录管理系统"
jquery = "http://ajax.useso.com/ajax/libs/jquery/2.1.1/jquery.min.js" #jquery2.0以上
page_size = 10

#后台菜单，只支持3级
admin_menu_list = [
	{ 
		"id": 1, 
		"name": "后台管理", 
		"selected": True, 
		"child_menu": [
			{
				"id": 2,
				"name": "数据管理",
				"child_menu": [
					{
						"id": 5,
						"name": "分类列表",
						"url": "dataclass_list.html",
						"param": "type:1", #demo type:1,id:2
					},
					{
						"id": 6,
						"name": "数据列表",
						"url": "data_list.html",
						"param": "type:1",
					},
				]
			},
			{
				"id": 3,
				"name": "区域管理",
				"child_menu": [
					{
						"id": 7,
						"name": "区域管理1",
						"url": "art_single.html",
						"param": "id:1",
					},
				]
			},
			{
				"id": 4,
				"name": "用户管理",
				"child_menu": [
					{
						"id": 8,
						"name": "修改密码",
						"url": "admin_pwd.html",
					},
					{
						"id": 9,
						"name": "管理员列表",
						"url": "admin_list.html",
					},
					{
						"id": 91,
						"name": "添加管理员",
						"url": "admin_add.html",
					},
				]
			},
			{
				"id": 10,
				"name": "商事平台数据浏览",
				"child_menu": [
					{
						"id": 11,
						"name": "企业",
						"url": "ml_qyxx.html",
						"param":"qylx:qiye",
						#param是用于  /admin/ajax_ml_list?qylx=qiye  的参数  在js文件中写入
					},
					{
						"id": 12,
						"name": "个体户",
						"url": "ml_qyxx.html",
						"param":"qylx:geti",
					},
				]
			},
			{
				"id": 13,
				"name": "工商数据浏览",
				"child_menu": [
					{
						"id": 14,
						"name": "新登记企业",
						"url": "ml_slzx.html",
						"param":"dengjileixin:new",
					},
					{
						"id": 15,
						"name": "注销企业",
						"url": "ml_slzx.html",
						"param":"dengjileixin:destory",
					},
				]
			},					
		]
	},
	
]
