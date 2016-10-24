<!DOCTYPE html>

<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="utf-8" />
  <title></title>
  <script src="../Chart.Core.js"></script>
  <script src="../Chart.Scatter.js"></script>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/3.3.4/js/bootstrap.min.js"></script>
</head>
<body>
  <canvas id="header-canvas" width="200" height="80"></canvas>
  <div id="legend"></div>

  <script>

    Chart.defaults.global.responsive = true;
    Chart.defaults.global.animation = false;

    $(document).ready(function () {

      $("#show").click(function(){
        console.log('Show clicked...');
        $.getJSON('http://127.0.0.1:8000/json_data', function(jd){

        console.log(JSON.stringify(jd));
        
        var data3 = [];

        var color = ['#cd6155','#9b59b6','#2980b9','#48c9b0','#16a085','#186a3b','#f4d03f','#b7950b','#ca6f1e','#ba4a00','#7b7d7d','#7f8c8d','#2e4053','#17202a','#1b4f72','#512e5f','#28b463','#e6b0aa','#239b56','#7d3c98']

        for (var i=0; i<jd.length; i++){
          data3[i] = {'label': jd[i].name, 'strokeColor': color[i], 'data':[]}
          for (var j = 0; j < jd[i].x.length; j++){
            data3[i].data[j] = {'x': new Date(jd[i].x[j]), 'y': jd[i].y[j]}
          }
        }

        var ctx3 = document.getElementById("header-canvas").getContext("2d");
        var myDateLineChart = new Chart(ctx3).Scatter(data3, {
          bezierCurve: true,
          showTooltips: true,
          scaleShowHorizontalLines: true,
          scaleShowLabels: true,
          scaleType: "date",
          scaleLabel: "<%=value%>"
        });

      });  

      });

          
    });
  </script>
  <button id="show">Show Data</button>
</body>
</html>
