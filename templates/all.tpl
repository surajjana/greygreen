<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Krispypapad | All Articles</title>

    <!-- <link rel="stylesheet" type="text/css" href="../test.css"> -->
</head>

<body style="overflow-x: hidden;font-family: 'sans';">

<center><img src="../logo.png" width="200"></center>

<center><h2>Krispypapad | All Articles</h2></center>
<br /><br />

<center><h4>Total Article Count : {{len(res)}}</h4></center> <br /><br />

<div style="margin-left: 15%; margin-right: 15%;">
% setdefault('count', 0)
% for i in range(0, len(res)):
	<li style="border: 1px solid #dbdbdb; border-radius:5px;margin-bottom: 5%;list-style: none; padding: 15px 10px; box-shadow: 1px 2px 10px -3px rgba(130,130,130,1);">
		<h3 style="margin: 0px;">
		% if (len(res[i]['title']) != 0):
			<a style="text-decoration: none;color: #2788c9;" href={{res[i]['original_article']}}>{{i+1}}. {{res[i]['title']}}</a></h3>
		% end
		% if (len(res[i]['title']) == 0):
			<a style="text-decoration: none;color: #2788c9;" href={{res[i]['original_article']}}>{{i+1}}. {{res[i]['original_article']}}</a></h3>
		% end

		<h5 style="color: #555555;font-style: italic;margin: 0px;">{{res[i]['domain']}}</h5>
	</li>
% end
</div>

</body>

</html>