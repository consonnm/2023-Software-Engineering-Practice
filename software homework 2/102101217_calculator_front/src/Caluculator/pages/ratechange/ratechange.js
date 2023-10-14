// pages/ratechange/ratechange.js
Page({
  data: {
    rate0:"",
    rate1:"",
    rate2:"",
    rate3:"",
    rate4:"",
    rate5:"",
    rate6:"",
    rate7:"",
    rate8:"",
    rate9:"",
    rate10:"",
    rate11:"",
  },

  onChange(event) {
    // event.detail 为当前输入的值
    console.log(event.detail);
  },
  updateRate() {
    wx.request({
      url: 'http://localhost:5000/updateRate',
      method: 'POST',
      data: {
        rate: [this.data.rate0,this.data.rate1,this.data.rate2,this.data.rate3,this.data.rate4,this.data.rate5,this.data.rate6,this.data.rate7,this.data.rate8,this.data.rate9,this.data.rate10,this.data.rate11]
      },
      header: {
        'content-type': 'application/json'
      },
      success: (res) => {
      },
      fail: function (error) {
        // 请求失败时的回调函数
        console.error('请求失败', error);
      }
    });
    wx.navigateTo({
      url: '/pages/rate/rate'
    });
  },
})