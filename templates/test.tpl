<!DOCTYPE html>
<html lang="en">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <title>Krispypapad | Content Admin Portal</title>

    <!-- <link rel="stylesheet" type="text/css" href="../test.css"> -->

</head>

<body>

<center><img src="../logo.png" width="200"></center>

<center><h2>Krispypapad Content Admin Portal</h2></center>
<br /><br />

<center>
	<form action="/insert_article" method="post">
		Article Title<br />
		<input type="text" name="title" placeholder="Article Title" > <br /><br />
		Original Article Link<br />
		<input type="text" name="article_link" placeholder="Original Article Link"> <br /><br />
		Domain<br />
		<input type="text" name="domain" placeholder="CSE,ECE, etc.."> <br /><br />
		<input type="submit" name="submit" value="Submit"> <br />
	</form>

	<br /><br />
	<center><h4>Total Article Count : {{count}}</h4></center>
</center>

</body>

</html>