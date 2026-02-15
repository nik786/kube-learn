"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

export default function Home() {
  const router = useRouter();
  const [teaserInput, setTeaserInput] = useState("");

  const handleSubmit = () => {
    if (!teaserInput.trim()) return;
    router.push(`/chat?prompt=${encodeURIComponent(teaserInput)}`);
  };

  return (
    <main className="w-full">

      {/* HERO SECTION */}
      <section
        className="min-h-screen pt-32 flex flex-col items-center justify-center text-center px-6"
        style={{
          backgroundImage:
            "linear-gradient(to bottom, #fbcfe8, #ddd6fe, #c7d2fe)",
        }}
      >
        <div className="bg-white/70 backdrop-blur-sm rounded-3xl px-10 py-14 max-w-3xl w-full">
          <div className="flex justify-center mb-6">
            <div className="w-16 h-16 rounded-full bg-yellow-400 flex items-center justify-center text-2xl">
              ✈️
            </div>
          </div>

          <h1 className="text-4xl md:text-6xl font-bold text-slate-900">
            Meet your personal <br /> travel genius ✨
          </h1>

          <p className="mt-6 text-slate-700 text-lg">
            Plan complex trips in minutes. Real-time info for flights, stays,
            restaurants and experiences.
          </p>

          {/* CHAT TEASER */}
          <div className="mt-12">
            <div className="bg-gradient-to-r from-pink-300 via-purple-300 to-indigo-300 p-2 rounded-full">
              <div className="flex items-center gap-4 px-6 py-4 rounded-full bg-white/90 backdrop-blur shadow-lg hover:shadow-xl transition">

                <div className="text-2xl text-yellow-400">✨</div>

                <input
                  value={teaserInput}
                  onChange={(e) => setTeaserInput(e.target.value)}
                  onKeyDown={(e) => {
                    if (e.key === "Enter") handleSubmit();
                  }}
                  placeholder="Ask me anything about travel!"
                  className="flex-1 bg-transparent outline-none text-slate-600"
                />

                <button
                  onClick={handleSubmit}
                  className="w-10 h-10 rounded-full bg-yellow-400 flex items-center justify-center text-black"
                >
                  ➤
                </button>

              </div>
            </div>
          </div>
        </div>
      </section>

      {/* TRAVEL CATEGORIES */}
      <section className="bg-white py-16">
        <div className="max-w-6xl mx-auto flex flex-wrap justify-center gap-12">
          <Category icon="🏨" label="Stays" active />
          <Category icon="✈️" label="Flights" />
          <Category icon="🚗" label="Cars" />
          <Category icon="📦" label="Packages" />
          <Category icon="🗺️" label="Tourist Places" />
          <Category icon="🚌" label="Buses" />
          <Category icon="🚆" label="Trains" />
        </div>
      </section>

      {/* TRAVELGEEK – EDITORIAL */}
      <section className="bg-white py-24 px-6">
        <div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-16 items-center">
          <div>
            <div className="flex items-center gap-4 mb-6">
              <div className="w-12 h-12 rounded-full bg-black flex items-center justify-center text-white">
                👓
              </div>
              <h2 className="text-3xl font-bold">TravelGeek</h2>
            </div>

            <p className="text-slate-700 text-lg leading-relaxed max-w-xl">
              is your travel genius, here to make planning your next adventure
              as easy as texting a friend. Built with cutting-edge AI and
              supercharged by real-time data, TravelGeek helps you dream up,
              plan, and book your trip from start to finish.
            </p>

            <div className="grid grid-cols-2 gap-10 mt-12">
              <FeatureBlock icon="💡" title="Get inspired" desc="Personalized destination ideas" />
              <FeatureBlock icon="🏷️" title="Price check" desc="Compare flights, hotels & activities" />
              <FeatureBlock icon="💬" title="One chat" desc="Everything in one conversation" />
              <FeatureBlock icon="🕒" title="In real time" desc="Maps and local tips as you go" />
            </div>
          </div>

          <div className="relative">
            <div className="rounded-3xl overflow-hidden shadow-xl">
              <img
                src="https://images.unsplash.com/photo-1517841905240-472988babdf9"
                alt="Traveler using phone"
                className="w-full h-full object-cover"
              />
            </div>

            <div className="absolute top-6 left-[-30px] bg-white px-4 py-2 rounded-full shadow text-sm">
              ✈️ Book me a flight to Rome
            </div>

            <div className="absolute bottom-8 right-[-30px] bg-white px-4 py-2 rounded-full shadow text-sm">
              🍽️ Recommend a dinner spot
            </div>
          </div>
        </div>
      </section>

      {/* ASK TRAVELGEEK – CARD STYLE */}
      <section className="bg-[#232b2b] py-28 px-6 text-white">
        <div className="max-w-7xl mx-auto">
          <div className="flex items-center justify-center gap-4 mb-16">
            <h2 className="text-4xl font-bold">Ask</h2>
            <div className="w-14 h-14 rounded-full bg-yellow-400 flex items-center justify-center text-black text-2xl">
              👓
            </div>
            <h2 className="text-4xl font-bold">TravelGeek</h2>
          </div>

          <div className="grid md:grid-cols-4 gap-10">
            <AskImageCard image="https://images.unsplash.com/photo-1552566626-52f8b828add9" text="Treat yourself to gourmet seafood by the sea." />
            <AskImageCard image="https://images.unsplash.com/photo-1507525428034-b723cf961d3e" text="Discover dreamy destinations with clear blue waters." />
            <AskImageCard image="https://images.unsplash.com/photo-1500534314209-a25ddb2bd429" text="Send me to stunning cliffside escapes." />
            <AskImageCard image="https://images.unsplash.com/photo-1542038784456-1ea8e935640e" text="Find unforgettable family adventures." />
          </div>
        </div>
      </section>

      {/* BRANDS */}
      <section
        className="relative min-h-[85vh] bg-cover bg-center flex items-center justify-center text-white"
        style={{
          backgroundImage:
            "url(https://images.unsplash.com/photo-1501785888041-af3ef285b470)",
        }}
      >
        <div className="absolute inset-0 bg-black/60" />
        <div className="relative z-10 text-center px-6 max-w-4xl">
          <h2 className="text-4xl md:text-6xl font-semibold mb-6">
            TravelGeek for Brands
          </h2>
          <p className="text-lg md:text-xl text-slate-200">
            We are the AI backbone of the travel industry. Build and launch your
            own customized AI agents based on your brand, content and data.
          </p>
          <button className="mt-10 bg-black text-yellow-400 px-10 py-4 rounded-full">
            Learn more
          </button>
        </div>
      </section>

      {/* FOOTER */}
      <footer className="bg-black text-slate-300 py-10 px-6">
        <div className="max-w-7xl mx-auto flex flex-col md:flex-row items-center justify-between gap-6">
          <div className="flex items-center gap-3">
            <div className="w-10 h-10 rounded-full bg-yellow-400 flex items-center justify-center text-black">
              👓
            </div>
            <span className="text-xl font-semibold">TravelGeek</span>
          </div>

          <div className="text-sm text-center">
            <p>© 2026 TravelGeek</p>
            <p className="mt-1">Powered by Matador Network</p>
            <div className="mt-1 flex gap-3 justify-center text-xs underline">
              <span>Privacy Policy</span>
              <span>Terms of Service</span>
            </div>
          </div>

          <div className="flex items-center gap-4">
            <span className="font-medium">Press</span>
            <div className="w-9 h-9 bg-yellow-400 rounded-md flex items-center justify-center text-black">f</div>
            <div className="w-9 h-9 bg-yellow-400 rounded-md flex items-center justify-center text-black">ⓘ</div>
            <div className="w-9 h-9 bg-yellow-400 rounded-md flex items-center justify-center text-black">▶</div>
          </div>
        </div>
      </footer>
    </main>
  );
}

/* ---------- COMPONENTS ---------- */

function Category({ icon, label, active = false }: any) {
  return (
    <div className="flex flex-col items-center gap-2 cursor-pointer group">
      <div className={`w-14 h-14 flex items-center justify-center rounded-xl text-2xl transition-all ${active ? "bg-indigo-100 text-indigo-600" : "bg-slate-100 text-slate-600 group-hover:bg-indigo-50 group-hover:text-indigo-600"}`}>
        {icon}
      </div>
      <span className={`text-sm font-medium ${active ? "text-indigo-600" : "text-slate-700 group-hover:text-indigo-600"}`}>
        {label}
      </span>
    </div>
  );
}

function FeatureBlock({ icon, title, desc }: any) {
  return (
    <div>
      <div className="text-2xl mb-2">{icon}</div>
      <h4 className="font-semibold text-slate-900">{title}</h4>
      <p className="text-slate-600 text-sm">{desc}</p>
    </div>
  );
}

function AskImageCard({ image, text }: any) {
  return (
    <div className="bg-[#2f3838] rounded-3xl overflow-hidden flex flex-col shadow-lg">
      <img src={image} alt={text} className="h-56 w-full object-cover" />
      <div className="p-6 flex flex-col justify-between flex-1">
        <p className="text-sm text-slate-200 mb-6">“{text}”</p>
        <button className="bg-yellow-400 text-black py-3 rounded-full font-semibold">
          ✨ Ask
        </button>
      </div>
    </div>
  );
}

