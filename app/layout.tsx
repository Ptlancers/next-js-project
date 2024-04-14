import "./globals.css";
import type { Metadata } from "next";
export const metadata: Metadata = {
	title: "Sign In",
	description: "Sign In page for Receipt Application",
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
