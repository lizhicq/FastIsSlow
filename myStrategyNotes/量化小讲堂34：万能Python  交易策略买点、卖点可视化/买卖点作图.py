"""
邢不行量化小讲堂系列文章配套代码
文章标题：万能Python | 交易策略买点、卖点可视化
文章链接：https://mp.weixin.qq.com/s/KrwoYvRjbZpqbWu7_xivlw
作者：邢不行
微信号：xingbuxing0807
"""


import matplotlib.pyplot as plt  # 导入这个画图工具
dfplot = df.copy()  # 用复制的方法创建一个df，很好的习惯

# 把 candle_begin_time 设置为index，这样画出来的图横轴才会是时间
dfplot.index = dfplot['candle_begin_time']

# 画出收盘价、中轨线的折线图
dfplot[['close', 'median']].plot()

# 画出布林线上下轨形成的带状区域，颜色为蓝色，alpha 为透明度
plt.fill_between(dfplot.index, dfplot['upper'], dfplot['lower'], color='b', alpha=0.2)

# 画出多头开仓点，即 signal 为1的点，形状是^（向上的三角形），颜色是红色，符号的大小是20
plt.plot(dfplot[dfplot['signal'] == 1]['close'], '^', color='red', markersize=20)

# 画出多头开仓点，即 signal 为0的点，形状是o（圆形），颜色是绿色，符号的大小是15
plt.plot(dfplot[dfplot['signal'] == 0]['close'], 'o', color='green', markersize=15)

# 画出多头开仓点，即 signal 为-1的点，形状是v（向下的三角形），颜色是红色，符号的大小是20
plt.plot(dfplot[dfplot['signal'] == -1]['close'], 'v', color='red', markersize=20)

# 展示图片
plt.show()
