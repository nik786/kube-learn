"use client";

import { useState } from "react";
import { Globe, User } from "lucide-react";

export default function Navbar() {
  const [location, setLocation] = useState("");

  const openMap = () => {
    if (!location.trim()) return;

    const query = encodeURIComponent(location);
    window.open(`https://www.google.com/maps/search/?api=1&query=${query}`, "_blank");
  };

  return (
    <nav className="fixed top-0 left-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-slate-200">
      <div className="mx-auto max-w-7xl px-6 py-4 flex items-center justify-between">

        {/* LEFT */}
        <div className="flex items-center gap-10">
          <span className="font-bold text-lg text-slate-900">
            TravelGeek
          </span>

          <ul className="hidden md:flex items-center gap-6 text-slate-800 font-medium">
            <li className="hover:text-indigo-600 cursor-pointer">ItineraryPlanner</li>
            <li className="hover:text-indigo-600 cursor-pointer">TravelGuides</li>
            <li className="hover:text-indigo-600 cursor-pointer">Blogs</li>
            <li className="hover:text-indigo-600 cursor-pointer">Resources</li>
          </ul>
        </div>

        {/* RIGHT */}
        <div className="flex items-center gap-4">

          {/* LOCATION SEARCH */}
          <div className="hidden md:flex items-center border rounded-full px-3 py-2 bg-white shadow-sm">
            <input
              value={location}
              onChange={(e) => setLocation(e.target.value)}
              onKeyDown={(e) => e.key === "Enter" && openMap()}
              placeholder="Search location"
              className="outline-none text-sm w-40"
            />
            <button
              onClick={openMap}
              className="text-indigo-600 hover:text-indigo-800 ml-2"
              title="Open in map"
            >
              <Globe size={18} />
            </button>
          </div>

          {/* LOGIN BUTTON */}
          <button
            className="
              flex items-center gap-2
              px-5 py-2
              rounded-full
              border border-indigo-500
              text-indigo-600
              font-medium
              hover:bg-indigo-50
              transition
            "
          >
            <User size={16} />
            Login
          </button>
        </div>
      </div>
    </nav>
  );
}

