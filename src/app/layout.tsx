import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Paycheck by White Claw",
  description: "Stablecoin payroll with yield-powered advances for crypto-native teams. Built on Solana.",
  openGraph: {
    title: "Paycheck by White Claw",
    description: "Stablecoin payroll with yield-powered advances for crypto-native teams.",
    siteName: "Paycheck",
  },
  twitter: {
    card: "summary_large_image",
    site: "@whiteclawonsol",
    creator: "@whiteclawonsol",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
