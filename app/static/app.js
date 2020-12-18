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
      c3.generate({
        bindto: '#temperature-chart-last-hour',
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

    // humidity

    columns = [
      ['x'].concat(data.time),
      ['humidity'].concat(data.humidity)
    ]
    c3.generate({
      bindto: '#humidity-chart-last-hour',
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

    // pressure

    columns = [
      ['x'].concat(data.time),
      ['pressure'].concat(data.pressure)
    ]
    c3.generate({
      bindto: '#pressure-chart-last-hour',
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
