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
	return <>{children}</>;
}
