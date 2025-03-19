# 赛博朋克风格 Flask 聊天机器人 

## 📌 项目简介
本项目是一个基于 Flask 框架的简单聊天机器人，使用正则表达式进行关键词匹配，具备基础的对话能力，并拥有赛博朋克风格的 Web UI。

## 💡 核心技术：
- ✅ Flask 后端 —— 处理用户输入、返回 AI 回复
- ✅ HTML + CSS + JS —— 构建炫酷的赛博朋克风 Web 界面
- ✅ 异步交互 —— 通过 AJAX（fetch API）实现无刷新聊天

## 📁 项目结构
Chatbot/
│── static/          # 存放前端静态文件（CSS、JS）
│   ├── style.css    # 赛博朋克风格的 CSS 样式
│   ├── script.js    # 处理用户输入的 JavaScript 代码
│── templates/       # 存放 HTML 模板
│   ├── index.html   # 聊天页面
│── app.py           # Flask 后端主程序
│── README.md        # 项目说明文档
│── requirements.txt # 依赖文件

## ✨ 主要功能
- 🔍 关键词匹配：使用正则表达式识别用户输入，返回预设回答
- 🌐 Flask Web 界面：采用黑色 + 霓虹红 UI，打造沉浸式赛博朋克风体验
- ⚡ 异步交互：前端通过 Fetch API 发送请求，实现无刷新聊天
- 🧠 简单上下文记忆：可记住用户名，并提供相应的个性化对话

## 💻 安装与运行
### 📌 1. 环境要求
- Python 3.x
- Flask
- Web 浏览器（推荐 Chrome）

### 📌 2. 安装依赖
在终端（Terminal / CMD / PowerShell）中运行：
```
pip install flask
```

### 📌 3. 运行项目
```
python app.py
```
如果运行成功，终端会显示：
```
Running on http://127.0.0.1:5000/
```
然后打开浏览器，访问 http://127.0.0.1:5000/ 开始聊天！

## 📜 代码解析
### 1️⃣ app.py（Flask 后端）
- responses 字典：存储用户输入与 AI 响应的匹配规则
- get_response(user_input)：使用正则匹配用户输入，返回 AI 回复
- / 路由：渲染 index.html，加载聊天界面
- /chat API：处理前端请求，返回 AI 回复（JSON 格式）

### 2️⃣ index.html（前端 UI）
- 输入框：用户输入消息
- 按钮：点击“发送”或按 Enter 发送消息
- 聊天框：显示聊天记录

### 3️⃣ style.css（前端 UI 样式）
- 黑色背景 + 霓虹红 UI，打造沉浸式赛博朋克风
- 滚动聊天框，显示用户与 AI 消息

### 4️⃣ script.js（前端交互）
- 监听回车事件，输入后自动发送消息
- 使用 Fetch API 调用 /chat 接口，获取 AI 回复
- 动态更新聊天内容，实现无刷新交互

## 📌 示例对话
用户: 你好
AI: 你好！我是你的AI助手，有什么可以帮助你的吗？

用户: 你是谁
AI: 我是一个简单的聊天机器人！

用户: 你会讲笑话吗
AI: 当然！为什么程序员喜欢黑色？因为它所有的颜色都包含在里面了！

用户: 再见
AI: 再见！希望很快再见到你！

## 📌 未来优化
- ✅ 支持更复杂的对话逻辑（基于 AI 或 NLP 处理）
- ✅ 添加 WebSocket 实现实时聊天
- ✅ 扩展 UI（增加用户头像、动画效果等）

## 📌 许可证
本项目基于 MIT License 开源，欢迎二次开发和改进！ 🚀🚀
