from flask import Flask, render_template, request, jsonify
import re  # 导入正则表达式模块

# 创建 Flask 应用
app = Flask(__name__)

# 预设的问答规则，使用正则表达式匹配用户输入
responses = {
    r'你好|hello|hi': "你好！我是你的AI助手，有什么可以帮助你的吗？",
    r'你是谁': "我是一个简单的聊天机器人！",
    r'你的名字是什么': "我叫CyberBot！",
    r'今天天气怎么样': "我无法实时获取天气，但你可以查看天气预报网站哦！",
    r'现在几点了': "当前时间请看你的系统时钟！",
    r'你能做什么': "我可以进行基本的对话，帮助你回答一些简单的问题！",
    r'再见|bye': "再见！希望很快再见到你！",
    r'你喜欢什么': "我喜欢和你聊天！",
    r'你会讲笑话吗': "当然！为什么程序员喜欢黑色？因为它所有的颜色都包含在里面了！",
    r'你喜欢什么颜色': "我喜欢霓虹红和黑色，它们充满赛博朋克风格！"
}

def get_response(user_input):
    """
    根据用户输入返回预设的响应。
    :param user_input: 用户输入的文本
    :return: 匹配的回复或默认回复
    """
    for pattern, response in responses.items():
        if re.search(pattern, user_input, re.IGNORECASE):  # 忽略大小写进行匹配
            return response
    return "抱歉，我不太明白你的问题，可以换个方式问问吗？"

@app.route('/')
def index():
    """
    渲染 HTML 页面
    """
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """
    处理聊天请求，接收 JSON 格式的消息，并返回 AI 响应
    """
    user_input = request.json.get("message", "")  # 获取用户发送的消息
    response = get_response(user_input)  # 获取匹配的机器人回复
    return jsonify({"response": response})  # 以 JSON 格式返回响应

if __name__ == '__main__':
    app.run(debug=True)  # 运行 Flask 服务器，开启调试模式
