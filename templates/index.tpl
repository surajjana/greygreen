<!DOCTYPE html>
<html>
<head>
    <title>Scatter Time Series</title>
    <script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>


<body>
  
  <div id="myDiv" style="width: 480px; height: 400px;"><!-- Plotly chart will be drawn inside this DIV --></div>
  <script>
    var data = [
      {
        x: ['2016-10-24 13:00:00', '2016-10-24 13:30:00', '2016-10-24 14:2:41'],
        y: [1, 3, 4],
        type: 'scatter',
        name: 'Restaurant 1'
      }
    ];

    Plotly.newPlot('myDiv', data);
  </script>
</body>

</html>