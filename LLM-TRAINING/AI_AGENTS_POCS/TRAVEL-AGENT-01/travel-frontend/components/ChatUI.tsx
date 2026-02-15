"use client";

import { useState, useEffect, useRef } from "react";

type Flight = {
  rank: number;
  airline: string;
  flight_number: string;
  departure: string;
  arrival: string;
  price: number;
  booking_link: string;
};

type Message =
  | {
      role: "user" | "assistant";
      type: "text";
      content: string;
      time?: string;
    }
  | {
      role: "assistant";
      type: "flights";
      data: {
        origin: string;
        destination: string;
        date: string;
        flights: Flight[];
      };
      time?: string;
    };

export default function ChatUI() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const bottomRef = useRef<HTMLDivElement | null>(null);

  useEffect(() => {
    setMessages([
      {
        role: "assistant",
        type: "text",
        content: "Hi 👋 How can I help you with your travel plans today?",
        time: new Date().toLocaleTimeString(),
      },
    ]);
  }, []);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = input;

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        type: "text",
        content: userMessage,
        time: new Date().toLocaleTimeString(),
      },
    ]);

    setInput("");
    setLoading(true);

    try {
      const res = await fetch(
        `${process.env.NEXT_PUBLIC_BACKEND_URL}/chat`,
        {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ message: userMessage }),
        }
      );

      const data = await res.json();

      if (data.type === "structured" && data.category === "flights") {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            type: "flights",
            data: data.data,
            time: new Date().toLocaleTimeString(),
          },
        ]);
      } else {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            type: "text",
            content: data.answer,
            time: new Date().toLocaleTimeString(),
          },
        ]);
      }
    } catch {
      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          type: "text",
          content: "⚠️ Backend connection failed.",
          time: new Date().toLocaleTimeString(),
        },
      ]);
    }

    setLoading(false);
  };

  return (
    <div className="flex h-[calc(100vh-80px)]">

      {/* SIDEBAR */}
      <aside className="w-64 bg-white border-r px-6 py-6 hidden md:block">
        <h1 className="text-xl font-bold mb-10">TravelGeek</h1>

        <nav className="space-y-5 text-slate-700">
          <SidebarItem label="Chats" />
          <SidebarItem label="Trips" />
          <SidebarItem label="Explore" />
          <SidebarItem label="Saved" />
          <SidebarItem label="Updates" />
          <SidebarItem label="Inspiration" />
          <SidebarItem label="Create" />
        </nav>

        <button className="mt-10 w-full bg-slate-900 text-white py-3 rounded-full">
          New chat
        </button>
      </aside>

      {/* CHAT AREA */}
      <main className="flex-1 flex flex-col bg-slate-50">

        {/* HEADER */}
        <div className="bg-white/80 backdrop-blur border-b px-8 py-4 font-semibold text-lg">
          Travel Conversation
        </div>

        {/* MESSAGES */}
        <div className="flex-1 overflow-y-auto px-10 py-10 space-y-8">

          {messages.map((msg, i) => (
            <div
              key={i}
              className={`flex ${
                msg.role === "user"
                  ? "justify-end"
                  : "justify-start"
              }`}
            >
              {msg.role === "assistant" && (
                <div className="mr-4 w-10 h-10 bg-yellow-400 rounded-full flex items-center justify-center shadow">
                  👓
                </div>
              )}

              <div
                className={`max-w-4xl px-6 py-5 rounded-2xl text-sm shadow ${
                  msg.role === "user"
                    ? "bg-gradient-to-r from-indigo-500 to-purple-600 text-white"
                    : "bg-white border text-slate-800"
                }`}
              >
                {/* TEXT MESSAGE */}
                {msg.type === "text" && (
                  <div className="whitespace-pre-line">
                    {msg.content}
                  </div>
                )}

                {/* FLIGHT TABLE */}
                {msg.type === "flights" && (
                  <>
                    <h3 className="text-lg font-semibold mb-4">
                      Cheapest Flights from {msg.data.origin} to{" "}
                      {msg.data.destination} on {msg.data.date}
                    </h3>

                    <div className="overflow-x-auto">
                      <table className="min-w-full text-sm border rounded-lg overflow-hidden">
                        <thead className="bg-slate-100">
                          <tr className="text-left">
                            <th className="px-4 py-3">Rank</th>
                            <th className="px-4 py-3">Airline</th>
                            <th className="px-4 py-3">Flight</th>
                            <th className="px-4 py-3">Departure</th>
                            <th className="px-4 py-3">Arrival</th>
                            <th className="px-4 py-3">Price</th>
                            
                          </tr>
                        </thead>
                        <tbody>
                          {msg.data.flights.map((f, idx) => (
                            <tr
                              key={idx}
                              className="border-t hover:bg-slate-50 transition"
                            >
                              <td className="px-4 py-3">{f.rank}</td>
                              <td className="px-4 py-3 font-medium">
                                {f.airline}
                              </td>
                              <td className="px-4 py-3">
                                {f.flight_number}
                              </td>
                              <td className="px-4 py-3">
                                {f.departure}
                              </td>
                              <td className="px-4 py-3">
                                {f.arrival}
                              </td>
                              <td className="px-4 py-3 font-semibold text-indigo-600">
                                ₹{f.price.toLocaleString()}
                              </td>
                              <td className="px-4 py-3">
                                <a
                                  href={f.booking_link}
                                  target="_blank"
                                  className="text-blue-600 underline"
                                >
                                  Book
                                </a>
                              </td>
                            </tr>
                          ))}
                        </tbody>
                      </table>
                    </div>
                  </>
                )}

                <div className="text-xs mt-3 opacity-60">
                  {msg.time}
                </div>
              </div>
            </div>
          ))}

          {/* LOADING */}
          {loading && (
            <div className="flex items-center gap-4">
              <div className="w-10 h-10 bg-yellow-400 rounded-full flex items-center justify-center shadow">
                👓
              </div>
              <div className="bg-white px-6 py-4 rounded-2xl shadow border text-sm">
                TravelGeek is thinking...
              </div>
            </div>
          )}

          <div ref={bottomRef} />
        </div>

        {/* INPUT */}
        <div className="border-t bg-white px-10 py-5">
          <div className="flex items-center gap-3 max-w-4xl mx-auto">
            <button className="text-xl">＋</button>

            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Ask anything about travel..."
              className="flex-1 border rounded-full px-6 py-3 outline-none focus:ring-2 focus:ring-indigo-400"
            />

            <button
              onClick={sendMessage}
              className="bg-indigo-600 hover:bg-indigo-700 text-white px-6 py-3 rounded-full transition"
            >
              ➤
            </button>
          </div>
        </div>
      </main>
    </div>
  );
}

function SidebarItem({ label }: { label: string }) {
  return (
    <div className="cursor-pointer hover:text-indigo-600 transition">
      {label}
    </div>
  );
}

