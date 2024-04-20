import "./globals.css";
import type { Metadata } from "next";
export const metadata: Metadata = {
	title: "Print Page",
	description: "This application manage your Receipt",
};

export default function RootLayout({
	children,
}: {
	children: React.ReactNode;
}) {
	return (
		<html lang="en">
			<body>{children}</body>
		</html>
	);
}
