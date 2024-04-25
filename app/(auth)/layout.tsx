import "./globals.css";
import type { Metadata } from "next";
import Header from "@/app/(auth)/components/Header"
export const metadata: Metadata = {
	title: "Receipt Application",
	description: "This application manage your Receipt",
};
export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<>
			<Header></Header>
			{children}
		</>
	);
}
