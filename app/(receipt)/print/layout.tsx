// layout.tsx
import "@/app/globals.css";
import type { Metadata } from "next";
export const metadata: Metadata = {
    title: "Print Layout",
    description: "This application manage your Receipt",
};
export default function RootLayout({
    children,
}: {
    children: React.ReactNode;
}) {
    return (
        <html lang="en">
            <body className="w-screen h-screen overflow-hidden flex flex-col">
                {children}
            </body>
        </html>
    );
}
