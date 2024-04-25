import "./globals.css";
import type { Metadata } from "next";
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
				{children}
			</body>
		</html>
	);
}
