"use client";

import { useState, useEffect, useRef } from "react";
import ReactMarkdown from "react-markdown";

type Flight = {
  rank: number;
  airline: string;
  flight_number: string;
  departure_time: string;
  arrival_time: string;
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
      flights: Flight[];
      route: string;
      date: string;
      time?: string;
    };

export default function ChatUI() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);

  const bottomRef = useRef<HTMLDivElement | null>(null);

  // Greeting (client only → no hydration error)
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

      // Structured Flights
      if (data.type === "structured" && data.category === "flights") {
        setMessages((prev) => [
          ...prev,
          {
            role: "assistant",
            type: "flights",
            flights: data.data.flights,
            route: `${data.data.origin} → ${data.data.destination}`,
            date: data.data.date,
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

        <div className="border-b bg-white px-6 py-4 font-semibold">
          Travel Conversation
        </div>

        {/* MESSAGES */}
        <div className="flex-1 overflow-y-auto px-6 py-8 space-y-6">

          {messages.map((msg, i) => (
            <div key={i} className={`flex ${msg.role === "user" ? "justify-end" : "justify-start"}`}>

              {msg.role === "assistant" && (
                <div className="mr-3 w-10 h-10 bg-yellow-400 rounded-full flex items-center justify-center">
                  👓
                </div>
              )}

              {/* TEXT MESSAGE */}
              {msg.type === "text" && (
                <div
                  className={`max-w-2xl px-5 py-4 rounded-2xl text-sm shadow ${
                    msg.role === "user"
                      ? "bg-gradient-to-r from-indigo-500 to-purple-600 text-white"
                      : "bg-white text-slate-800 border"
                  }`}
                >
                  <ReactMarkdown
                    components={{
                      p: ({ children }) => (
                        <p className="mb-3 leading-relaxed">{children}</p>
                      ),
                      li: ({ children }) => (
                        <li className="ml-5 list-disc mb-1">{children}</li>
                      ),
                      h3: ({ children }) => (
                        <h3 className="font-semibold mt-4 mb-2">{children}</h3>
                      ),
                    }}
                  >
                    {msg.content}
                  </ReactMarkdown>

                  <div className="text-xs mt-3 opacity-60">
                    {msg.time}
                  </div>
                </div>
              )}

              {/* FLIGHT TABLE MESSAGE */}
              {msg.type === "flights" && (
                <div className="bg-white border rounded-2xl shadow p-5 max-w-5xl overflow-x-auto">

                  <h3 className="font-semibold mb-4">
                    Cheapest Flights ({msg.route}) on {msg.date}
                  </h3>

                  <table className="w-full text-sm border-collapse">
                    <thead>
                      <tr className="bg-slate-100">
                        <th className="p-2 text-left">Rank</th>
                        <th className="p-2 text-left">Airline</th>
                        <th className="p-2 text-left">Flight No</th>
                        <th className="p-2 text-left">Departure</th>
                        <th className="p-2 text-left">Arrival</th>
                        <th className="p-2 text-left">Price</th>
                        <th className="p-2 text-left">Booking</th>
                      </tr>
                    </thead>
                    <tbody>
                      {msg.flights.map((f) => (
                        <tr key={f.rank} className="border-b hover:bg-slate-50">
                          <td className="p-2">{f.rank}</td>
                          <td className="p-2 font-medium">{f.airline}</td>
                          <td className="p-2">{f.flight_number}</td>
                          <td className="p-2">{f.departure_time}</td>
                          <td className="p-2">{f.arrival_time}</td>
                          <td className="p-2">₹{f.price.toLocaleString()}</td>
                          <td className="p-2">
                            <a
                              href={f.booking_link}
                              target="_blank"
                              className="text-indigo-600 underline"
                            >
                              Book
                            </a>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>

                  <div className="text-xs mt-3 opacity-60">
                    {msg.time}
                  </div>
                </div>
              )}
            </div>
          ))}

          {loading && (
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-yellow-400 rounded-full flex items-center justify-center">
                👓
              </div>
              <div className="bg-white px-5 py-3 rounded-2xl shadow border text-sm">
                TravelGeek is thinking...
              </div>
            </div>
          )}

          <div ref={bottomRef} />
        </div>

        {/* INPUT */}
        <div className="border-t bg-white px-6 py-4">
          <div className="flex items-center gap-3 max-w-3xl mx-auto">
            <button className="text-xl">＋</button>

            <input
              value={input}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && sendMessage()}
              placeholder="Ask anything"
              className="flex-1 border rounded-full px-5 py-3 outline-none"
            />

            <button
              onClick={sendMessage}
              className="bg-indigo-600 text-white px-6 py-2 rounded-full"
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
    <div className="cursor-pointer hover:text-indigo-600">
      {label}
    </div>
  );
}

