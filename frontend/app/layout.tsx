import { Amita, Geist, Geist_Mono, Urbanist } from "next/font/google";
import { Noto_Sans_Devanagari } from "next/font/google"; // Add Noto Sans Devanagari
import "./globals.css";
import { Sidebar } from "./(components)/sidebar";
import ParticlesComponent from "@/components/particle";

const getUrbanist = Urbanist({
  variable: "--font-urbanist",
  subsets: ["latin"],
});

const getAmita = Amita({
  variable: "--font-amita",
  subsets: ["devanagari"],
  weight: "400", // or "700" depending on your preference
});

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${getUrbanist.variable} ${getAmita.variable} antialiased bg-neutral-900`}
      >
        <ParticlesComponent id="particles" />
        <div className="flex h-screen bg-black text-white">
          <Sidebar />
          {children}
        </div>
      </body>
    </html>
  );
}
