// pages/history/history.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    historyRecords: []
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad(options) {
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

 
})