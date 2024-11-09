function sendMessage() {
    const messageInput = document.getElementById("message-input");
    const chatBox = document.getElementById("varchat_password");

    if (messageInput.value.trim() !== "") {
        const messageElement = document.createElement("div");
        messageElement.textContent = messageInput.value;
        chatBox.appendChild(messageElement);
        messageInput.value = "";
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}

function generatePassword() {
    const characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    let password = "";
    const length = 23; // Define la longitud de la contraseña

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * characters.length);
        password += characters[randomIndex];
    }

    // Mostrar la contraseña generada en el chat
    const chatBox = document.getElementById("varchat_password");
    const passwordMessage = document.createElement("div");
    passwordMessage.textContent = `generated password: ${password}`;
    chatBox.appendChild(passwordMessage);
    chatBox.scrollTop = chatBox.scrollHeight;
}
