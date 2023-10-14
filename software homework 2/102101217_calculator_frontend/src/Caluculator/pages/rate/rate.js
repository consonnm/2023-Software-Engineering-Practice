// pages/rate/rate.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    depositRate: [0, 0, 0, 0, 0, 0, 0],
    loanRate: [0, 0, 0, 0, 0,0,0],
    
    loanMoney: "",
    loanRateTime: "",
    loanRateResult: "",
    depositMoney: "",
    depositRateTime: "",
    depositRateResult: "",
  },
  onLoad: function () {
    wx.request({
      url: 'http://localhost:5000/queryRate',
      method: 'POST',
      data: {
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
        var i= 0
        while(i<7){
          this.data.depositRate[i]=res.data.rate[i]
          i++
        }
        this.setData({depositRate: this.data.depositRate })
        while(i<12){
          this.data.loanRate[i-7]=res.data.rate[i]
          i++
        }
        this.setData({loanRate: this.data.loanRate })
        console.log('请求成功', res.data.result);
      },
      fail: function (error) {
        // 请求失败时的回调函数
        console.error('请求失败', error);
      }
    });

  },

  currentDeposit() {
    wx.request({
      url: 'http://localhost:5000/calculateRate',
      method: 'POST',
      data: {
        flag: 0,
        amount: this.data.depositMoney,
        time: this.data.depositRateTime,
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
        this.data.depositRateResult=res.data.result,
        this.setData({depositRateResult: this.data.depositRateResult })
        
      },
      fail: function (error) {
        // 请求失败时的回调函数
        console.error('请求失败', error);
      }
    });
    
  },
  fixDeposit() {
    wx.request({
      url: 'http://localhost:5000/calculateRate',
      method: 'POST',
      data: {
        flag: 1,
        amount: this.data.depositMoney,
        time: this.data.depositRateTime,
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
        this.data.depositRateResult=res.data.result,
        this.setData({depositRateResult: this.data.depositRateResult })
        
      },
      fail: function (error) {
        // 请求失败时的回调函数
        console.error('请求失败', error);
      }
    });
    
  },
  loanCalculate() {
    wx.request({
      url: 'http://localhost:5000/calculateRate',
      method: 'POST',
      data: {
        flag: 2,
        amount: this.data.loanMoney,
        time: this.data.loanRateTime,
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
        this.data.loanRateResult=res.data.result,
        this.setData({loanRateResult: this.data.loanRateResult })
        
      },
      fail: function (error) {
        // 请求失败时的回调函数
        console.error('请求失败', error);
      }
    });
    
  },
  
})