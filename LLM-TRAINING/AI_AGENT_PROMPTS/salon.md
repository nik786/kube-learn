Master Prompt for Lovable

App Overview

App Name: Kapils Salon – AI Review Assistant

Goal:
Build a mobile-first, premium web app that helps customers of Kapils Salon generate authentic Google reviews in under 60 seconds and post them directly to the salon’s Google review page.

Core Flow:
User selects a few simple options → AI generates two review versions (Short + Detailed) → user can Copy or Post on Google → “Post” opens Google’s review popup using the salon’s placeid.

The experience must feel branded, effortless, fast, and trustworthy.

0) Inputs You Will Receive (Injected by User)
Brand Details

Salon Name: Kapils Salon

Tagline: India’s Most Trusted Hair & Beauty Salon Chain

City / Locality: Mumbai

Services (comma-separated):
Haircut, Hair Styling, Hair Color, Hair Spa, Keratin Treatment, Smoothening, Bridal Makeup, Party Makeup, Facial, Cleanup, Manicure, Pedicure, Grooming

Unique Strengths (comma-separated):
Expert stylists, premium salon experience, hygiene & safety standards, personalized consultation, latest techniques, professional products

Brand Assets

Logo:
https://www.kapilssalon.com/wp-content/uploads/2022/03/kapils-salon-logo.png

Primary Color: #C4161C

Secondary Color: #000000

Accent Gradient: Red → Black

Google Review URL (placeid)
https://search.google.com/local/writereview?placeid=ChIJAQW1d_i25zsRcNzTHA9pxBs

AI Provider

Provider: OpenAI

Model: GPT-4.1 mini
API :
1) App & Tech Requirements

Type: Responsive web app (PWA-ready)

Design: Mobile-first

Tech Preference:
React + TypeScript + Tailwind (or Lovable UI blocks)

App States

Form Input

Generating Reviews (animated loader)

Results Screen (Short + Detailed reviews)

2) Header & Branding

Left: Kapils Salon logo (48px height, rounded)

Right: Small badge → “Powered by AI”

Title: Kapils Salon Review Assistant

Subtext: Write a genuine review in under 60 seconds

Theme

Headings & CTAs: #C4161C

Accents: #000000

Soft gradients (red → black) for loader and result cards

3) Stats Bar (Credibility Section)

Display 3–4 compact chips under the header (icons optional):

Customers served: 1000+

Avg rating: 4.8 / 5

Top services: Haircut, Hair Color, Styling

Hygiene & safety focused

4) Review Form

All fields required unless marked optional.

Required Dropdowns

Visit Type:
Haircut, Hair Color, Keratin/Smoothing, Facial/Cleanup,
Manicure/Pedicure, Styling/Makeover, Other

Experience Tone:
Professional, Friendly, Fun & Stylish, Practical & Time-Saving,
Relaxing & Pampering, Inspirational

Who Are You?
Student, Working Professional, Entrepreneur, Homemaker, Freelancer, Other

Why You Chose Kapils Salon?
Nearby location, Good reviews, Clean & hygienic, Skilled staff,
Value for money, Recommendation

What You Liked Most?
Expert stylists, Service quality, Cleanliness, Pricing,
Staff behavior, Ambience, Timeliness

Impact / Outcome:
Boosted confidence, Loved the hairstyle, Time saved,
Great value, Perfect for an event

Optional Fields

Staff / Stylist Name (text)

Additional Notes (10–30 words)

UX Notes

Primary CTA: “Generate My Reviews”
(disabled until required fields are selected)

Helper text below CTA:
“Keep it honest — this tool just helps you express it better.”

5) Review Generation Rules (Critical)
Output

Generate two reviews per request:

SHORT REVIEW

1–2 sentences

Natural, concise

India-friendly tone

DETAILED REVIEW

3–5 sentences

Mentions:

Service type

Experience tone

Specific likes

Outcome / impact

Staff name (only if provided)

Authenticity Constraints

No fake claims

No exaggerated superlatives

No invented details

Sounds like a real customer from India

Honest, polite, human

Variety & Style

Light randomness on regeneration

Rotate openings (e.g., “I visited…”, “Booked…”, “Tried…”)

Simple English

5-star tone without sounding fake

Internal System Prompt (Compose Automatically)
You are an assistant helping a real customer of Kapils Salon in Mumbai
write an authentic Google review.

Use the user’s selections to generate naturally worded reviews that
mention the service, experience tone, specific likes, and outcome.

Keep the tone honest, India-friendly, and concise.
Avoid exaggeration. Never invent facts.

Return two versions:
SHORT (1–2 sentences)
DETAILED (3–5 sentences)

6) Results Screen

Display two review cards:

Each Card Includes

Title: SHORT REVIEW / DETAILED REVIEW

⭐⭐⭐⭐⭐ icons

Review text

Buttons:

Copy (clipboard)

Post on Google

Post on Google Behavior

Copy review text automatically

Open new tab:

https://search.google.com/local/writereview?placeid=ChIJAQW1d_i25zsRcNzTHA9pxBs

Mini Guide Below Buttons

Tap “Post on Google”

Select stars (your choice)

Paste review → Submit

Extra

Generate New button to reset form

7) Errors & Edge Cases

API failure:
“Couldn’t generate right now. Please try again.”

Missing fields: gentle validation

Generic output hint:
“Try adding 1–2 personal details for a better result.”

8) Privacy & Ethics (Footer)

“Your words are your own.
This tool only helps you express your experience clearly.
Please post honest feedback.”

9) Admin / Brand Controls (Hidden)

Accessible via:

?admin=1 URL param or hotkey

Admin can edit:

Google Place ID

Logo

Brand colors

Tagline

Services list

Default tones

Post-link preview text

10) Performance & Polish

Fast load

Skeleton loaders

Subtle motion (ease-out)

High contrast & accessibility

Large tap targets

Save last inputs (localStorage)

Toast feedback: “Copied!”

11) Monetization (Optional / White-Label)

Optional footer text:
“Powered by Future Agents”

Toggle ON/OFF

Optional CTA:
“Create this for your business”
→ mailto:contact@futureagents.in
