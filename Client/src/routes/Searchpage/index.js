import React from 'react'
import {Link} from 'react-router-dom'
import {Menu,Layout,Input,Card,message,Spin} from 'antd';
import $ from 'jquery';
import './style.css'

const { Header, Content, Footer } = Layout;
const { Search } = Input;

class Searchpage extends React.Component{
  constructor(props){
    super(props);
    this.state = {
      ip:'',
      products:[],
      loading:true,
    }
  }
  componentDidMount(){
    if(this.props.location.state === undefined){
      message.warning("缺少查询参数",2);
      this.props.history.push("/homepage");
    }else{
      console.log(this.props.location.state.ip)
      this.getdata(this.props.location.state.ip)
    }
  }

  getdata = (ip) =>{
    let json = {
        "ip":ip
    }
    console.log(json)
    $.ajax({
        url: `http://127.0.0.1:5000/scan`,
        type : "POST",	//请求类型  post|get
        // data : "key=value&key1=value2",	//后台用 request.getParameter("key");
        dataType: "json",    //返回数据的 类型 text|json|html--
        contentType: "application/json;charset=utf-8",
        data:  JSON.stringify(json),
        success : (data) => {
            if(data.code === 200){
                let productlist = data.data;
                this.setState({
                  loading:false,
                  products:productlist,
                });
            }else if(data.code === 300){
              message.warning("请输入查询ip",2);
              this.props.history.push("/homepage");
            }
            else {
              message.warning("获取数据失败，请联系管理员",2);
              this.props.history.push("/homepage");
            }
        },
        error:() => {
          message.error("获取数据失败，请检查网络连接",2);
          this.props.history.push("/homepage");
      }
    });
  }

  renderCard = () => {
    const { products,loading } = this.state;
    let cards = [];
    if(loading === false){
      
      if( products[0] !== undefined){
        for(let i = 0;i < products.length;++i){
          cards.push(
            <Card title={products[i].name} style={styles.card} extra={<Link to={{pathname:"/detail",state:{ip:products[i].ip}}}>更多</Link>}>
              <p>ip: {products[i].ip}</p>
              <p>类型: {products[i].type}</p>
              <p>厂商：{products[i].vendor}</p>
              <p>位置：China</p>
            </Card>
          )
          
        }
      }
      
    }
    return cards;
    
  }

  onSearch = (value) =>{
    this.getdata(value)
  }

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
                <Menu.Item key="/controlboard">
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
            <Spin size='large' spinning={this.state.loading}>
              <Content style={styles.content}>
                <Layout>
                  <Header style={{verticalAlign:'middle',background:'#fff'}}>
                    <Search placeholder="输入查询的ip,多个ip使用逗号分隔" 
                      onSearch={this.onSearch}
                      className='searchs' 
                      enterButton />
                  </Header>
                  
                  <Content style={{width:'80%',height:'100%',margin:'0 auto',overflow:'scroll '}}>
                    {this.renderCard()}
                    {/* <Card title='120.78.154.43' style={styles.card} extra={<Link to="/detail">更多</Link>}>
                      <p>类型: Hardware</p>
                      <p>名称: Cisco870routeror2960switch(IOS12.2-12.4)</p>
                      <p>厂商：Cisco</p>
                      <p>位置：China</p>
                      <p>设备信息：cpe: /h: cisco: 870_router','cpe: /o: cisco: ios: 12</p>
                    </Card>
                    <Card title='120.78.154.43' style={styles.card} extra={<Link to="/detail">更多</Link>}>
                      <p>类型: Hardware</p>
                      <p>名称: Cisco870routeror2960switch(IOS12.2-12.4)</p>
                      <p>厂商：Cisco</p>
                      <p>位置：China</p>
                      <p>设备信息：cpe: /h: cisco: 870_router','cpe: /o: cisco: ios: 12</p>
                    </Card>
                    <Card title='120.78.154.43' style={styles.card} extra={<Link to="/detail">更多</Link>}>
                      <p>类型: Hardware</p>
                      <p>名称: Cisco870routeror2960switch(IOS12.2-12.4)</p>
                      <p>厂商：Cisco</p>
                      <p>位置：China</p>
                      <p>设备信息：cpe: /h: cisco: 870_router,cpe: /o: cisco: ios: 12</p>
                    </Card> */}
                  </Content>
                </Layout>
              </Content>
            </Spin>
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
      minHeight:`calc(100vh - 98px)`,
      background:'#fff',
      textAlign:'center',
      background:'#eee'
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
    },
    card:{
      marginTop:10,
      textAlign:'left',
    }
  }
  
  export default Searchpage