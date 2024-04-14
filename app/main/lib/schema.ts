interface Receipt {
	id: string;
	date: string;
	donor_registration_number: string;
	receipt_number: string;
	donar_name: string;
	unique_identification_number: string;
	address: string;
	transaction_id: string;
	donated_amount: string;
	donated_amount_letters: string;
	donation_type: string;
	mode_of_receipt: string;
}
export type { Receipt };
