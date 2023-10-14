// pages/Calculator/Calculator.js

Page({
  onLoad() {
    wx.setNavigationBarTitle({
      title: 'consonnm\' 科学计算器',
    })
  },
  /**
   * 页面的初始数据
   */
  data: {
    showChose: 0,
    keysdata: [{
        name: 'asin',
        index: '001',
        type: 1
      },
      {
        name: 'acos',
        index: '002',
        type: 1
      },
      {
        name: 'atan',
        index: '003',
        type: 1
      },
      {
        name: 'sqrt',
        index: '004',
        type: 1
      },
      {
        name: 'AC',
        index: '005',
        type: 3
      },

      {
        name: 'C',
        index: '006',
        type: 3
      },
      {
        name: 'Back',
        index: '007',
        type: 2
      },
      {
        name: '%',
        index: '008',
        type: 0
      },
      {
        name: '÷',
        index: '009',
        type: 0
      },
      {
        name: '!',
        index: '010',
        type: 0
      },

      {
        name: '7',
        index: '011',
        type: 0
      },
      {
        name: '8',
        index: '012',
        type: 0
      },
      {
        name: '9',
        index: '013',
        type: 0
      },
      {
        name: '×',
        index: '014',
        type: 0
      },
      {
        name: 'sin',
        index: '015',
        type: 1
      },

      {
        name: '4',
        index: '016',
        type: 0
      },
      {
        name: '5',
        index: '017',
        type: 0
      },
      {
        name: '6',
        index: '018',
        type: 0
      },
      {
        name: '-',
        index: '019',
        type: 0
      },
      {
        name: 'cos',
        index: '020',
        type: 1
      },

      {
        name: '1',
        index: '021',
        type: 0
      },
      {
        name: '2',
        index: '022',
        type: 0
      },
      {
        name: '3',
        index: '023',
        type: 0
      },
      {
        name: '=',
        index: '024',
        type: 5
      },
      {
        name: '.',
        index: '025',
        type: 4
      },

      {
        name: 'π',
        index: '026',
        type: 0
      },
      {
        name: '0',
        index: '027',
        type: 0
      },
      {
        name: 'sin',
        index: '028',
        type: 1
      },
      {
        name: '+',
        index: '029',
        type: 0
      },
      {
        name: 'ln',
        index: '030',
        type: 1
      },

      {
        name: '(',
        index: '031',
        type: 0
      },
      {
        name: ')',
        index: '032',
        type: 0
      },
      {
        name: '^',
        index: '033',
        type: 0
      },
      {
        name: 'e',
        index: '034',
        type: 0
      },
      {
        name: 'log',
        index: '035',
        type: 1
      }

    ],
    resultNum: '', //结果
    expression: '', //计算表达式
    sidebarVisible: 0, // 用于控制侧边栏是否可见的变量
    list: [],
  },

  // 键盘点击事件
  keyClick(event) {
    var n = event.target.dataset.num;
    if(this.data.list.length>=1&&this.data.list[this.data.list.length - 1] == '='){
      this.data.expression=this.data.resultNum;
      this.data.resultNum="";
      this.setData({
        expression: this.data.expression
      })
      this.setData({resultNum: this.data.resultNum })
      this.data.list=[];
      this.data.list.push(this.data.expression);

    }
    if (n.type == 0) { //普通数字
      this.data.expression += n.name;
      this.data.list.push(n.name);
    } else if (n.type == 1) { //科学函数
      this.data.expression += n.name + '(';
      this.data.list.push(n.name + '(');
    } else if (n.type == 2) { //退格
      this.Backspace();
    } else if (n.type == 3) { //清零
      this.clear();
      this.data.resultNum="";
      this.setData({resultNum: this.data.resultNum })
    } else if (n.type == 4) { //点
      if (this.data.list[this.data.list.length - 1] != '.') {
        this.data.expression += n.name;
        this.list.push(n.name);
      }
    } else if (n.type == 5) {
      wx.request({
        url: 'http://localhost:5000/calculateNum',
        method: 'POST',
        data: {
          expression: this.data.expression,
        },
        header: {
          'content-type': 'application/json'
        },
        success: (res) => {
          // 请求成功时的回调函数
          console.log('请求成功', res.data.result);
          this.data.resultNum = res.data.result;
          this.setData({resultNum: this.data.resultNum })
          this.data.list.push("=");
        },
        fail: function (error) {
          // 请求失败时的回调函数
          console.error('请求失败', error);
        }
      });
    }
    this.setData({
      expression: this.data.expression
    })
  },
  Backspace() {
    if (this.data.list.length != 0) {
      var size = this.data.list[this.data.list.length - 1].length;
      this.data.list.pop();
      this.data.expression = this.data.expression.slice(0, this.data.expression.length - size);
    }
  },
  clear() {
    this.data.list = [];
    this.data.expression = "";
  },

  showSidebar() {
    this.setData({
      sidebarVisible: !this.data.sidebarVisible
    });
  },
  show() {
    this.setData({
      showChose: !this.data.showChose
    });
  },

})