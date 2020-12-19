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
          ['bar_temp'].concat(data.bar_temp),
          ['humidity'].concat(data.humidity)
        ],
        axes: {
          ext_temp: 'y',
          int_temp: 'y',
          bar_temp: 'y',
          humidity: 'y2',
        }
      },
      axis: {
        x: {
          type: 'timeseries',
          tick: {
            format: '%H:%M',
            rotate: -60
          }
        },
        y: {
          tick: {
            format: function (d) { return d + " C" }
          }
        },
        y2: {
          show: true,
          tick: {
            format: function (d) { return d + " %" }
          }
        }
      },
      point: {
        show: false
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
        },
        y: {
          tick: {
            format: function (d) { return d + " hPa" }
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
          ['bar_temp'].concat(data.bar_temp),
          ['humidity'].concat(data.humidity)
        ],
        axes: {
          ext_temp: 'y',
          int_temp: 'y',
          bar_temp: 'y',
          humidity: 'y2',
        }
      },
      axis: {
        x: {
          type: 'timeseries',
          tick: {
            format: '%H:%M',
            rotate: -60
          }
        },
        y: {
          tick: {
            format: function (d) { return d + " C" }
          }
        },
        y2: {
          show: true,
          tick: {
            format: function (d) { return d + " %" }
          }
        }
      },
      point: {
        show: false
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
        },
        y: {
          tick: {
            format: function (d) { return d + " hPa" }
          }
        }
      },
      point: {
        show: false
      }
  });
}


function last_week_charts(data) {
  c3.generate({
    bindto: '#temperature-chart-last-week',
      data: {
        x: 'x',
        xFormat: '%Y-%m-%d %H:%M:%S',
        columns: [
          ['x'].concat(data.time),
          ['ext_temp'].concat(data.ext_temp),
          ['int_temp'].concat(data.int_temp),
          ['bar_temp'].concat(data.bar_temp),
          ['humidity'].concat(data.humidity)
        ],
        axes: {
          ext_temp: 'y',
          int_temp: 'y',
          bar_temp: 'y',
          humidity: 'y2',
        }
      },
      axis: {
        x: {
          type: 'timeseries',
          tick: {
            format: '%Y-%m-%d %H:%M',
            rotate: -60
          }
        },
        y: {
          tick: {
            format: function (d) { return d + " C" }
          }
        },
        y2: {
          show: true,
          tick: {
            format: function (d) { return d + " %" }
          }
        }
      },
      point: {
        show: false
      }
  });

  // pressure
  c3.generate({
    bindto: '#pressure-chart-last-week',
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
            format: '%Y-%m-%d %H:%M',
            rotate: -60
          }
        },
        y: {
          tick: {
            format: function (d) { return d + " hPa" }
          }
        }
      },
      point: {
        show: false
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

  fetch('/last-week.json')
    .then(response => response.json())
    .then(data => {last_week_charts(data)});

});
