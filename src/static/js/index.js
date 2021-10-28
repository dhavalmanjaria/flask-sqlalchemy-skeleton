$(function() {
	var form = $('#login-form');
	$("#log").toggleClass('alert');
	$("#log").html('');

	form.submit(function(ev) {
		ev.preventDefault();
		

		var json_data = JSON.stringify(form.serializeJSON());

		$.ajax({
			type: 'POST',
			url: 'api/v1/execute',
			data: json_data,
			success: function(res) {
				console.log("OK");
				$("#log").toggleClass('alert alert-success');
				$("#log").html('Data saved!');
				console.log(res);
			},
			error: function(res) {
				console.log("ERR");
				console.log(res['responseJSON']);
				$("#log").toggleClass('alert alert-danger');
				$("#log").html('Error: ' + res['responseJSON']['data'] );

			},
			dataType: 'json',
			contentType: 'application/json'
		});
	});
})