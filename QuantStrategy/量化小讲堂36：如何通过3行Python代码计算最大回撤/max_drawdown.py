"""
邢不行量化小讲堂系列文章配套代码
文章标题：如何通过3行Python代码计算最大回撤
文章链接：https://mp.weixin.qq.com/s/Dwt4lkKR_PEnWRprLlvPVw
作者：邢不行
微信号：xingbuxing0807
"""


import pandas as pd

pd.set_option('expand_frame_repr', False)  # 当列太多时不换行
pd.set_option('display.max_rows', 1000)

all_data = pd.read_csv(r'E:\timing_strategy\data\output_data\equity_curve.csv')
print(all_data)


equity = all_data[['candle_begin_time', 'equity_curve']].copy()
equity['candle_begin_time'] = pd.to_datetime(equity['candle_begin_time'])



# 使用最大回撤衡量风险
# 最大回撤：从某一个高点，到之后的某个低点，之间最大的下跌幅度。实际意义：在最坏的情况下，会亏多少钱

# 计算当日之前的资金曲线最高点
equity['max2here'] = equity['equity_curve'].expanding().max()

# 计算历史最高值到当日的剩余量，drawdown
equity['dd2here'] = equity['equity_curve'] / equity['max2here']

# 计算回撤完之后剩余量的最小值（也就是最大回撤的剩余量），以及最大回撤的结束时间
end_date, remains= tuple(equity.sort_values(by=['dd2here']).iloc[0]
                                [['candle_begin_time', 'dd2here']])

# 计算最大回撤开始时间
start_date = equity[equity['candle_begin_time'] <= end_date]\
            .sort_values(by='equity_curve', ascending=False)\
            .iloc[0]['candle_begin_time']

print('最大回撤 (%):', round((1-remains) * 100, 2))
print('最大回撤开始时间：', start_date)
print('最大回撤结束时间：', end_date)




