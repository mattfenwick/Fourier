
function makeChart(elemid, title, sers) {
    console.log('some data: ' + JSON.stringify(sers));
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
                series: sers
    });
    return myChart;
}

