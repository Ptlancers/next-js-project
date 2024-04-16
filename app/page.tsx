import Link from "next/link";
import InputWrapper from "./components/InputWrapper";
import LoginForm from "./components/LoginForm";
export default function Home() {
	const InputFields = [
		{
			name: "username",
			label: "Username",
			type: "text",
		},
		{
			name: "section_code",
			label: "Section Code",
			type: "text",
		},
		{
			name: "unique_registration_number",
			label: "Unique Registration Number",
			type: "text",
		},
	];

	return (
		<main className="w-screen h-screen overflow-x-hidden overflow-y-auto flex flex-col items-center justify-center p-3">
			<div className="w-[80vw] lg:w-[42vw] h-auto flex-col items-center">
				<LoginForm>
					<h1 className="mb-4 text-2xl font-semibold text-center">
						Sign In
					</h1>
					{InputFields.map((field_data, index) => {
						return (
							<InputWrapper
								key={index}
								id={field_data.name}
								name={field_data.name}
								type={field_data.type}
								placeholder={`Enter ${field_data.label}...`}
							>
								{field_data.label}
							</InputWrapper>
						);
					})}

					<div className="flex flex-col space-y-3 p-3 items-center justify-center">
						<p>
							Dont have an account?{" "}
							<Link
								href="/sign-up"
								className="text-sky-800 hover:underline font-semibold cursor-pointer hover:text-sky-500"
							>
								Sign Up here
							</Link>
						</p>
						<button
							type="submit"
							className="bg-teal-500 hover:bg-teal-800 text-white font-semibold px-3 py-2 rounded-md shadow-sm shadow-black hover:shadow-none"
						>
							Login
						</button>
					</div>
				</LoginForm>
			</div>
		</main>
	);
}
