## discern客户端

### 技术栈

 - react
 - antd
 - antv
 - react-router
 - mobx
 - canvas
 - ES6
 - cookie
 - react-admin

参考了其他优秀的插件，比如[动态打字效果](https://blog.csdn.net/qq_37860930/article/details/80859473)、背景粒子效果、[shuffle（洗牌）](https://github.com/Vestride/Shuffle)，[全屏插件](https://github.com/sindresorhus/screenfull.js)等，自己对有些插件封装成类使用

所有路由都需要登录才可进入，自己封装了PrivateRoute组件来实现路由认证，登录信息保存在cookie中，原本是保存在store中，但是刷新页面后登录状态丢失，所以就保存在cookie中
登录背景图太大，使用了[TinyPNG](https://tinypng.com/)进行压缩，并编写了一个loading效果
<br/>

### 项目目录结构

<img src="https://github.com/zhangZhiHao1996/image-store/blob/master/react-admin-master/111.png?raw=true"/>
<br />
assets----存储静态图片资源和共用icon图标<br/>
components----存储共用组件<br/>
routes----业务页面入口和常用模板<br/> 
store----状态管理<br/>
utils----工具函数<br/>
<br/>

### 项目截图

![主页.png](https://i.loli.net/2021/02/05/pvnyWD1TirYzs72.png)
![监控台.png](https://i.loli.net/2021/02/05/V61XmiA5Dzdj4Ma.png)
![识别结果.png](https://i.loli.net/2021/02/05/q4EYXoDvyuhISgc.png)
![设备详情.png](https://i.loli.net/2021/02/05/Hncmtw1gFYxrAUp.png)

### 问题

因为项目回滚了一个版本，数据域还存在一些问题(厂商显示国家)，待优化
