"use client";

import { useState } from "react";

/* --- BOT AVATAR (single source of truth) --- */
const BOT_AVATAR =
  "https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg";

export default function Chatbot() {
  const [open, setOpen] = useState(false);
  const [msg, setMsg] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const [messages, setMessages] = useState([
    {
      sender: "bot",
      text: "Hi, I'm Mimi. I'm your K8s Assistant. What can I do for you today?"
    }
  ]);

  async function sendMessage() {
    if (!msg.trim()) return;

    setMessages((prev) => [...prev, { sender: "user", text: msg }]);
    setMsg("");
    setIsTyping(true);

    try {
      const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: msg })
      });

      const data = await res.json();

      setMessages((prev) => [...prev, { sender: "bot", text: data.reply }]);
    } catch {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "Sorry, something went wrong." }
      ]);
    } finally {
      setIsTyping(false);
    }
  }

  /* ---------------- CLOSED STATE ---------------- */
  if (!open) {
    return (
      <button
        onClick={() => setOpen(true)}
        className="
          fixed bottom-6 right-6
          w-14 h-14
          bg-blue-600
          rounded-full
          shadow-lg
          flex items-center justify-center
          hover:bg-blue-700
          transition
          z-50
        "
        aria-label="Open chat"
      >
        <svg width="26" height="26" viewBox="0 0 24 24" fill="white">
          <path d="M20 2H4C2.9 2 2 2.9 2 4v18l4-4h14c1.1 0 2-.9 2-2V4c0-1.1-.9-2-2-2z" />
        </svg>
      </button>
    );
  }

  /* ---------------- OPEN STATE ---------------- */
  return (
    <div
      className="
        fixed bottom-6 right-6
        w-[360px] h-[520px]
        bg-white
        rounded-2xl
        shadow-xl
        flex flex-col
        overflow-hidden
        z-50
        animate-in slide-in-from-bottom-4 duration-300
      "
    >
      {/* Header */}
      <div className="bg-blue-600 text-white p-4 flex items-center gap-3">
        <div className="relative">
          <img
            src={BOT_AVATAR}
            className="w-10 h-10 rounded-full object-cover"
            alt="Mimi AI Bot"
          />
          {/* Online indicator */}
          <span className="absolute bottom-0 right-0 w-3 h-3 bg-green-500 border-2 border-white rounded-full"></span>
        </div>

        <div className="flex-1">
          <div className="font-semibold leading-tight">
            Mimi <span className="text-xs opacity-80">(AI Assistant)</span>
          </div>
          <div className="text-xs opacity-90">
            We’ll return today at 07:30 PM
          </div>
        </div>

        <button
          onClick={() => setOpen(false)}
          className="text-xl leading-none hover:opacity-80"
          aria-label="Close chat"
        >
          ×
        </button>
      </div>

      {/* Messages */}
      <div className="flex-1 p-4 overflow-y-auto space-y-4 bg-gray-50">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`flex gap-2 ${m.sender === "user" ? "justify-end" : ""}`}
          >
            {m.sender === "bot" && (
              <img
                src={BOT_AVATAR}
                className="w-8 h-8 rounded-full"
                alt="bot"
              />
            )}
            <div
              className={`px-4 py-2 rounded-2xl text-sm max-w-[80%]
                ${
                  m.sender === "bot"
                    ? "bg-white shadow"
                    : "bg-blue-600 text-white"
                }
              `}
            >
              {m.text}
            </div>
          </div>
        ))}

        {/* Typing indicator */}
        {isTyping && (
          <div className="flex gap-2 items-center text-sm text-gray-500">
            <img
              src={BOT_AVATAR}
              className="w-6 h-6 rounded-full"
              alt="typing"
            />
            <span className="animate-pulse">Mimi is typing…</span>
          </div>
        )}
      </div>

      {/* Input */}
      <div className="p-3 border-t bg-white">
        <div className="flex items-center gap-2 border rounded-full px-3 py-2">
          <input
            value={msg}
            onChange={(e) => setMsg(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Ask me anything..."
            className="flex-1 outline-none text-sm"
          />
          <button
            onClick={sendMessage}
            className="text-blue-600 font-semibold"
          >
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}

