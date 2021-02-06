import React from 'react'
import { withRouter, Switch, Redirect } from 'react-router-dom'

import LoadableComponent from '../../utils/LoadableComponent'
import PrivateRoute from '../../components/PrivateRoute'

const Homepage = LoadableComponent(()=>import('../../routes/Homepage/index'))
const Home = LoadableComponent(()=>import('../../routes/Home/index'))
const Controlboard = LoadableComponent(()=>import('../../routes/Controlboard/index'))
const Searchpage = LoadableComponent(()=>import('../../routes/Searchpage/index'))
const Detail = LoadableComponent(()=>import('../../routes/Detail/index'))

class Index extends React.Component{
  state = {
    collapsed: false
  }

  toggle = () => {
    // console.log(this)  状态提升后，到底是谁调用的它
    this.setState({
      collapsed: !this.state.collapsed
    })
  }
  render() {
    // 设置Sider的minHeight可以使左右自适应对齐
    return (
      <div>
        <Switch>
          <PrivateRoute exact path='/homepage' component={Homepage}/>
          <PrivateRoute exact path='/controlboard' component={Controlboard}/>
          <PrivateRoute exact path='/search' component={Searchpage}/>
          <PrivateRoute exact path='/detail' component={Detail}/>
          <PrivateRoute exact path='/home' component={Home}/>
          <Redirect exact from='/' to='/homepage'/>
        </Switch>
      </div>
    );
  }
}
export default Index