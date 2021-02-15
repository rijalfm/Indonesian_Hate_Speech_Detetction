$(document).ready(function() {

	function formToJSON($form) {
		var formArray = $form.serializeArray();
		var formJSON = {};

		$.map(formArray, function(n, i) {
			formJSON[n['name']] = n['value'];
		})

		return formJSON;
	}


	$('#submit').click(function(e){
		e.preventDefault();
		var data = formToJSON($('#text-data'));
		$.ajax({
			url: 'http://127.0.0.1:5000/api/text',
			method: 'POST',
			data: data,
			success: function(data){
				$('.results').empty();
				var hateSpeech = data['hate_speech'];
				var abuse = data['abusive'];

				if (hateSpeech == '0') {
					$('.results').append('<div class="h5"><span class="badge rounded-pill bg-success">Not Hate Speech</span></div>');
				} else {
					$('.results').append('<div class="h5"><span class="badge rounded-pill bg-danger">Hate Speech</span></div>');
				}

				if (abuse.length > 0) {
					var msg = '<div class="card mt-3"><div class="card-header">Abusive Words</div><ul class="list-group">';
					for (const word of abuse) {
						msg += '<li class="list-group-item"><strong  style="text-transform: capitalize;">'+word['abusive_word']+
						'</strong> <span  style="text-transform: uppercase;"> ['+word['category']+']</span></li>'
					}
					$('.results').append(msg);
				} else {
					var msg = '<div class="card mt-3"><div class="card-header">Abusive Words</div><ul class="list-group">'+
										'<li class="list-group-item text-center">No Abusive Words</li></ul></div>';

					$('.results').append(msg);
				}
			},
			error: function(data){
				var msg = '<div class="alert alert-danger alert-dismissible fade show" role="alert">' +
          'Text can\'t be empty!' +
          '<button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button></div>'
				$('.results').empty();
				$('.results').append(msg);
			}
		})
	})
})