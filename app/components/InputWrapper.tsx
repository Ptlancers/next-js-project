"use client";
import { useState } from "react";

type InputProps = React.InputHTMLAttributes<HTMLInputElement>;

const InputWrapper: React.FC<InputProps> = ({ children, ...props }) => {
	return (
		<div className="w-full p-2 flex items-center justify-between">
			<label
				className="w-1/2 block text-sm font-medium text-gray-700"
				htmlFor={props.id}
			>
				{children}
			</label>
			<input
				className="placeholder:text-sm h-10 px-4 w-1/2 border-2 border-gray-300 rounded-md focus:outline-gray-600"
				{...props}
			/>
		</div>
	);
};

export default InputWrapper;
