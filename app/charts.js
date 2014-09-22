
var COLORS = [
  'red',    'black', 
  'green',  'orange',
  'blue',   'purple',
  'cyan',   'magenta',
  'green', 'blue',
  'yellow', 'brown'
];

function makeChart(elemid, title, sers) {
    var myChart = new Highcharts.Chart({
                'chart': {
                    'renderTo'          : elemid,
                    'defaultSeriesType' : 'line',
                    'zoomType'          : 'xy'
                },
                'title' : {
                    'text' : title       // chart title
                },
                xAxis : {
                    title : {
                        enabled : true,
                        text : "point"// x label
                    },
                    startOnTick : false,
                    endOnTick : false,
                    showLastLabel : true,
//                    categories : cats  // x series
                },
                yAxis : {
                    title : {
                        text : 'amplitude'
                    }
                },
                tooltip : {
                    formatter : function() {
                        return "x: " + this.x + "<br/>y: " + this.y;
                    }
                },
                legend : {
                    layout : 'vertical',
                    align : 'left',
                    verticalAlign : 'top',
                    x : 5,
                    y : 5,
                    floating : false,
                    backgroundColor : '#FFFFFF',
                    borderWidth : 1
                },
                plotOptions : {
                    scatter : {
                        marker : {
                            radius : 5,
                            states : {
                                hover : {
                                    enabled : true,
                                    lineColor : 'rgb(100,100,100)'
                                }
                            }
                        },
                        states : {
                            hover : {
                                marker : {
                                    enabled : false
                                }
                            }
                        }
                    }
                }, 
                series: sers.map(function(s, ix) {
                    if (ix > COLORS.length) {
                        throw new Error('colors exhausted');
                    }
                    return {'data': s.data, 
                            'name': s.name, 
                            'marker': {'radius': 2}, 
                            'visible': false,
                            'color': COLORS[ix]};
                })
    });
    return myChart;
}

