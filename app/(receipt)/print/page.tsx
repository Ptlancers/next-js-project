import PrinterComponent from "./components/PrinterComponent";
const Page = () => {
	return (
		<main className="w-screen h-screen overflow-x-hidden overflow-y-auto flex flex-col items-center justify-center p-3">
			{<PrinterComponent />}
		</main>
	);
};

export default Page;
