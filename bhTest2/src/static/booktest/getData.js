//查询省信息
$(function(){
	$.get('pro/0',function(data){
		$.each(data.data,function(index,item){
		$('#pro').append('<option   value="'+item[0]+'">'+item[1]+'</option>')
		});
	});
	
	$("#pro").change(function(){
		var id = $(this).val();
		$("#city").empty();
		$("#city").append('<option value="">请选择市</option>');
		$.get('city/'+id,function(data){
			$.each(data.data,function(index,item){
				$('#city').append('<option   value="'+item[0]+'">'+item[1]+'</option>')
			});
			});
		});
	$("#city").change(function(){
		var id = $(this).val();
		$("#dis").empty();
		$("#dis").append('<option value="">请选择县</option>');
		$.get('dis/'+id,function(data){
			$.each(data.data,function(index,item){
				$('#dis').append('<option   value="'+item[0]+'">'+item[1]+'</option>')
			})
		})
	})
	});
