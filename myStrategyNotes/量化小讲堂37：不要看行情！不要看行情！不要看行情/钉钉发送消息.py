"""
本程序中的函数send_dingding_msg，可以使用钉钉发送消息。

robot_id是钉钉群的id，可以网上搜索一下，如何查找这个id

程序作者：邢不行，微信：xingbuxing0807
"""

import requests, datetime, json

# =====钉钉发送消息
def send_dingding_msg(content, robot_id='这里填上机器人id'):

    try:
        msg = {
            "msgtype": "text",
            "text": {"content":  content + '\n' + datetime.datetime.now().strftime("%m-%d %H:%M:%S")}}

        Headers = {"Content-Type": "application/json ;charset=utf-8 "}
        url = 'https://oapi.dingtalk.com/robot/send?access_token=' + robot_id
        body = json.dumps(msg)
        requests.post(url, data=body, headers=Headers)
    except Exception as err:
        print('钉钉发送失败', err)


send_dingding_msg('这里填上要发送的内容')
