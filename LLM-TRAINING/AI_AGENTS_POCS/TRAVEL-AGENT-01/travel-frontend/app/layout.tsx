import "../globals.css";
import Navbar from "@/components/Navbar";

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className="h-screen bg-[#f7f7f8]">
        <Navbar />

        {/* Offset for fixed navbar */}
        <main className="pt-[72px] h-[calc(100vh-72px)]">
          {children}
        </main>
      </body>
    </html>
  );
}

