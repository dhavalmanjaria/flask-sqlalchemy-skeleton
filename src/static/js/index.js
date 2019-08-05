$(function() {
	var form = $('#login-form');

	form.submit(function(ev) {
		ev.preventDefault();

		var json_data = JSON.stringify($(this).elements);

		console.log(json_data);

		$.ajax({
			type: 'POST',
			url: 'api/v1/users/new',
			data: json_data,
			success: function() {
				console.log("OK");
			},
			error: function() {
				console.log("ERR");
			},
			dataType: 'json',
			contentType: 'application/json'
		});
	});
})