import "./globals.css";
import type { Metadata } from "next";
import Header from "./components/Header";
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
		<html lang="en">
			<body className="w-screen h-screen overflow-hidden flex flex-col">
				<Header></Header>
				{children}
			</body>
		</html>
	);
}
