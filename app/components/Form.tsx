"use client";
import React from "react";

type FormProps = React.FormHTMLAttributes<HTMLFormElement>;

const Form: React.FC<FormProps> = ({ children, ...rest }) => {
	return (
		<form
			className={`w-full h-auto p-3 px-6 shadow-md shadow-black border-2 border-b-0 rounded-md`}
			autoComplete="false"
			{...rest}
		>
			{children}
		</form>
	);
};

export default Form;
