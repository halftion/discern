import { Chart } from '@antv/g2';
import React from 'react'

const data = [
  { type: '路由/网关', value: 340, cat: '硬件' },
  { type: '家用设备', value: 20760, cat: '硬件' },
  { type: '工控设备', value: 28750, cat: '硬件' },
  { type: 'web', value: 14870, cat: '组件' },
  { type: 'ssh', value: 37098, cat: '组件' },
  { type: 'cdn', value: 49099, cat: '组件' },
];




class Typechart extends React.Component{
    componentDidMount(){
        const chart = new Chart({
            container: 'typechart',
            autoFit: true,
            width: 350,
            height: 250,
            padding: [20, 0, 50, 100],
          });
        chart.data(data);
        chart.scale({
            value: {
                max: 55000,
                min: 0,
                alias: '数量',
            },
        });
        chart.axis('type', {
            tickLine: null,
            line: null,
        });
        chart.axis('value', {
            label: null,
            title: {
                offset: 30,
                style: {
                fontWeight: 300,
                },
            },
            grid: null,
        });
        chart.legend(false);
        chart.coordinate('rect').transpose();
        chart
        .interval()
        .position('type*value')
        .color('cat', ['#face1d', '#2194ff'])
        .size(26)
        .label('value', {
            style: {
            fill: '#8d8d8d',
            },
            offset: 10,
            content: (originData) => {
            return (originData.value + '').replace(/(\d)(?=(?:\d{3})+$)/g, '$1,');
            },
        });

        chart.annotation().text({
            top: true,
            position: ['ssh', 'min'],
            content: '组件',
            style: {
                fill: '#c0c0c0',
                fontSize: 12,
                fontWeight: '300',
                textAlign: 'center',
            },
            offsetX: -70,
            rotate: Math.PI * -0.5
        });
        chart.annotation().text({
            top: true,
            position: ['家用设备', 'min'],
            content: '硬件',
            style: {
                fill: '#c0c0c0',
                fontSize: 12,
                fontWeight: '300',
                textAlign: 'center',
            },
            offsetX: -70,
            rotate: Math.PI * -0.5
            });
            chart.annotation().line({
            start: ['-20%', '50%'],
            end: ['100%', '50%'],
            style: {
                stroke: '#c0c0c0',
                lineDash: [2, 2],
            },
        });
        
        chart.interaction('element-active');
        chart.render();
    }
    
    render(){
        return(
        <div id="typechart">

        </div>);
    }
}

export default Typechart;