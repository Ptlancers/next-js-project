"use client";
import React, { FormEvent } from "react";
import Form from "@/app/components/Form";
import Swal from "sweetalert2";
import request from "@/app/lib/request";
import { setToken } from "@/app/lib/token";
import { useRouter } from "next/navigation";
const SignUpForm = ({ children }: { children: React.ReactNode }) => {
	const router = useRouter();
	async function onSubmit(event: FormEvent<HTMLFormElement>) {
		event.preventDefault();

		const formData = new FormData(event.currentTarget);
		const formDataJSON: { [key: string]: string } = {};

		formData.forEach((val, key) => {
			formDataJSON[key] = val.toString();
		});

		for (let key in formDataJSON) {
			if (!formDataJSON[key]) {
				Swal.fire({
					icon: "info",
					title: "Input Required",
					text: `please fill the ${key} field`,
				});
				return;
			}
		}

		await request(
			"http://localhost:8000/api/auth/sign-up",
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
					text: "Created Successful",
				});
				router.push("/main");
			})
			.catch((error) => {
				Swal.fire({
					icon: "error",
					title: error.message,
					text: "Fail to create user",
				});
			});
	}

	return <Form onSubmit={onSubmit}>{children}</Form>;
};

export default SignUpForm;
