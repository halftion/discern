import { Chart } from '@antv/g2';
import React from 'react';

const data = [
  { genre: '22', sold: 275 },
  { genre: '80', sold: 115 },
  { genre: '443', sold: 120 },
  { genre: '20', sold: 350 },
  { genre: '21', sold: 150 },
];

class Portchart extends React.Component{
    componentDidMount(){
        // Step 1: 创建 Chart 对象
        const chart = new Chart({
            container: 'portchart', // 指定图表容器 ID
            width:350,
            height: 300, // 指定图表高度
        });
        // Step 2: 载入数据源
        chart.data(data);
        // Step 3: 创建图形语法，绘制柱状图
        chart.interval().position('genre*sold');
        // Step 4: 渲染图表
        chart.render();
    }
    render(){
        return(
            <div id='portchart' style={{paddingTop:20}} />
        )
    }
}

export default Portchart;