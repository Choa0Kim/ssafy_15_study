// chat.js
// 실제 api key 넣으셔야 챗봇 작동합니당
// api key는 일부러 제외했습니다.
const API_KEY = "api key 자리!!"; 
const chatContent = document.getElementById('chat-content');
const userInput = document.getElementById('user-input');
const sendBtn = document.getElementById('send-btn');
const chatToggleBtn = document.getElementById('chat-toggle-btn');
const chatWindow = document.getElementById('chat-window');
const closeChat = document.getElementById('close-chat');

// 챗봇 창 열기/닫기
chatToggleBtn.onclick = () => {
    chatWindow.style.display = chatWindow.style.display === 'none' ? 'flex' : 'none';
};

closeChat.onclick = () => {
    chatWindow.style.display = 'none';
};

// 메시지 전송 및 API 호출
async function sendMessage() {
    const text = userInput.value.trim();
    if (!text) return;

    appendMessage('user', text);
    userInput.value = '';

    try {
        const response = await fetch(`https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=${API_KEY}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                contents: [{ parts: [{ text: `너는 FinanceLink의 금융 상담사야. 간결하고 친절하게 답해줘: ${text}` }] }]
            })
        });

        const data = await response.json();
        const botResponse = data.candidates[0].content.parts[0].text;
        appendMessage('bot', botResponse);
    } catch (error) {
        appendMessage('bot', "오류가 발생했습니다. API 키를 확인해주세요.");
    }
}

function appendMessage(sender, text) {
    const msgDiv = document.createElement('div');
    msgDiv.className = `message ${sender === 'user' ? 'user-msg' : 'bot-msg'}`;
    msgDiv.innerText = text;
    chatContent.appendChild(msgDiv);
    chatContent.scrollTop = chatContent.scrollHeight;
}

sendBtn.onclick = sendMessage;
userInput.onkeypress = (e) => { if (e.key === 'Enter') sendMessage(); };