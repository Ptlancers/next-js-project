"use client";
import React from "react";

import { useRouter } from "next/navigation";
import { removeToken } from "@/app/lib/token";
const Logout = () => {
	const router = useRouter();
	const handleClick = (e: React.MouseEvent<HTMLButtonElement>) => {
		e.preventDefault();
		removeToken();
		router.push("/");
	};
	return (
		<button
			onClick={handleClick}
			type="submit"
			className="bg-teal-500 hover:bg-teal-800 text-white font-semibold px-3 py-2 rounded-md shadow-sm shadow-black hover:shadow-none absolute right-3 top-2"
		>
			Logout
		</button>
	);
};

export default Logout;
