#coding:utf-8

web_name = "长沙市统计局工商名录管理系统"
jquery = "http://ajax.useso.com/ajax/libs/jquery/2.1.1/jquery.min.js" #jquery2.0以上
page_size = 16

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
				"name": "管理员管理",
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
				]
			},
			{
				"id": 10,
				"name": "名录查询系统",
				"child_menu": [
					{
						"id": 11,
						"name": "工商企业查询",
						"url": "/qiye/",
					},
					{
						"id": 12,
						"name": "工商个体户",
						"url": "admin_list.html",
					},
				]
			},
		]
	},
	
]
