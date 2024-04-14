"use client";
import React, { FormEvent } from "react";
import Form from "./Form";
import request from "@/app/lib/request";
import { setToken } from "@/app/lib/token";
import { useRouter } from "next/navigation";
import Swal from "sweetalert2";
const LoginForm = ({ children }: { children: React.ReactNode }) => {
	const router = useRouter();
	async function onSubmit(event: FormEvent<HTMLFormElement>) {
		event.preventDefault();

		const formData = new FormData(event.currentTarget);
		const formDataJSON: { [key: string]: string } = {};

		formData.forEach((val, key) => {
			formDataJSON[key] = val.toString();
		});

		let field = null;
		if (!formDataJSON["username"]) {
			field = "username";
		} else if (
			!formDataJSON["section_code"] &&
			!formDataJSON["unique_registration_number"]
		) {
			if (!formDataJSON["section_code"]) {
				field = "Section Code";
			} else {
				field = "Unique Registration Number";
			}
		}
		if (field) {
			Swal.fire({
				icon: "info",
				title: "Input Required",
				text: `please fill the ${field} field`,
			});
			return;
		}

		await request(
			"http://localhost:8000/api/auth/sign-in",
			"post",
			formDataJSON
		)
			.then((res) => {
				if (res.ok) {
					return res.json();
				}
				throw new Error(res.statusText);
			})
			.then((data) => {
				setToken(data.access_token);
				Swal.fire({
					icon: "success",
					title: `Welcome ${formDataJSON["username"]}`,
					text: "Login Successful",
				});
				router.push("/main");
			})
			.catch((error) => {
				Swal.fire({
					icon: "error",
					title: error.message,
					text: "Invalid user credientials",
				});
			});
	}

	return <Form onSubmit={onSubmit}>{children}</Form>;
};

export default LoginForm;
