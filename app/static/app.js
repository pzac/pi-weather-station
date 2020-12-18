document.addEventListener('DOMContentLoaded', function(){
  fetch('/last-hour.json')
    .then(response => response.json())
    .then(data => {
      let columns = [
                ['x'].concat(data.time),
                ['ext_temp'].concat(data.ext_temp),
                ['int_temp'].concat(data.int_temp),
                ['bar_temp'].concat(data.bar_temp)
            ]
      var chart = c3.generate({
        bindto: '#chart',
          data: {
            x: 'x',
            xFormat: '%Y-%m-%d %H:%M:%S',
            columns: columns
          },
          axis: {
            x: {
              type: 'timeseries',
              tick: {
                format: '%H:%M',
                rotate: -60
              }
            }
          }
      });
    });


});
