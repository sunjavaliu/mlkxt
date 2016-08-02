
var curr_page = 1; //当前页
var request_data = true; //这个变量是为了防止请求完数据后，更新分页导航数据时反复请求数据

function show_data(list) {
	$(".listing > tbody").empty();

	//title部分
	var item_str = '<tr>';
	item_str += '<th class="first">注册号</th>';
	item_str += '<th>名称</th>';
	item_str += '<th>法定代表人</th>';
	item_str += '<th>主营项目类别</th>';
	//item_str += '<th>经营范围</th>';
	item_str += '<th>住所(经营场所)</th>';
	item_str += '<th>注册资本(万元人民币)</th>';
	item_str += '<th>商事主体类型</th>';
	item_str += '<th>成立日期</th>';
	item_str += '<th>营业期限</th>';
	item_str += '<th>核发日期</th>';
	item_str += '<th>登记机关</th>';
	item_str += '<th>状态</th>';
	item_str += '<th>统一信用代码</th>';
	item_str += '<th class="last">操作</th>';
	item_str += '</tr>';
	$(".listing > tbody").append(item_str);
	
	for(var i in list) {
		var item = list[i];
		
		item_str = '<tr class="bg">';
		item_str += '<td class="first style1">' + item.zch + '</td>';
		item_str += '<td id="mc">' + item.mcyename  + '</td>'
		item_str += '<td id="fddbr">' + item.fddbri  + '</td>'
		item_str += '<td id="zyxmlb">' + item.zyxmlb  + '</td>'
		//item_str += '<td id="jyfw">' + item.jyfw  + '</td>'
		item_str += '<td id="dz">' + item.dz  + '</td>'
		item_str += '<td id="rjzczb">' + item.rjzczb  + '</td>'
		item_str += '<td id="qylx">' + item.qylx  + '</td>'
		item_str += '<td id="clrq">' + item.clrq  + '</td>'
		item_str += '<td id="yyqx">' + item.yyqx  + '</td>'
		item_str += '<td id="hzrq">' + item.hzrq  + '</td>'
		item_str += '<td id="djjg">' + item.djjg  + '</td>'
		item_str += '<td id="ztzt">' + item.zt  + '</td>'
		item_str += '<td id="xydm">' + item.xydm  + '</td>'
		item_str += '<td class="last"><a href="#" class="btn_del" id="btn_del_' + item.id + '">删除</a></td>';
		item_str += '</tr>';
		$(".listing > tbody").append(item_str);
	}
	
	//删除按钮
	$(".btn_del").click(function() {
		if(confirm("确认删除吗？")) {
			var id = $(this).attr("id").split("_")[2];
			$.getJSON(
				"ajax_admin_del?id=" + id + "&random=" + Math.random(),
				function(data) {
					do_page();
				}
			);
		}
		return false;
	});
}

function update_page_nav(data) {
	
	var opt = {
		callback: function(page_index, jq) {
			curr_page = page_index + 1;
			if(request_data) {
				request_data = false;
				do_page();
			}
			else
				request_data = true;
			return false;
		},
		items_per_page: data.page_size,
		current_page: curr_page - 1,
		num_edge_entries: 1
	};
	
	$("#Pagination").pagination(data.total, opt);
}

function do_page() {
	$.getJSON(
		"ajax_ml_list?page=" + curr_page + "&random=" + Math.random(),
		function(data) {
			show_data(data.data.list);
			update_page_nav(data.data);			
		}
	);
}

$(function() {
	//alert(window.document.location.href)
	$.getJSON(
		"ajax_ml_list?random=" + Math.random(),
		function(data) {
			if(data.data.page_count == 1) {
				$(".pagetable").hide(); //只有一页的话就不显示分页导航
				
				show_data(data.data.list);
			}
			else {
				show_data(data.data.list);				
				update_page_nav(data.data);
			}
		}
	);
	
	//添加按钮
	$("#add_btn").click(function() {
		$("#center-column").load("../../static/simple/admin_templates/admin_add.html?random=" + Math.random());
		return false;
	});
	
});
