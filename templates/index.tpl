<!DOCTYPE html>
<html>
<head>
    <title>Grey Green | Restaurant Data</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
</head>


<body>
  
  <div id="myDiv" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div>
  <script>
    $(document).ready(function(){
      $.getJSON('http://127.0.0.1:8000/json_data', function(jd) {

        console.log(jd);

        var data = jd;

        Plotly.newPlot('myDiv', data);
                  
      });
    });
  </script>
</body>

</html>