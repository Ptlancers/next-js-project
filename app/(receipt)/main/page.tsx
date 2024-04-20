import Logout from "./components/Logout";
import MainForm from "./components/MainForm";
import type { Metadata } from "next";
import { getCurrentDate } from "@/app/lib/utility";
import { Receipt } from "./lib/schema";
export const metadata: Metadata = {
	title: "Receipt",
	description: "Receipt page for Receipt Application",
};

export default async function Page() {
	let defaultProps: Receipt = {
		id: "",
		date: getCurrentDate(),
		donor_registration_number: "",
		donor_name: "",
		receipt_number: "",
		unique_identification_number: "",
		address: "",
		transaction_id: "",
		donated_amount: "",
		donated_amount_letters: "",
		donation_type: "corpus",
		mode_of_receipt: "cash",
	};

	return (
		<main className="w-full h-[100vh-3rem]  overflow-y-auto flex flex-col items-center justify-center">
			<div className="w-[80vw] lg:w-[42vw] h-full flex-col items-center py-6">
				<MainForm defaultProps={defaultProps}></MainForm>
			</div>
		</main>
	);
}
