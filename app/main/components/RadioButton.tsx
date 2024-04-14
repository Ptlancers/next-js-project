type InputProps = React.InputHTMLAttributes<HTMLInputElement> & {
	isChecked: boolean;
};

const RadioButton: React.FC<InputProps> = ({ children, ...props }) => {
	return (
		<div className="mb-0">
			<input
				type="radio"
				id={props.id}
				name={props.name}
				value={props.value}
				className="sr-only"
				onChange={props.onChange}
			/>
			<label
				htmlFor={props.id}
				className={`text-center text-sm font-semibold cursor-pointer inline-block px-3 py-2 rounded border border-gray-300 text-gray-700 hover:border-gray-800 ${
					props.isChecked
						? "shadow-none border-2 border-black"
						: "shadow-sm shadow-black"
				}`}
			>
				{children}
			</label>
		</div>
	);
};

export default RadioButton;
