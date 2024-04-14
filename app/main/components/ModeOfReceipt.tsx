import React from "react";
import RadioGroup from "./RadioGroup";
const ModeOfReceipt = ({
	value,
	onChange,
}: {
	value: string;
	onChange: React.ChangeEventHandler<HTMLInputElement>;
}) => {
	let content_data = [
		{ id: "cash", value: "cash" },
		{ id: "digital", value: "digital" },
		{ id: "cheque", value: "cheque" },
	];
	return (
		<div className="w-full p-2 flex items-center justify-between">
			<label className="w-1/2 block text-sm font-medium text-gray-700">
				Mode Of Receipt
			</label>
			<div className="w-1/2 py-2 space-x-2 flex justify-evenly">
				<RadioGroup
					value={value}
					content_data={content_data}
					name={"mode_of_receipt"}
					onChange={onChange}
				/>
			</div>
		</div>
	);
};

export default ModeOfReceipt;
