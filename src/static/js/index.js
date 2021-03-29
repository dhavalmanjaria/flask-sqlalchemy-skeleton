$(function() {
	var form = $('#login-form');

	form.submit(function(ev) {
		ev.preventDefault();
		$("#log").html('');

		var json_data = JSON.stringify(form.serializeJSON());

		$.ajax({
			type: 'POST',
			url: 'api/v1/execute',
			data: json_data,
			success: function(res) {
				console.log("OK");
				$("#log").toggleClass('alert-success');
				$("#log").html('Data saved!');
			},
			error: function(res) {
				console.log("ERR");
				console.log(res['responseJSON']);
				$("#log").toggleClass('alert-danger');
				$("#log").html('Error: ' + res['responseJSON']['data'] );

			},
			dataType: 'json',
			contentType: 'application/json'
		});
	});
})