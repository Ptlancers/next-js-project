"use client";
import InputWrapper from "@/app/components/InputWrapper";
import React, { FormEvent, useState, useEffect } from "react";
import DonationType from "./DonationType";
import ModeOfReceipt from "./ModeOfReceipt";
import Swal from "sweetalert2";
import Form from "@/app/components/Form";
import request from "@/app/lib/request";
import { numberToText } from "@/app/lib/utility";
import { useRouter, useSearchParams } from "next/navigation";
import { Receipt } from "@/app/main/lib/schema";
import { Suspense } from "react";

const MainForm = ({ defaultProps }: { defaultProps: Receipt }) => {
	const router = useRouter();
	const searchParams = useSearchParams();
	const [data, setData] = useState(defaultProps);
	const [button_text, setButtonText] = useState("create");
	const [update_receipt_number, setUpdateReceiptNumber] = useState("");

	useEffect(() => {
		request("http://localhost:8000/api/auth/token")
			.then((res) => {
				if (res.ok) {
					return res.json();
				}
				throw new Error(res.statusText);
			})
			.catch((error) => {
				router.push("/");
			});
	}, [router]);
	const createParams = (id: string) => {
		const params = new URLSearchParams(searchParams.toString());
		params.set("id", id);

		return params.toString();
	};
	const cleanUp = () => {
		setData({ ...defaultProps });
		setButtonText("create");
		setUpdateReceiptNumber("");
	};

	const handleClear = (event: React.MouseEvent<HTMLButtonElement>) => {
		event.preventDefault();
		cleanUp();
	};

	const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
		const { name, value } = e.target;
		setData((prev) => {
			if (name === "donated_amount") {
				if (value !== "") {
					for (let i = 0; i < value.length; i++) {
						if (isNaN(parseInt(value[i]))) {
							return { ...prev };
						}
					}
				}
				return {
					...prev,
					[name]: value,
					["donated_amount_letters"]: numberToText(value),
				};
			} else if (name === "receipt_number") {
				handleUpdate(value);
			}
			return { ...prev, [name]: value };
		});
	};

	const handleUpdate = (receipt_no: string) => {
		if (receipt_no === update_receipt_number) {
			setButtonText("update");
		} else {
			setButtonText("create");
		}
	};

	const handleSearch = (e: React.ChangeEvent<HTMLInputElement>): void => {
		const target = e.target as HTMLInputElement;
		const searchText = target.value;

		request(`http://localhost:8000/api/receipt/get-data/${searchText}`)
			.then((res) => {
				if (res.ok) {
					return res.json();
				}
				throw new Error(res.statusText);
			})
			.then((data) => {
				Swal.fire({
					title: "Data Found",
					text: "Do you want to update this data?",
					icon: "question",
					showCancelButton: true,
					confirmButtonText: "Yes",
					cancelButtonText: "Cancel",
					reverseButtons: true,
				}).then((result) => {
					if (result.isConfirmed) {
						setData(() => ({ ...data }));
						setButtonText("update");
						setUpdateReceiptNumber(data.receipt_number);
					} else {
						cleanUp();
					}
				});
			})
			.catch((error) => {
				console.error("Error:", error);
			});
	};
	const handlePrint = (id: string) => {
		Swal.fire({
			title: "Print Confirmation",
			text: "Do you want to print?",
			icon: "question",
			showCancelButton: true,
			confirmButtonText: "Print",
			cancelButtonText: "Cancel",
		}).then((result) => {
			if (result.isConfirmed) {
				router.push("/print?" + createParams(id));
			}
		});
	};
	const onSubmit = (
		event: FormEvent<HTMLFormElement>,
		callBackFunc: Function
	): void => {
		event.preventDefault();

		let url = "http://localhost:8000/api/receipt/insert-data";
		let method = "post";
		if (update_receipt_number) {
			url = `http://localhost:8000/api/receipt/update-data/${data["id"]}`;
			method = "put";
		}
		request(url, method, data)
			.then((res) => {
				if (res.ok) {
					return res.json();
				}
				throw new Error(res.statusText);
			})
			.then((res_data) => {
				(async () => {
					await Swal.fire({
						icon: "success",
						title: "success",
						text: res_data.detail,
						timer: 2000,
					});
				})();
				setTimeout(() => {
					handlePrint(res_data.id);
				}, 3000);
				callBackFunc();
			})
			.catch((error) => {
				Swal.fire({
					icon: "error",
					title: "Something Went wrong. Try again!",
					text: error.message,
				});
			});
	};

	const InputFields = [
		{
			name: "date",
			label: "Date",
			type: "date",
			value: data.date,
		},
		{
			name: "donor_registration_number",
			label: "Donor Registration Number",
			type: "text",
			value: data.donor_registration_number,
		},
		{
			name: "receipt_number",
			label: "Receipt Number",
			type: "text",
			value: data.receipt_number,
			onBlur: handleSearch,
		},
		{
			name: "donor_name",
			label: "Donor Name",
			type: "text",
			value: data.donor_name,
		},
		{
			name: "unique_identification_number",
			label: "Unique Identification Number",
			type: "text",
			value: data.unique_identification_number,
		},
		{
			name: "address",
			label: "Address",
			type: "text",
			value: data.address,
		},
		{
			name: "transaction_id",
			label: "Transaction Id",
			type: "text",
			value: data.transaction_id,
		},
		{
			name: "donated_amount",
			label: "Donated Amount",
			type: "text",
			value: data.donated_amount,
		},
		{
			name: "donated_amount_letters",
			label: "Donated Amount Letter",
			type: "text",
			disabled: true,
			value: data.donated_amount_letters,
		},
	];

	return (
		<Form
			onSubmit={(e: FormEvent<HTMLFormElement>) => {
				onSubmit(e, cleanUp);
			}}
		>
			<h1 className="mb-4 text-2xl font-semibold text-center">Receipt</h1>
			{InputFields.map((field_data, index) => {
				const { label, ...input_attribute } = field_data;
				return (
					<InputWrapper
						key={index}
						id={field_data.name}
						{...input_attribute}
						onChange={handleInputChange}
						placeholder={`Enter ${field_data.label}...`}
					>
						{label}
					</InputWrapper>
				);
			})}
			<DonationType
				value={data.donation_type}
				onChange={handleInputChange}
			></DonationType>
			<ModeOfReceipt
				value={data.mode_of_receipt}
				onChange={handleInputChange}
			></ModeOfReceipt>
			<div className="flex flex-row space-y-3 p-3 items-center justify-between">
				<button
					type="submit"
					className="bg-teal-500 hover:bg-teal-800 text-white font-semibold px-3 py-2 rounded-md shadow-sm shadow-black hover:shadow-none"
				>
					{button_text}
				</button>

				<button
					type="button"
					className="bg-red-500 hover:bg-red-800 text-white font-semibold px-3 py-2 rounded-md shadow-sm shadow-black hover:shadow-none"
					onClick={handleClear}
				>
					Cancel
				</button>
			</div>
		</Form>
	);
};

const SuspenseComponent = ({ defaultProps }: { defaultProps: Receipt }) => (
	<Suspense fallback={<div>Loading...</div>}>
		<MainForm defaultProps={defaultProps}></MainForm>
	</Suspense>
);
export default SuspenseComponent;
