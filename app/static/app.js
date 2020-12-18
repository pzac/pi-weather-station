function last_hour_charts(data) {
    c3.generate({
      bindto: '#temperature-chart-last-hour',
        data: {
          x: 'x',
          xFormat: '%Y-%m-%d %H:%M:%S',
          columns: [
            ['x'].concat(data.time),
            ['ext_temp'].concat(data.ext_temp),
            ['int_temp'].concat(data.int_temp),
            ['bar_temp'].concat(data.bar_temp)
          ],
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
  c3.generate({
    bindto: '#humidity-chart-last-hour',
      data: {
        x: 'x',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: [
          ['x'].concat(data.time),
          ['humidity'].concat(data.humidity)
        ]
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
  c3.generate({
    bindto: '#pressure-chart-last-hour',
      data: {
        x: 'x',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: [
          ['x'].concat(data.time),
          ['pressure'].concat(data.pressure)
        ]
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
}

function last_24_hours_charts(data) {
    c3.generate({
      bindto: '#temperature-chart-last-24-hours',
        data: {
          x: 'x',
          xFormat: '%Y-%m-%d %H:%M:%S',
          columns: [
            ['x'].concat(data.time),
            ['ext_temp'].concat(data.ext_temp),
            ['int_temp'].concat(data.int_temp),
            ['bar_temp'].concat(data.bar_temp)
          ],
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
  c3.generate({
    bindto: '#humidity-chart-last-24-hours',
      data: {
        x: 'x',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: [
          ['x'].concat(data.time),
          ['humidity'].concat(data.humidity)
        ]
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
  c3.generate({
    bindto: '#pressure-chart-last-24-hours',
      data: {
        x: 'x',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: [
          ['x'].concat(data.time),
          ['pressure'].concat(data.pressure)
        ]
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
}

document.addEventListener('DOMContentLoaded', function(){
  fetch('/last-hour.json')
    .then(response => response.json())
    .then(data => {last_hour_charts(data)});

  fetch('/last-24-hours.json')
    .then(response => response.json())
    .then(data => {last_24_hours_charts(data)});

});
