import React, { useState } from "react";
import axios from "axios";

const Chatbot = () => {
  const [message, setMessage]: any = useState("");
  const [chatLog, setChatLog]: any = useState([]);

  const handleSendMessage = async () => {
    if (message.trim() === "") return;

    const newMessage = { sender: "user", text: message };
    setChatLog([...chatLog, newMessage]);

    // Send message to Flask backend running on localhost:5000
    try {
      const response = await axios.post("http://localhost:5000/chat", {
        message: message,
      });

      const botMessage: any = { sender: "bot", text: response.data.response };
      setChatLog([...chatLog, newMessage, botMessage]);

      setMessage(""); // Clear message input
    } catch (error) {
      console.error("Error sending message", error);
    }
  };

  return (
    <div className="flex-column">
      <div className="chat-window">
        {chatLog.map((msg, index) => (
          <div key={index} className={msg.sender}>
            <span>{msg.sender === "user" ? "You" : "Bot"}: </span>
            <span>{msg.text}</span>
          </div>
        ))}
      </div>
      <div>
        <input
          type="text"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          placeholder="Type a message"
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chatbot;
