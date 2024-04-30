"use client";
import React from "react";
import RadioButton from "./RadioButton";

interface ContentData {
	id: string;
	value: string;
}
interface RadioGroupAttribute {
	content_data: Array<ContentData>;
	name: string;
	value: string;
	onChange: React.ChangeEventHandler<HTMLInputElement>;
}
const RadioGroup = (props: RadioGroupAttribute) => {
	return (
		<>
			{props.content_data.map((field_data, index) => {
				
				return (
					<RadioButton
						key={index}
						id={field_data.id}
						value={field_data.value}
						name={props.name}
						isChecked={field_data.value === props.value}
						onChange={props.onChange}
					>
						{field_data.value}
					</RadioButton>
				);
			})}
		</>
	);
};

export default RadioGroup;
