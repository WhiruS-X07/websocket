let socket;

function connectWebSocket() {
    socket = new WebSocket("ws://localhost:8080");

    socket.onopen = () => console.log("✅ Connected to WebSocket server");

    socket.onmessage = event => {
        displayMessage("Server: " + event.data);
    };

    socket.onclose = () => {
        console.log("⚠️ WebSocket disconnected. Reconnecting...");
        setTimeout(connectWebSocket, 3000); // Try reconnecting after 3 seconds
    };

    socket.onerror = error => console.error("❌ WebSocket error:", error);
}

window.onload = connectWebSocket; // Connect WebSocket after page loads

function sendMessage() {
    const input = document.getElementById("messageInput");
    if (input.value.trim() !== "" && socket.readyState === WebSocket.OPEN) {
        const messageText = input.value;

        // Display message immediately
        displayMessage("You: " + messageText);

        // Send the message to the server
        socket.send(messageText);

        input.value = ""; // Clear input after sending
    }
}

function getLastMessages() {
    if (socket.readyState === WebSocket.OPEN) {
        socket.send("GET_LAST_5"); // Request last 5 messages
    }
}

function displayMessage(text) {
    const messagesDiv = document.getElementById("messages");
    const message = document.createElement("p");
    message.textContent = text;
    messagesDiv.appendChild(message);
    messagesDiv.scrollTop = messagesDiv.scrollHeight; // Auto-scroll
}