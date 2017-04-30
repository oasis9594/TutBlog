$("#image-holder").click(function() {
		$("#fileUpload").click();
	});
	function readURL(input){
		var ext = input.files[0]['name'].substring(input.files[0]['name'].lastIndexOf('.') + 1).toLowerCase();
		if (input.files && input.files[0] && (ext == "gif" || ext == "png" || ext == "jpeg" || ext == "jpg")){
			var reader = new FileReader();
			reader.onload = function (e) {
				$('#my-image').attr('src', e.target.result);
			}

			reader.readAsDataURL(input.files[0]);
		}else{
			$('#my-image').attr('src', '../static/img/apple-icon.png');
		}
	}