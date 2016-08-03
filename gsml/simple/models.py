#coding:utf-8

from django.db import models
import json
import time
import commons
from django.db.models import Q

def to_json(obj):
	fields = []
	for field in obj._meta.fields:
		fields.append(field.name)
	d = {}
	for attr in fields:
		val = getattr(obj, attr)
		
		#如果是model类型，就要再一次执行model转json
		if isinstance(val, models.Model):
			val = json.loads(to_json(val))
		d[attr] = val
	return json.dumps(d)

class Admin(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	pwd = models.CharField(max_length = 50)
	add_time = models.IntegerField(default = 0)
	userlevel = models.IntegerField(default = 0)
	
	def toJSON(self):
		return to_json(self)
	
	#获取分页数据，静态方法
	@staticmethod
	def getList(page, page_size):
		total = Admin.objects.all().count()
		page_count = commons.page_count(total, page_size)
	
		offset = (page - 1) * page_size
		limit = offset + page_size
		admin_list = Admin.objects.all().order_by("-id")[offset:limit]
		
		admin_list_json = []
		for admin in admin_list:		
			item = json.loads(admin.toJSON())
			item["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["add_time"]))
			
			#移除密码
			del item["pwd"]
			admin_list_json.append(item)
	
		data = {
			"page_size": page_size,
			"page_count": page_count,
			"total": total,
			"page": page,
			"list": admin_list_json,
		}
		return data

class ArtSingle(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	content = models.TextField()
	
	def toJSON(self):
		return to_json(self)
	
class DataClass(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	parent_id = models.IntegerField(default = 0)
	sort = models.IntegerField(default = 0)
	type = models.IntegerField(default = 0)

	def toJSON(self):
		return to_json(self)
		
	#递归删除分类，静态方法
	@staticmethod
	def deleteById(id):
		dc_list = DataClass.objects.filter(parent_id = id)
	
		for dc in dc_list:
			child_count = DataClass.objects.filter(parent_id = dc.id).count()
			if child_count > 0:
				DataClass.deleteById(dc.id)
		
			#删除该分类下面的对应数据
			Data.objects.filter(dataclass_id = dc.id).delete()
			dc.delete()
			
	#递归获取父分类的dict，静态方法
	@staticmethod
	def getById(id):
		dataclass = DataClass.objects.get(id = id)
		dataclass_json = json.loads(dataclass.toJSON())	
		if dataclass_json["parent_id"] != 0:
			dataclass_json["parent"] = DataClass.getById(dataclass_json["parent_id"])	
		return dataclass_json
		
	#递归获取该分类下的分类(返回list)，静态方法
	@staticmethod
	def listById(id):
		dc_list = DataClass.objects.filter(parent_id = id).order_by("-sort", "-id")
		dc_list_json = []
		for dc in dc_list:
			item = json.loads(dc.toJSON())
				
			child_count = DataClass.objects.filter(parent_id = item["id"]).count()
			if child_count > 0:
				item["children"] = DataClass.listById(item["id"])
			
			dc_list_json.append(item)

		return dc_list_json

class Data(models.Model):
	id = models.AutoField(primary_key = True)
	name = models.CharField(max_length = 50)
	content = models.TextField()
	add_time = models.IntegerField(default = 0)
	dataclass = models.ForeignKey(DataClass)
	sort = models.IntegerField(default = 0)
	type = models.IntegerField(default = 0)
	hits = models.IntegerField(default = 0)
	picture = models.CharField(max_length = 50)

	def toJSON(self):
		return to_json(self)
	
	#获取分页数据，静态方法
	@staticmethod
	def getList(page, page_size, type):
		total = Data.objects.filter(type = type).count()
		page_count = commons.page_count(total, page_size)
	
		offset = (page - 1) * page_size
		limit = offset + page_size
	
		data_list = Data.objects.filter(type = type).order_by("-sort", "-id")[offset:limit]
		data = []
		for i in data_list:
			item = json.loads(i.toJSON())
			item["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["add_time"]))
			data.append(item)
	
		data = {
			"page_size": page_size,
			"page_count": page_count,
			"total": total,
			"page": page,
			"list": data,
		}
		return data






































class ssdata(models.Model):
	'''
	title = models.CharField(max_length = 150)
	content = models.TextField()
	timestamp = models.DateTimeField()
	'''
	
	zch = models.TextField()
	mcyename = models.TextField()
	fddbri = models.TextField()
	zyxmlb = models.TextField()
	dz = models.TextField()
	rjzczb = models.TextField()
	qylx = models.TextField()
	clrq = models.TextField()
	yyqx = models.TextField()
	hzrq = models.TextField()
	djjg = models.TextField()
	zt = models.TextField()
	jyfw = models.TextField()
	xydm = models.TextField() 
	#def __unicode__(self):
	#	return self.name
	def toJSON(self):
		return to_json(self)
	
	#获取分页数据，静态方法
	@staticmethod
	def getList(page, page_size,dzm,qylx):
		
		print("start")
		print(qylx)
		if dzm=="430100":
			if qylx == "qiye" :
				total=ssdata.objects.exclude(qylx__icontains="个体").count()
			else:
				total= data=ssdata.objects.filter(qylx__contains="个体").count()
		else:
			if qylx == "qiye" :
				total=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).exclude(qylx__icontains="个体").count()
			else:
				total=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).filter(qylx__contains="个体").count()
		#total = ssdata.objects.all().count()
		page_count = commons.page_count(total, page_size)
		offset = (page - 1) * page_size
		limit = offset + page_size
		#ss_list = ssdata.objects.all().order_by("-id")[offset:limit]
	
		if dzm=="430100":
			if qylx == "qiye" :
				ss_list=ssdata.objects.exclude(qylx__icontains="个体").order_by("-id")[offset:limit]
			else:
				ss_list= data=ssdata.objects.filter(qylx__contains="个体").order_by("-id")[offset:limit]
		else:
			if qylx == "qiye" :
				ss_list=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).exclude(qylx__icontains="个体").order_by("-id")[offset:limit]
			else:
				ss_list=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).filter(qylx__contains="个体").order_by("-id")[offset:limit]

		ss_list_json = []
		for ss in ss_list:		
			item = json.loads(ss.toJSON())
			#item["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["add_time"]))
			
			#移除密码
			#del item["pwd"]
			ss_list_json.append(item)
	
		data = {
			"page_size": page_size,
			"page_count": page_count,
			"total": total,
			"page": page,
			"list": ss_list_json,
		}
		print(data)
		return data
	
	class Meta:
		db_table = 'ssjibenxinxi'   #指定表名
		ordering = ['-hzrq']		#按核准日期排序
		
class gszxdata(models.Model):
	'''
	title = models.CharField(max_length = 150)
	content = models.TextField()
	timestamp = models.DateTimeField()
	'''
	
	zch = models.TextField()
	qiyename = models.TextField()
	hzriqi = models.TextField()
	djjg = models.TextField()


	def toJSON(self):
		return to_json(self)
	
	#获取分页数据，静态方法
	@staticmethod
	def getList(page, page_size,dzm,qylx):
		
		print("start")
		print(qylx)
		if dzm=="430100":
			if qylx == "qiye" :
				total=ssdata.objects.exclude(qylx__icontains="个体").count()
			else:
				total= data=ssdata.objects.filter(qylx__contains="个体").count()
		else:
			if qylx == "qiye" :
				total=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).exclude(qylx__icontains="个体").count()
			else:
				total=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).filter(qylx__contains="个体").count()
		#total = ssdata.objects.all().count()
		page_count = commons.page_count(total, page_size)
		offset = (page - 1) * page_size
		limit = offset + page_size
		#ss_list = ssdata.objects.all().order_by("-id")[offset:limit]
	
		if dzm=="430100":
			if qylx == "qiye" :
				ss_list=ssdata.objects.exclude(qylx__icontains="个体").order_by("-id")[offset:limit]
			else:
				ss_list= data=ssdata.objects.filter(qylx__contains="个体").order_by("-id")[offset:limit]
		else:
			if qylx == "qiye" :
				ss_list=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).exclude(qylx__icontains="个体").order_by("-id")[offset:limit]
			else:
				ss_list=ssdata.objects.filter(Q(zch__startswith=dzm)|Q(xydm__startswith="__"+dzm)).filter(qylx__contains="个体").order_by("-id")[offset:limit]

		ss_list_json = []
		for ss in ss_list:		
			item = json.loads(ss.toJSON())
			#item["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["add_time"]))
			
			#移除密码
			#del item["pwd"]
			ss_list_json.append(item)
	
		data = {
			"page_size": page_size,
			"page_count": page_count,
			"total": total,
			"page": page,
			"list": ss_list_json,
		}

		return data
		
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'gsqiyezhuxiao'   #指定表名
		ordering = ['-hzriqi']		#按核准日期排序	
		
		
class gssldata(models.Model):
	'''
	title = models.CharField(max_length = 150)
	content = models.TextField()
	timestamp = models.DateTimeField()
	'''
	
	zch = models.TextField()
	qiyename = models.TextField()
	hzriqi = models.TextField()
	djjg = models.TextField()


	def toJSON(self):
		return to_json(self)
	
	#获取分页数据，静态方法
	@staticmethod
	def getList(page, page_size,dzm,dengjileixin):
		
		total=gssldata.objects.filter()().count()
		#total = ssdata.objects.all().count()
		page_count = commons.page_count(total, page_size)
		offset = (page - 1) * page_size
		limit = offset + page_size
		#ss_list = ssdata.objects.all().order_by("-id")[offset:limit]
	

		ss_list=gssldata.objects.all().order_by("-id")[offset:limit]

		ss_list_json = []
		for ss in ss_list:		
			item = json.loads(ss.toJSON())
			#item["add_time"] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(item["add_time"]))
			
			#移除密码
			#del item["pwd"]
			ss_list_json.append(item)
	
		data = {
			"page_size": page_size,
			"page_count": page_count,
			"total": total,
			"page": page,
			"list": ss_list_json,
		}

		return data
		
	def __unicode__(self):
		return self.name
	
	class Meta:
		db_table = 'gsqiyesheli'   #指定表名
		ordering = ['-hzriqi']		#按核准日期排序	
		
		
#############


class Tag(models.Model):
	"""docstring for Tags"""
	tag_name = models.CharField(max_length=20, blank=True)
	create_time = models.DateTimeField(auto_now_add=True)

	def __unicode__(self):
		return self.tag_name


class Author(models.Model): 
	"""docstring for Author"""
	name = models.CharField(max_length=30)
	email = models.EmailField(blank=True)
	website = models.URLField(blank=True)

	def __unicode__(self):
		return u'%s' % (self.name)


class Blog(models.Model):
	"""docstring for Blogs"""
	caption = models.CharField(max_length=50)
	author = models.ForeignKey(Author)
	tags = models.ManyToManyField(Tag, blank=True)
	content = models.TextField()
	publish_time = models.DateTimeField(auto_now_add=True)
	update_time = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'%s %s %s' % (self.caption, self.author, self.publish_time)