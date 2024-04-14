import React from "react";
import RadioGroup from "./RadioGroup";
const DonationType = ({
	value,
	onChange,
}: {
	value: string;
	onChange: React.ChangeEventHandler<HTMLInputElement>;
}) => {
	let content_data = [
		{ id: "corpus", value: "corpus" },
		{ id: "others", value: "others" },
	];
	return (
		<div className="w-full p-2 flex items-center justify-between">
			<label
				className="w-1/2 block text-sm font-medium text-gray-700"
				htmlFor={"donation_type"}
			>
				Donation Type
			</label>
			<div className="w-1/2 py-2 flex justify-evenly">
				<RadioGroup
					content_data={content_data}
					name={"donation_type"}
					value={value}
					onChange={onChange}
				/>
			</div>
		</div>
	);
};

export default DonationType;
