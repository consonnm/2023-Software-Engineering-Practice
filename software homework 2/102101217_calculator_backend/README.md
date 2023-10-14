**目录**







------



### 项目源码地址



### Calculator

| 这个作业属于哪个课程 | https://bbs.csdn.net/forums/ssynkqtd-05 |
| -------------------- | --------------------------------------- |
| 这个作业要求在哪里   | https://bbs.csdn.net/topics/617377308   |
| 这个作业的目标       | 继续完善计算器并且实现前后端分离        |

### 1. PSP表格

| PSP                                     | Personal Software Process Stages        | 预估耗时（分钟） | 实际耗时（分钟） |
| --------------------------------------- | --------------------------------------- | ---------------- | ---------------- |
| Planning                                | 计划                                    | 10               | 15               |
| • Estimate                              | • 估计这个任务需要多少时间              | 20               | 15               |
| Development                             | 开发                                    | 580              | 625              |
| • Analysis                              | • 需求分析 (包括学习新技术）            | 60               | 60               |
| • Design Spec                           | • 生成设计文档                          | 70               | 50               |
| • Design Review                         | • 设计复审                              | 10               | 20               |
| • Coding Standard                       | • 代码规范 (为目前的开发制定合适的规范) | 10               | 15               |
| • Design                                | • 具体设计                              | 30               | 50               |
| • Coding                                | • 具体编码                              | 240              | 300              |
| • Code Review                           | • 代码复审                              | 60               | 30               |
| • Test                                  | • 测试（自我测试，修改代码，提交修改）  | 90               | 90               |
| Reporting                               | 报告                                    | 120              | 100              |
| • Test Repor                            | • 测试报告                              | 20               | 20               |
| • Size Measurement                      | • 计算工作量                            | 10               | 10               |
| • Postmortem & Process Improvement Plan | • 事后总结, 并提出过程改进计划          | 80               | 60               |
|                                         | 合计                                    | 700              | 750              |

### 2. 设计实现过程

功能结构图

```
        计算器  
├── 科学计算器  
│   ├── 表达式计算  
│   ├── 查询历史记录  
│   └── 可视化界面  
├── 利率计算器  
│   ├── 利率计算  
│   ├── 修改利率  
│   └── 可视化界面  
└── 
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

1.前端 工具：微信开发者工具
 2.后端 使用sqlalchemy和pmysql连接和操作数据库  工具：PyCharm
 3.数据库 mysql
 4.数据库可视化工具 sqlyog

### 3. 成品展示

#####     1.科学计算功能+历史记录查询

​         

![img](https://img-blog.csdnimg.cn/5fabf636f7dd4ea69e1eb6f83f43a83a.gif)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

#####     2.利率计算+利率修改

![img](https://img-blog.csdnimg.cn/27920b4f6f8e4c3dbb8e5165d4b8d73d.gif)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

​         

#####     3.后端数据库（用户id功能待完善）

​           ![img](https://img-blog.csdnimg.cn/1f03d69fbb274277b6751a4bd11b312c.png)![img](https://img-blog.csdnimg.cn/d7ba60f9a95f4011b1e9d777ac91179e.png)![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

![img](https://img-blog.csdnimg.cn/b2aafa4f800a4bd88d59c21e677f5cd1.png)

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

### 4. 代码说明

#####     1.前端（微信小程序）

​    请求后端接口示例

```python
 wx.request({
      url: 'http://localhost:5000/queryHistory',
      method: 'POST',
      data: {
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
        // 请求成功时的回调函数
        console.log('请求成功', res.data.result);
        this.data.historyRecords = res.data.history;
        this.setData({historyRecords: this.data.historyRecords })
      },
      fail: function (error) {
        // 请求失败时的回调函数
        console.error('请求失败', error);
      }
    });
  },
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

​     样式设计示例

```python
.calculateScreen {
  position: relative;
  width: 100%;
  height: 30vh;
  background-color: #eee;
  z-index: 99;
  box-shadow: 6rpx 6rpx 12px 6rpx rgba(211, 209, 209, 0.3);
  overflow: hidden;
  backdrop-filter: blur(20rpx);
}
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

​    使用vant 2组件库

```python
"usingComponents": {
    "van-button": "@vant/weapp/button/index",
    "van-sidebar": "@vant/weapp/sidebar/index",
    "van-sidebar-item": "@vant/weapp/sidebar-item/index",
    "van-popup": "@vant/weapp/popup/index",
    "van-divider": "@vant/weapp/divider/index",
    "van-icon": "@vant/weapp/icon/index",
    "van-field": "@vant/weapp/field/index",
    "van-cell": "@vant/weapp/cell/index",
    "van-cell-group": "@vant/weapp/cell-group/index"
  }
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

#####     2.后端（python）

​    科学计算

```python
@app.route('/calculateNum', methods=['POST'])
def calculateNum():
    data = request.get_json()
    expression = data['expression']
    re = cal(expression)
    data = {
        'result': re
    }
    re = expression + " = " + str(re)
    new_expression = Expression(content=re)
    session.add(new_expression)
    session.commit()
    return jsonify(data)
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

​     计算历史记录查询

```python
@app.route('/queryHistory', methods=['POST'])
def queryHistory():
    results = session.query(Expression) \
        .order_by(Expression.id.desc()) \
        .limit(10) \
        .all()
    history = []
    i = 0
    while i < len(results):
        history.append(results[i].content)
        i += 1
    data = {
        'history': history
    }
    return jsonify(data)
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

​    利率修改

```python
@app.route('/updateRate', methods=['POST'])
def updateRate():
    data = request.get_json()
    rate = data['rate']
    i = 1
    print(rate)
    while i <= 7:
        rate[i-1]=float(rate[i-1])
        session.query(depositRate).filter(depositRate.id == i).update(
            {depositRate.rate: rate[i-1]})
        session.commit()
        i += 1
    i = 1
    while i <= 5:
        rate[i+6] = float(rate[i+6])
        rate[i+6] = float(rate[i+6])
        session.query(loanRate).filter(loanRate.id == i).update(
            {loanRate.rate: rate[i+6]})
        session.commit()
        i += 1
    return "200"
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

利率查询

```python
@app.route('/queryRate', methods=['POST'])
def queryRate():
    data = request.get_json()
    rate = []
    re = session.query(depositRate).all()
    i = 0
    while i < 7:
        rate.append(re[i].rate)
        i += 1
    re = session.query(loanRate).all()
    i = 0
    while i < 5:
        rate.append(re[i].rate)
        i += 1
    print(rate)
    data = {
        'rate': rate
    }
    return jsonify(data)
```

![点击并拖拽以移动](data:image/gif;base64,R0lGODlhAQABAPABAP///wAAACH5BAEKAAAALAAAAAABAAEAAAICRAEAOw==)

##   4.心路历程与收获

第一次完整的完成从前端到后端的开发，进一步提高了对前后端对接的理解，对接流程和对接细节也更加清晰！ 

### 