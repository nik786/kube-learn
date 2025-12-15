MASTER PROMPT for Lovable
App Name: Kapils Salon – AI Review Assistant
Goal: Create a mobile-first web app that helps Kapils Salon generate authentic Google reviews in seconds and post them directly to Apple’s Google review page. The app must be simple, fast, and trustworthy: the user selects a few options → AI generates two review versions (Short + Detailed) → with Copy and Post buttons → “Post” opens Apple’s Google review popup (placeid). The app should feel branded, premium, and effortless.

0) Inputs You’ll Receive (I will paste these)
Brand details:
Salon Name: Kapils Salon
Tagline: India’s Most Trusted Hair & Beauty Salon Chain
City/Locality: Mumbai
Services (comma-separated): Haircut, Hair Styling, Hair Color, Hair Spa, Keratin Treatment, Smoothening, Bridal Makeup, Party Makeup, Facial, Cleanup, Manicure, Pedicure, Grooming
Unique strengths (comma-separated): expert stylists, premium salon experience, hygiene & safety standards, personalized consultation, latest techniques, professional products

Brand assets:
Logo file: https://www.kapilssalon.com/wp-content/uploads/2022/03/kapils-salon-logo.png
Primary color: #C4161C
Secondary color: #000000
Accent gradient: red→black

Google Review URL (placeid link):
 https://search.google.com/local/writereview?placeid=ChIJAQW1d_i25zsRcNzTHA9pxBs

API choice & key: OpenAI or Gemini
Provider: OpenAI
API : 
Model: GPT 4.1 mini

1) Build a responsive web app (PWA-ready)
Tech: Use React + TypeScript + Tailwind (internally) or the platform’s UI blocks.
States:
Form Input
 Generating Reviews (animated loader)
 Results (SHORT + DETAILED review cards)
Mobile-first with clean spacing, large tap targets, and clear CTAs.

2) Header & Branding
Left: Kapils Salon logo (48px height, rounded), Right: small badge “Powered by AI”.
Title: “Kapils Salon Review Assistant”
Subtext: “Write a genuine review in under 60 seconds.”
Theme: use #C4161C for headings/CTAs, #000000 for accents, soft gradient backgrounds (red→black) on results and loader.

3) Stats Bar (credibility)
Show 3–4 compact chips under the header (icons ok):
“Customers served: 1000+”
 “Avg rating: 4.8/5”
 “Top services: Haircut, Hair Color, Styling”
 “Hygiene & safety focused”

4) Review Form (required dropdowns + optional notes)
All fields required unless marked optional.
Visit Type: Haircut, Hair Color, Keratin/Smoothing, Facial/Cleanup, Manicure/Pedicure, Styling/Makeover, Other
Experience Tone: Professional, Friendly, Fun & Stylish, Practical & Time-Saving, Relaxing & Pampering, Inspirational
Who Are You? Student, Working Professional, Entrepreneur, Homemaker, Freelancer, Other
Why You Chose Kapils Salon? Nearby location, Good reviews, Clean & hygienic, Skilled staff, Value for money, Recommendation
What You Liked Most? Expert stylists, Service quality, Cleanliness, Pricing, Staff behavior, Ambience, Timeliness
Impact/Outcome: Boosted confidence, Loved the hairstyle, Time saved, Great value, Perfect for an event
Staff/Stylist (optional text):
Additional Notes (optional 10–30 words): free text
Primary CTA: “Generate My Reviews” (disabled until required fields chosen)
UX: Show small hint text: “Keep it honest—this tool just helps you express it better.”

5) Generation Rules (very important)
Create two reviews per request:
SHORT REVIEW (1–2 sentences): concise, natural, India-friendly tone.
DETAILED REVIEW (3–5 sentences): specific, warm, mentions service and impact, optional staff name if provided.
Authenticity constraints:
No false claims, no superlatives stacking (“best best ever”), avoid hype.
 Never fabricate facts not hinted by inputs.
 Encourage honesty; sound like a real person from India.
Variety & uniqueness:
Use light randomness; vary structure/wording if user regenerates.
 Avoid repetitive openings; rotate intros (“I visited…”, “Tried…”, “Booked…”)
Style: Simple English, polite, culturally neutral, 5-star tone but not fake.
System Prompt to LLM (compose internally using form data):
“You are an assistant helping a real customer of Kapils Salon in Mumbai write an authentic Google review.
 Use the user’s selections to produce naturally worded reviews that mention service type, experience tone, specific likes, and impact.
 Keep it honest, India-friendly, and concise. Avoid exaggeration, avoid promises, and never invent details.
 Return two versions: SHORT (1–2 sentences) and DETAILED (3–5 sentences).”

6) Results Screen
Two cards: SHORT REVIEW and DETAILED REVIEW
Each shows 5-star icons, the review text, and two buttons:
Copy → copies review to clipboard
Post on Google → copies text then opens new tab to:
 https://search.google.com/local/writereview?placeid=**ChIJAQW1d_i25zsRcNzTHA9pxBs**
How to Post mini-guide under buttons:
Tap “Post on Google”
 Select stars (we suggest the rating you feel is right)
 Paste your review → Submit
Generate New button to reset the form.

7) Error & Edge Cases
If API fails: show friendly message: “Couldn’t generate right now. Please try again.”
Validate dropdowns; mark missing fields gently.
If review seems too generic, show “Try adding 1–2 personal details for a better result.”

8) Privacy & Ethics note (footer)
“Your words are your own. This tool only helps you express your experience clearly. Please post honest feedback.”

9) Admin/Brand Controls (simple)
Hidden panel toggle (hotkey or URL param ?admin=1) to change:
Google Place ID, logo, brand colors, tagline, top services list
 Default tone/visit options (add/remove)
 Post link preview text

10) Performance & Polish
Fast initial load, skeleton loaders, subtle motion (ease-out).
 Accessible labels/aria, large buttons, high contrast with #C4161C.
 Save last inputs locally to speed re-generation (localStorage).
 Add small toast “Copied!” feedback.

11) Monetization (optional for white-label)
Show “Powered by Future Agents” with a tiny link; allow toggling off.
If enabled, add “Create this for your business” → opens mailto:contact@futureagents.in.
