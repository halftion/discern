import React from 'react'
import {Link} from 'react-router-dom'
import {Menu,Layout,Row,Col,Icon,Statistic,Card} from 'antd';
import Worldmap from './world.js'
import Wordcloud from './wordcloud.js'
import Typechart from './typechart.js'
import Panel from './panel.js'
import Portchart from './portchart.js'
import './style.css'

const { Header, Content, Footer } = Layout;


class Controlboard extends React.Component{
    
  render() {
    // 设置Sider的minHeight可以使左右自适应对齐
    return (
      <div>
        <Layout>
          <Header style={styles.menu}>
            <Menu style={styles.menu} mode="horizontal">
              <Menu.Item key="/homepage">
                <Link to="/homepage">
                  首页
                </Link>
              </Menu.Item>
              <Menu.Item key='/controlboard'>
                <Link to="/controlboard">
                  监控台
                </Link>
              </Menu.Item>
              <Menu.Item key="/search">
                  <Link to="/search">
                    搜索
                  </Link>
                </Menu.Item>
            </Menu>
          </Header>
          <Content style={styles.content}>
            <Row style={{height:'100%'}}>
              <Col span={6}>
                <Panel />
                <Card title='端口' style={{border:'none'}}>
                  <Portchart />
                </Card>
                
              </Col>
              <Col span={12} style={styles.mapbox}>
                  <div className='iconbox'>
                    <Icon type='database' style={{fontSize:50,display:'inline-block',paddingRight:20}} />
                    <Statistic style={{display:'inline-block'}} title="设备" value={112893} />
                  </div>
                  <div className='iconbox'>
                    <Icon type='appstore' style={{fontSize:50,display:'inline-block',paddingRight:20}} />
                    <Statistic style={{display:'inline-block'}} title="组件" value={2893} />
                  </div>
                  <Card title="设备分布" style={{border:'none'}}>
                    <Worldmap />
                  </Card>   
              </Col> 
              <Col span={6}>
                
                <Typechart />
                <Card title="厂商" style={{border:'none'}}>
                    <Wordcloud />
                </Card>
              </Col>
            </Row>
          </Content>
          <Footer style={styles.foo}>descern ©2021 Created by halftion.cn</Footer>
        </Layout>
      </div>
    );
  }
}

const styles = {
  menu:{
    padding:0,
    width:'100%',
    height:48,
    textAlign:'center',
  },
  content:{
    height:`calc(100vh - 98px)`,
    background:'#fff',
  },
  foo:{
    padding:0,
    background:"#fff",
    height:50,
    lineHeight:'50px',
    textAlign:'center',
    verticalAlign:'middle',
  },
  mapbox:{
    height:'100%',
  }
}

export default Controlboard