function sendMessage(event) {
    if (event && event.key !== "Enter") return;

    let userInput = document.getElementById("user-input");
    let message = userInput.value.trim();
    if (message === "") return;

    let chatBox = document.getElementById("chat-box");

    // 添加用户消息
    let userMessage = document.createElement("div");
    userMessage.classList.add("user-message");
    userMessage.textContent = "🧑‍💻 你: " + message;
    chatBox.appendChild(userMessage);

    userInput.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;

    // 发送到后端
    fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        let botMessage = document.createElement("div");
        botMessage.classList.add("bot-message");
        botMessage.textContent = "👾 CyberBot: " + data.response;
        chatBox.appendChild(botMessage);
        chatBox.scrollTop = chatBox.scrollHeight;
    });
}
