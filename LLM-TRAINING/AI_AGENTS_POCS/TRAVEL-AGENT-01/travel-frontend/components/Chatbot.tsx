"use client";

import { useState } from "react";

/* --- BOT AVATAR --- */
const BOT_AVATAR =
  "https://images.pexels.com/photos/415829/pexels-photo-415829.jpeg";

type Message =
  | { sender: "user"; text: string }
  | { sender: "bot"; text?: string; payload?: any };

export default function Chatbot() {
  const [open, setOpen] = useState(false);
  const [msg, setMsg] = useState("");
  const [isTyping, setIsTyping] = useState(false);

  const [messages, setMessages] = useState<Message[]>([
    {
      sender: "bot",
      text: "Hi, I'm Mimi. I'm your travel Assistant. What can I do for you today?"
    }
  ]);

  async function sendMessage() {
    if (!msg.trim()) return;

    const userText = msg;

    setMessages((prev) => [...prev, { sender: "user", text: userText }]);
    setMsg("");
    setIsTyping(true);

    try {
      const API_URL = process.env.NEXT_PUBLIC_BACKEND_URL;
      if (!API_URL) throw new Error("NEXT_PUBLIC_BACKEND_URL not defined");

      const res = await fetch(`${API_URL}/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: userText })
      });

      const data = await res.json();

      if (data.type === "flights") {
        setMessages((prev) => [
          ...prev,
          { sender: "bot", payload: data }
        ]);
      } else {
        setMessages((prev) => [
          ...prev,
          { sender: "bot", text: data.answer }
        ]);
      }
    } catch (err) {
      console.error("Chat error:", err);
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
      >
        💬
      </button>
    );
  }

  /* ---------------- OPEN STATE ---------------- */
  return (
    <div className="fixed bottom-6 right-6 w-[360px] h-[520px] bg-white rounded-2xl shadow-xl flex flex-col overflow-hidden z-50">
      {/* Header */}
      <div className="bg-blue-600 text-white p-4 flex items-center gap-3">
        <img
          src={BOT_AVATAR}
          className="w-10 h-10 rounded-full object-cover"
          alt="bot"
        />
        <div className="flex-1">
          <div className="font-semibold text-sm">
            Mimi <span className="text-xs">(AI Assistant)</span>
          </div>
          <div className="text-xs opacity-80">Online</div>
        </div>
        <button onClick={() => setOpen(false)}>✕</button>
      </div>

      {/* Messages */}
      <div className="flex-1 p-3 overflow-y-auto space-y-4 bg-gray-50">
        {messages.map((m, i) => (
          <div
            key={i}
            className={`flex gap-2 ${m.sender === "user" ? "justify-end" : ""}`}
          >
            {m.sender === "bot" && (
              <img
                src={BOT_AVATAR}
                className="w-7 h-7 rounded-full"
                alt="bot"
              />
            )}

            <div
              className={`rounded-xl px-3 py-2 text-sm max-w-[85%]
                ${
                  m.sender === "user"
                    ? "bg-blue-600 text-white"
                    : "bg-white shadow"
                }
              `}
            >
              {m.payload?.type === "flights" ? (
                <FlightCards data={m.payload} />
              ) : (
                m.text
              )}
            </div>
          </div>
        ))}

        {isTyping && (
          <div className="text-xs text-gray-500">Mimi is typing...</div>
        )}
      </div>

      {/* Input */}
      <div className="p-3 border-t">
        <div className="flex gap-2">
          <input
            value={msg}
            onChange={(e) => setMsg(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Ask me anything..."
            className="flex-1 border rounded-full px-3 py-2 text-sm outline-none"
          />
          <button
            onClick={sendMessage}
            className="bg-blue-600 text-white px-4 rounded-full"
          >
            ➤
          </button>
        </div>
      </div>
    </div>
  );
}

/* ---------------- Flight Cards Component ---------------- */

function FlightCards({ data }: any) {
  return (
    <div className="space-y-3">
      <div className="text-xs text-gray-500 font-semibold">
        ✈ {data.origin} → {data.destination} | {data.date}
      </div>

      {data.flights.map((f: any, i: number) => (
        <div
          key={i}
          className="border rounded-xl p-2 bg-white shadow-sm text-xs"
        >
          <div className="flex justify-between items-center">
            <div className="font-semibold">
              {f.airline} · {f.flight_no}
            </div>
            <div className="text-green-600 font-bold">
              ₹{f.price.toLocaleString()}
            </div>
          </div>

          <div className="flex justify-between mt-1 text-gray-600">
            <span>⏱ {f.duration}</span>
            <span>✈ {f.route}</span>
          </div>

          <button className="mt-2 w-full bg-blue-600 text-white text-xs py-1 rounded-lg hover:bg-blue-700">
            Book
          </button>
        </div>
      ))}
    </div>
  );
}

