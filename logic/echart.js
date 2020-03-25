// PCA
var data = genData(5);

option = {
    title: {
        text: '贡献指标PCA结果',
        left: 'center'
    },
    tooltip: {
        trigger: 'item',
        formatter: ''
    },
    legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 10,
        top: 20,
        bottom: 20,
        data: data.legendData,
        selected: data.selected
    },
    series: [
        {

            type: 'pie',
            radius: '55%',
            center: ['40%', '50%'],
            data: data.seriesData,
            emphasis: {
                itemStyle: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};

function genData(count) {
    var nameList = ["commit", "add_line", "del_line", "age", "active_day"];
    var legendData = [];
    var seriesData = [];
    var selected = {};
    var l = [0.60850762,0.24800851,0.11034727,0.01971071,0.0134259];
    for (var i = 0; i < count; i++) {
        name = nameList[i];
        legendData.push(name);
        seriesData.push({
            name: name,
            value: l[i],
        });
        // selected[name] = i < 6;
    }

    return {
        legendData: legendData,
        seriesData: seriesData,
        selected: selected
    };
}

// 相关性
var hours = ["commit", "add_line", "del_line", "age", "active_day"];
var days = ["commit", "add_line", "del_line", "age", "active_day"];

var data = [[0, 0, 1.0], [0, 1, 0.7126388878481319], [0, 2, 0.7330085267547043], [0, 3, 0.5716927690096156], [0, 4, 0.9382086683784457], [1, 0, 0.712638887848132], [1, 1, 1.0], [1, 2, 0.9555522225262686], [1, 3, 0.4419738632922879], [1, 4, 0.7092603682073418], [2, 0, 0.7330085267547043], [2, 1, 0.9555522225262687], [2, 2, 1.0], [2, 3, 0.4506874641635873], [2, 4, 0.7266822817524654], [3, 0, 0.5716927690096156], [3, 1, 0.4419738632922878], [3, 2, 0.45068746416358724], [3, 3, 1.0], [3, 4, 0.6678745095652185], [4, 0, 0.9382086683784459], [4, 1, 0.709260368207342], [4, 2, 0.7266822817524653], [4, 3, 0.6678745095652187], [4, 4, 1.0]]

data = data.map(function (item) {
    return [item[1], item[0], item[2] || '-'];
});

option = {
    tooltip: {
        position: 'top'
    },
    animation: false,
    grid: {
        height: '50%',
        top: '10%'
    },
    xAxis: {
        type: 'category',
        data: hours,
        splitArea: {
            show: true
        }
    },
    yAxis: {
        type: 'category',
        data: days,
        splitArea: {
            show: true
        }
    },
    visualMap: {
        min: 0,
        max: 1,
        calculable: true,
        orient: 'horizontal',
        left: 'center',
        bottom: '15%'
    },
    series: [{
        name: 'Punch Card',
        type: 'heatmap',
        data: data,
        label: {
            show: true
        },
        emphasis: {
            itemStyle: {
                shadowBlur: 1,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    }]
};