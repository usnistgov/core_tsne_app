var tsnePlot = document.getElementById('tsne-plot');
var dataId = $("#data_id").html();

var NOT_SELECTED_COLOR = 'rgb(130, 130, 200)';
var SELECTED_COLOR = 'rgb(100, 230, 130)';

var NOT_SELECTED_SIZE = 8;
var SELECTED_SIZE = 20;

Plotly.d3.csv(downloadLatestUrl, function (err, rows) {
    var x = [], y = [], titles = [], ids = [], colors = [], sizes=[];
    for (var i = 0; i < rows.length; i++) {
        var row = rows[i];
        x.push(row['X']);
        y.push(row['Y']);
        ids.push(row['id']);
        titles.push(row['title']);

        if (dataId == row['id']){
            sizes.push(SELECTED_SIZE);
            colors.push(SELECTED_COLOR);
        }else {
            sizes.push(NOT_SELECTED_SIZE);
            colors.push(NOT_SELECTED_COLOR);
        }
    }

    var data = [{
        mode: 'markers',
        name: titles,
        x: x,
        y: y,
        ids: ids,
        text: titles,
        marker: {
            size: sizes,
            color: colors
        }
    }];

    var layout = {
        xaxis: {title: 'X'},
        yaxis: {title: 'Y'}
    };

    Plotly.newPlot("tsne-plot", data, layout, {
        modeBarButtonsToRemove: ['sendDataToCloud', 'hoverCompareCartesian', 'autoScale2d', 'hoverClosestCartesian']
    });
    // Select Zone prints IDs
    //https://plot.ly/javascript/plotlyjs-events/#select-event
    tsnePlot.on('plotly_selected', function (data) {
        if (data != undefined) {
            var links = "";
            data.points.forEach(function (pt) {
                links += "<a target=\"_blank\" style=\"color:"+pt['marker.color']+"\" href=\""+dataDetailsUrl+"?id="
                    + pt.id + "\">" + pt.text + "</a> ";
            });

            $('#documents').html(links);
        }
    });
});
