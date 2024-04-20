"use client";

import { NextPage } from "next";
import { useState, useEffect } from "react";
import { usePathname, useRouter } from "next/navigation";
import Link from "next/link";
import request from "@/app/lib/request";
import { removeToken } from "@/app/lib/token";
interface Props {}

const Header: NextPage<Props> = ({}) => {
	const [button_text, setButtonText] = useState("Sign Up");
	const [navigate_link, setNavigateLink] = useState("/sign-up");
	const pathname = usePathname();
	const router = useRouter();
	useEffect(() => {
		(async () => {
			await request("http://localhost:8000/api/auth/token")
				.then((res) => {
					if (res.ok) {
						router.push("/main");
						return true;
					}
					throw new Error();
				})
				.catch(() => {
					if (pathname === "/main") {
						router.push("/");
					}
				});
		})();

		if (pathname === "/") {
			setButtonText("Sign Up");
			setNavigateLink("/sign-up");
		} else if (pathname === "/sign-up") {
			setButtonText("Sign In");
			setNavigateLink("/");
		} else if (pathname === "/main") {
			setButtonText("Logout");
			setNavigateLink("/");
		}
	}, [pathname, router]);
	return (
		<header className="w-full h-[3rem] px-5 flex justify-between items-center bg-gray-700 text-white">
			<h1 className="font-semibold tracking-wider cursor-pointer hover:text-rose-500">
				Receipt App
			</h1>
			<Link
				href={navigate_link}
				className={`rounded-md text-white font-semibold underline underline-offset-2 hover:text-rose-500 ${
					pathname === "/main" &&
					"bg-red-500 no-underline px-2 p-0.5 hover:bg-red-800 hover:text-white"
				}`}
				onClick={() => {
					if (pathname === "/main") {
						removeToken();
					}
				}}
			>
				{button_text}
			</Link>
		</header>
	);
};

export default Header;
