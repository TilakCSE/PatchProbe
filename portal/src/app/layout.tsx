import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "PatchProbe — Release note triage",
  description: "A research MVP that suggests the first area to verify after a software upgrade.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="en"><body>{children}</body></html>;
}

