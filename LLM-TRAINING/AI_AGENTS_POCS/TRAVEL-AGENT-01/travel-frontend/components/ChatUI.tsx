"use client";

import { useState, useEffect, useRef } from "react";

interface Message {
  type: string;
  category?: string;
  data?: any;
  message?: string;
}

export default function ChatUI() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([
    {
      type: "bot",
      message: "Hi 👋 How can I assist you with your travel plans today?",
    },
  ]);
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef<HTMLDivElement>(null);

  // Auto-scroll only after first real user message
  useEffect(() => {
    if (messages.length > 1) {
      bottomRef.current?.scrollIntoView({ behavior: "smooth" });
    }
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { type: "user", message: input };
    setMessages((prev) => [...prev, userMessage]);
    setLoading(true);

    try {
      const res = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input }),
      });

      const data = await res.json();
      setMessages((prev) => [...prev, data]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { type: "error", message: "Server error. Please try again." },
      ]);
    }

    setLoading(false);
    setInput("");
  };

  return (
    <div className="flex h-full">

      {/* Sidebar */}
      <div className="w-64 bg-white border-r hidden md:flex flex-col p-6">
        <button
          onClick={() =>
            setMessages([
              {
                type: "bot",
                message:
                  "Hi 👋 How can I assist you with your travel plans today?",
              },
            ])
          }
          className="bg-black text-white py-2 rounded-md mb-6"
        >
          + New Chat
        </button>

        <div className="space-y-4 text-gray-600 text-sm">
          <p>Trips</p>
          <p>Explore</p>
          <p>Saved</p>
          <p>Updates</p>
          <p>Inspiration</p>
        </div>
      </div>

      {/* Chat Area */}
      <div className="flex-1 flex flex-col">

        {/* Messages */}
        <div className="flex-1 overflow-y-auto px-6 py-10 space-y-6 max-w-3xl mx-auto w-full">

          {messages.map((msg, i) => (
            <div key={i}>

              {/* USER */}
              {msg.type === "user" && (
                <div className="flex justify-end">
                  <div className="bg-black text-white px-4 py-3 rounded-lg max-w-xl">
                    {msg.message}
                  </div>
                </div>
              )}

              {/* BOT TEXT */}
              {msg.type === "bot" && (
                <div className="flex items-start gap-3">
                  <div className="text-xl">🤖</div>
                  <div className="bg-white px-4 py-3 rounded-lg shadow max-w-xl">
                    {msg.message}
                  </div>
                </div>
              )}

              {/* ERROR */}
              {msg.type === "error" && (
                <div className="flex items-start gap-3">
                  <div>⚠️</div>
                  <div className="bg-red-100 text-red-600 px-4 py-3 rounded-lg">
                    {msg.message}
                  </div>
                </div>
              )}

{/* ================= FLIGHTS ================= */}
{msg.category === "flights" && msg.data?.flights && (
  <div className="flex items-start gap-3">
    <div className="text-2xl mt-1">✈️</div>

    <div className="bg-white p-6 rounded-2xl shadow-sm w-full overflow-x-auto">
      <h2 className="font-semibold text-lg mb-6 text-gray-800">
        Flights from {msg.data.origin} to {msg.data.destination} on{" "}
        {msg.data.date}
      </h2>

      <table className="w-full border-collapse text-sm">
        <thead>
          <tr className="bg-gray-50 text-gray-600 uppercase text-xs tracking-wider">
            <th className="py-3 px-4 text-center w-12">#</th>
            <th className="py-3 px-4 text-left w-20">Airline</th>
            <th className="py-3 px-4 text-left w-28">Flight</th>
            <th className="py-3 px-4 text-center w-24">Departure</th>
            <th className="py-3 px-4 text-center w-24">Arrival</th>
            <th className="py-3 px-4 text-center w-24">Duration</th>
            <th className="py-3 px-4 text-right w-28">Price</th>
          </tr>
        </thead>

        <tbody>
          {msg.data.flights.map((f: any, index: number) => (
            <tr
              key={index}
              className="border-t hover:bg-gray-50 transition"
            >
              <td className="py-3 px-4 text-center">{f.rank}</td>
              <td className="py-3 px-4 text-left font-medium">
                {f.airline}
              </td>
              <td className="py-3 px-4 text-left">{f.flight_no}</td>
              <td className="py-3 px-4 text-center">{f.departure}</td>
              <td className="py-3 px-4 text-center">{f.arrival}</td>
              <td className="py-3 px-4 text-center">{f.duration}</td>
              <td className="py-3 px-4 text-right font-semibold text-blue-600">
                ₹{f.price.toLocaleString()}
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  </div>
)}

              {/* HOTELS */}
              {msg.category === "hotels" && msg.data?.hotels && (
                <div className="bg-white p-6 rounded-lg shadow">
                  <h2 className="font-semibold mb-4">
                    Budget Hotels in {msg.data.city}
                  </h2>
                  <ul className="list-disc pl-6 space-y-2">
                    {msg.data.hotels.map((h: any, idx: number) => (
                      <li key={idx}>
                        <strong>{h.hotel_name}</strong> — ₹
                        {h.price.toLocaleString()} {h.currency}
                      </li>
                    ))}
                  </ul>
                </div>
              )}

              {/* PLACES */}
{msg.category === "places" && msg.data?.summary && (
  <div className="bg-white p-6 rounded-lg shadow">
    <h2 className="font-semibold mb-4">Travel Information</h2>
    <div className="whitespace-pre-line">
      {msg.data.summary}
    </div>
  </div>
)}
              {/* ITINERARY */}
              {msg.category === "itinerary" && msg.data?.content && (
                <div className="bg-white p-6 rounded-lg shadow">
                  <h2 className="font-semibold mb-4">Travel Plan</h2>
                  <p className="whitespace-pre-line">
                    {msg.data.content}
                  </p>
                </div>
              )}
            </div>
          ))}

          {loading && (
            <div className="text-gray-400 text-sm">AI is typing...</div>
          )}

          <div ref={bottomRef} />
        </div>

        {/* Input */}
        <div className="border-t bg-white p-4">
          <div className="max-w-3xl mx-auto flex gap-3">
            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Message TravelGeek..."
              className="flex-1 border rounded-lg px-4 py-3 focus:outline-none focus:ring-2 focus:ring-black"
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            />
            <button
              onClick={sendMessage}
              className="bg-black text-white px-6 rounded-lg"
            >
              Send
            </button>
          </div>
        </div>

      </div>
    </div>
  );
}

