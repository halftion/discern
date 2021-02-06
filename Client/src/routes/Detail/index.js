import React from 'react'
import {Link} from 'react-router-dom'
import {Menu,Layout,Input,Card,message,Spin,Table} from 'antd';
import $ from 'jquery';
import './style.css'


const { Header, Content, Footer } = Layout;
const { Search } = Input;

class Detail extends React.Component{
    constructor(props){
        super(props);
        this.state = {
          ip:'',
          products:[],
          cve:[],
          cvedetails:[],
          loading:true,
          loadingdetail:true,
          columns:[
            { title: 'cve_id', dataIndex: 'cve_id', key: 'cve_id' },
            { title: 'cwe_id', dataIndex: 'cwe_id', key: 'cwe_id' },
            { title: 'exp', dataIndex: 'exp', key: 'exp' },
            { title: '漏洞类型', dataIndex: 'vulneravility_type', key: 'vulneravility_type' },
            { title: '评分', dataIndex: 'score', key: 'score' },
            { title: '授权访问等级', dataIndex: 'gainedaccess_level', key: 'gainedaccess_level' },
            { title: '访问方式', dataIndex: 'access', key: 'access' },
            { title: '复杂度', dataIndex: 'complexity', key: 'complexity' },
            { title: '认证', dataIndex: 'authentication', key: 'authentication' },
            {
                title: '操作',
                dataIndex: 'cve_url',
                key: 'cve_url',
                render: (text) => <a href={'https://www.cvedetails.com' + text}>更多</a>,
              },
          ]
        }
      }
      componentDidMount(){
        if(this.props.location.state === undefined){
          message.warning("缺少查询参数",2);
          this.props.history.push("/homepage");
        }else{
          console.log(this.props.location.state.ip)
          this.setState({
              ip:this.props.location.state.ip
          })
          this.getData(this.props.location.state.ip)
        }
      }

    renderCPE = () =>{
        const { products } = this.state;
        let cpes = [];
        if(products[0] !== undefined){
            for(let i = 0;i < products.length;++i){
                if(products[i].os !== undefined){
                    if(products[i].os[0] !== undefined){
                        for(let j = 0;j < products[i].os.length;++j){
                            if(products[i].os[j] !== undefined){
                                if(products[i].os[j].cpe !== undefined){
                                    if(products[i].os[j].cpe[0] !== undefined){
                                        for(let k = 0;k < products[i].os[j].cpe.length;++k){
                                            cpes.push(
                                                <span>
                                                    <br />
                                                    {products[i].os[j].cpe[k]}
                                                </span>
                                            );
                                        }

                                    }
                                }
                            }
                            
                        }
                    }  
                }
            }
        }
        return cpes;
    }

    renderNames = () =>{
        const { products } = this.state;
        let names = [];
        if(products[0] !== undefined){
            for(let i = 0;i < products.length;++i){
                if(products[i].name !== undefined){
                    names.push(
                        <span><br/>{products[i].name}</span>
                    );
                }
                
            }
        }
        return names;
    }

    renderTypes = () =>{
        const { products } = this.state;
        let types = [];
        if(products[0] !== undefined){
            for(let i = 0;i < products.length;++i){
                if(products[i].type !== undefined){
                    types.push(
                        <span><br/>{products[i].type}</span>
                    )
                }
                
            }
        }
        return types
    }

    renderVendor = () =>{
        const { products } = this.state;
        let vendor = '';
        if(products[0] !== undefined){ 
            if(products[0].vendor !== undefined){
                vendor = <span>{products[0].vendor}</span>;
            }    
        }
        return vendor
    }

    appendCVE = () =>{
        const { products } = this.state;
        let cves = [];
        if(products[0] !== undefined){
            for(let i = 0;i < products.length;++i){
                if(products[i].cve !== undefined){
                    for(let j = 0;j < products[i].cve.length;++j){
                        cves.push(products[i].cve[j]);
                    }
                }   
            }
        }
        this.setState({
            cve:cves
        })
    }

    getData = (ip) =>{
        let json = {
            "ip":ip
        }
        console.log(json)
        $.ajax({
            url: `http://127.0.0.1:5000/detail`,
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
                      products:productlist
                    });
                    this.appendCVE()
                    let cves = this.state.cve
                    this.getCVEDetail(cves);
                }else {
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

    getCVEDetail = (cves) =>{
        let json = {
            "cve":cves
        }
        console.log(json)
        $.ajax({
            url: `http://127.0.0.1:5000/vul_detail`,
            type : "POST",	//请求类型  post|get
            dataType: "json",    //返回数据的 类型 text|json|html--
            contentType: "application/json;charset=utf-8",
            data:  JSON.stringify(json),
            success : (data) => {
                if(data.code === 200){
                    let cvelist = data.data;
                    this.setState({
                      cvedetails:cvelist,
                      loadingdetail:false,
                    });
                }else {
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
    
    onSearch = (value) =>{
        this.props.history.push({pathname:'/search', state:{ip:value}})
      };

    render(){
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
            <Content style={styles.content}>
              <Layout>
                <Header style={{verticalAlign:'middle',background:'#fff'}}>
                  <Search placeholder="输入查询的起止ip" 
                    onSearch={this.onSearch}
                    className='searchs' 
                    enterButton />
                </Header>
               
                <Content style={{width:'80%',height:'100%',margin:'0 auto',overflow:'scroll '}}>
                    <Spin size='large' spinning={this.state.loading}>
                        <Card  title={this.state.ip} style={styles.card}>
                            <p>类型: {this.renderTypes()}</p>
                            <p>名称: {this.renderNames()}</p>
                            <p>厂商：{this.renderVendor()}</p>
                            <p>位置：China</p>
                            <p>设备信息：{this.renderCPE()}</p>
                        </Card>
                  </Spin>
                  <Table
                    columns={this.state.columns}
                    expandedRowRender={record => <p style={{ margin: 0 }}>{record.description}</p>}
                    loading = {this.state.loadingdetail}
                    dataSource={this.state.cvedetails}
                    />
                </Content>
              </Layout>
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
  
  export default Detail