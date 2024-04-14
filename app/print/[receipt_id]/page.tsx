import PrinterComponent from "./components/PrinterComponent";
import { Receipt } from "@/app/main/lib/schema";
import request from "@/app/lib/request";

export async function generateStaticParams() {
	try {
		const data = await request("http://localhost:8000/api/receipt/all");
		const jsonData = await data.json();
		return jsonData.map((current: Receipt) => ({
			params: { receipt_id: current.id.toString() },
		}));
	} catch (error) {
		return [];
	}
}

const Page = async ({ params }: { params: { receipt_id: string } }) => {
	const printData: Receipt = await request(
		`http://localhost:8000/api/receipt/${params.receipt_id}`
	).then((res) => {
		return res.json();
	});
	const printLabels = Object.entries(printData).map(([key, value], index) => {
		const formattedKey =
			key.charAt(0).toUpperCase() + key.slice(1).replaceAll("_", " ");
		return (
			<div className={`${key}Wrapper p-1`} key={index}>
				<div id={key} className="flex flex-row text-xl">
					<label className="text-xl font-bold">{`${formattedKey} : `}</label>
					<span className="flex items-center justify-start w-auto text-xl border-b-2 border-black border-dotted">
						{value}
					</span>
				</div>
				{key === "date" && (
					<div className="w-screen h-20 text-2xl text-center muttName">
						<h1>
							Shri Sringari Sharatha Mutt
							<h2>Shengottai-627809</h2>
						</h1>
					</div>
				)}
			</div>
		);
	});

	return (
		<main className="w-screen h-screen overflow-x-hidden overflow-y-auto flex flex-col items-center justify-center p-3">
			<PrinterComponent>{printLabels}</PrinterComponent>
		</main>
	);
};

export default Page;
