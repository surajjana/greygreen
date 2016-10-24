<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Grey Green | Adding Grey Restaurant Data</title>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>

    <!-- <link rel="stylesheet" type="text/css" href="../test.css"> -->

    <script type="text/javascript">

    $(document).ready(function(){
    	
    	$("#content").on("change paste keyup", function() {
    		var x = 320 - $(this).val().length 
    		if(x >= 0){
    			$("#char_val").css("color", "blue")
    			$("#char_val").text(x + " characters remaining")
    		}else if(x < 0){
    			$("#char_val").css("color", "red")
    			$("#char_val").text(x + " characters remaining")
    		}
		})

		$.fn.serializeFormJSON = function () {
	        var o = {};
	        var a = this.serializeArray();
	        $.each(a, function () {
	            if (o[this.name]) {
	                if (!o[this.name].push) {
	                    o[this.name] = [o[this.name]];
	                }
	                o[this.name].push(this.value || '');
	            } else {
	                o[this.name] = this.value || '';
	            }
	        });
	        return o;
	    };

		$('#submit').click(function(){
			var data = $('#test').serializeFormJSON();

			
    		$.post('http://localhost:8000/add_data', data, function(data){

            	console.log(data)
            	var data = JSON.parse(data)

              	if(data.status == 'OK'){
                 	console.log('data inserted')
                 	alert('Data Inserted')
              	}else{
                	console.log('not valid')
                	alert('Not Valid')
              	}
           	})
	        
		})

    })

    </script>

</head>

<body>

<center><h2>Adding Grey Green Restaurant Data</h2></center>
<br /><br />

<center>
	<form id="test" action="#" method="post">
		Restaurant ID<br />
		<input type="text" name="r_id" placeholder="Restaurant ID (1 to 20)" > <br /><br />
		Time<br />
		<input type="text" name="r_time" placeholder="YYYY-MM-DD HH:MM:SS" > <br /><br />
		User Rating<br />
		<input type="text" name="rating" placeholder=" ( 1 to 5 ) " > <br /><br />
		
		
		<input type="button" name="submit" id="submit" value="Submit"> <br />
	</form>

</center>

</body>

</html>