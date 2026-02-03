import Chatbot from "@/components/Chatbot";


export default function Home() {
return (
<main className="relative">
{/* Navbar */}
<nav className="fixed top-0 w-full bg-white shadow z-50">
<div className="max-w-7xl mx-auto flex justify-between items-center p-4">
<h1 className="text-xl font-bold">AI Solutions</h1>
<ul className="flex gap-6 font-medium">
<li>Services</li>
<li>Industries</li>
<li>Support</li>
<li>Blog</li>
<li>Contact Us</li>
</ul>
</div>
</nav>


{/* Hero */}
<section className="pt-24 bg-gradient-to-r from-indigo-600 to-purple-600 text-white">
<div className="max-w-7xl mx-auto grid md:grid-cols-2 gap-8 p-8">
<div>

<h2 className="text-4xl font-bold mb-4">Build Intelligent Experiences</h2>
<p className="mb-6">AI powered solutions for cloud, DevOps, and enterprises.</p>
<button className="bg-white text-indigo-600 px-6 py-2 rounded">Get Started</button>
</div>
<img
src="https://images.pexels.com/photos/3861969/pexels-photo-3861969.jpeg"
className="rounded-lg shadow"
alt="AI"
/>
</div>
</section>


{/* Services */}
<section className="max-w-7xl mx-auto p-8">
<h3 className="text-3xl font-bold mb-6">Services</h3>
<div className="grid md:grid-cols-3 gap-6">
{['AI Chatbots', 'Cloud DevOps', 'Observability'].map(s => (
<div key={s} className="bg-white p-6 rounded shadow">
<h4 className="font-semibold text-xl mb-2">{s}</h4>
<p>Enterprise‑grade solutions with scalability and security.</p>
</div>
))}
</div>
</section>



{/* Industries */}
<section className="bg-gray-100 p-8">
<div className="max-w-7xl mx-auto">
<h3 className="text-3xl font-bold mb-6">Industries</h3>
<div className="grid md:grid-cols-4 gap-4">
{['Finance', 'Healthcare', 'Retail', 'IT Services'].map(i => (
<div key={i} className="bg-white p-4 rounded shadow text-center">{i}</div>
))}
</div>
</div>
</section>


{/* Footer */}
<footer className="bg-gray-900 text-white p-6 text-center">
© 2025 AI Solutions. All rights reserved.
</footer>


{/* Chatbot */}
<Chatbot />
</main>
);
}



