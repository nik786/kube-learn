"use client";

import { useEffect, useRef, useState } from "react";

export default function Chatbot({
  openChat,
  setOpenChat,
  messages,
  setMessages,
}: any) {
  const [input, setInput] = useState("");

  const messagesEndRef = useRef<any>(null);

  // AUTO SCROLL
  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages]);

  // SEND MESSAGE
  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = {
      role: "user",
      text: input,
    };

    setMessages((prev: any) => [...prev, userMessage]);

    const prompt = input;

    setInput("");

    try {
      // LOADING MESSAGE
      const loadingMessage = {
        role: "assistant",
        text: "Thinking...",
        loading: true,
      };

      setMessages((prev: any) => [
        ...prev,
        loadingMessage,
      ]);

      // BACKEND CALL
      const response = await fetch(
        "http://localhost:8000/chat",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            message: prompt,
          }),
        }
      );

      const data = await response.json();

      console.log("LLM RESPONSE:", data);

      // REMOVE LOADING
      setMessages((prev: any) =>
        prev.filter((msg: any) => !msg.loading)
      );

      // TEXT RESPONSE
      if (data.type === "text") {
        setMessages((prev: any) => [
          ...prev,
          {
            role: "assistant",
            text:
              data.answer ||
              "I couldn't generate a response.",
          },
        ]);
      }

      // STRUCTURED FLIGHT RESPONSE
      else if (
        data.type === "structured" &&
        data.category === "flights"
      ) {
        const flights = data.data?.flights || [];

        if (flights.length === 0) {
          setMessages((prev: any) => [
            ...prev,
            {
              role: "assistant",
              text: "😔 No flights found.",
            },
          ]);
        } else {
          const formattedFlights = flights
            .map(
              (f: any) =>
                `✈️ ${f.airline} (${f.flight_no})

🕒 ${f.departure_time} → ${f.arrival_time}

⏱ ${f.duration}

💰 ₹${f.price}`
            )
            .join("\n\n-------------------\n\n");

          setMessages((prev: any) => [
            ...prev,
            {
              role: "assistant",
              text: formattedFlights,
            },
          ]);
        }
      }

      // FALLBACK
      else {
        setMessages((prev: any) => [
          ...prev,
          {
            role: "assistant",
            text:
              "⚠️ Unsupported response type received.",
          },
        ]);
      }
    } catch (error) {
      console.error("CHAT ERROR:", error);

      // REMOVE LOADING
      setMessages((prev: any) =>
        prev.filter((msg: any) => !msg.loading)
      );

      setMessages((prev: any) => [
        ...prev,
        {
          role: "assistant",
          text:
            "⚠️ Failed to connect to AI backend.",
        },
      ]);
    }
  };

  return (
    <div
      className={`fixed top-0 right-0 h-screen w-full md:w-[420px] bg-white shadow-2xl z-50 transform transition-transform duration-300 flex flex-col ${
        openChat
          ? "translate-x-0"
          : "translate-x-full"
      }`}
    >
      {/* HEADER */}
      <div className="flex items-center justify-between px-5 py-4 border-b bg-white">

        <div>
          <h2 className="font-bold text-xl text-slate-900">
            TravelGeek AI
          </h2>

          <p className="text-sm text-slate-500">
            Your personal travel genius ✨
          </p>
        </div>

        <button
          onClick={() => setOpenChat(false)}
          className="text-3xl text-slate-400 hover:text-black transition"
        >
          ✕
        </button>
      </div>

      {/* CHAT AREA */}
      <div className="flex-1 overflow-y-auto p-5 space-y-5 bg-slate-50">

        {messages.map(
          (msg: any, index: number) => (
            <div
              key={index}
              className={`max-w-[85%] px-5 py-4 rounded-3xl text-sm leading-relaxed shadow-sm whitespace-pre-line ${
                msg.role === "user"
                  ? "ml-auto bg-indigo-600 text-white"
                  : msg.loading
                  ? "bg-yellow-100 text-slate-700 animate-pulse"
                  : "bg-green-100 text-slate-800"
              }`}
            >
              {msg.text}
            </div>
          )
        )}

        <div ref={messagesEndRef} />
      </div>

      {/* QUICK SUGGESTIONS */}
      <div className="px-4 py-3 border-t bg-white flex flex-wrap gap-2">

        <button
          onClick={() =>
            setInput(
              "cheap flights from kolkata to bangkok tomorrow"
            )
          }
          className="px-3 py-2 bg-slate-100 hover:bg-slate-200 rounded-full text-sm transition"
        >
          Bangkok flights
        </button>

        <button
          onClick={() =>
            setInput("best hotels in bali")
          }
          className="px-3 py-2 bg-slate-100 hover:bg-slate-200 rounded-full text-sm transition"
        >
          Bali hotels
        </button>

        <button
          onClick={() =>
            setInput("3 day trip to rome")
          }
          className="px-3 py-2 bg-slate-100 hover:bg-slate-200 rounded-full text-sm transition"
        >
          Rome itinerary
        </button>
      </div>

      {/* INPUT */}
      <div className="p-4 border-t bg-white">

        <div className="flex items-center gap-3">

          <input
            value={input}
            onChange={(e) =>
              setInput(e.target.value)
            }
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
            placeholder="Ask your travel question..."
            className="flex-1 border border-slate-300 rounded-full px-5 py-4 outline-none focus:border-indigo-500"
          />

          <button
            onClick={sendMessage}
            className="w-14 h-14 rounded-full bg-yellow-400 hover:scale-105 transition flex items-center justify-center text-black text-xl shadow-lg"
          >
            ➤
          </button>

        </div>
      </div>
    </div>
  );
}
