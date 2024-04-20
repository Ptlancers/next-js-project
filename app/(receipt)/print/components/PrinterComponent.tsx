"use client";
import React, { useEffect, useRef, useState, Suspense } from "react";
import { useReactToPrint } from "react-to-print";
import { useSearchParams, useRouter } from "next/navigation";
import request from "@/app/lib/request";
interface PrintData {
	[key: string]: string;
}

const PrinterComponent = () => {
	const componentRef = useRef<HTMLDivElement>(null);
	const [printData, setPrintData] = useState<PrintData | null>(null);
	const router = useRouter();
	const searchParams = useSearchParams();
	const id: string | null = searchParams.get("id");

	const printLabels = printData
		? Object.entries(printData).map(([key, value], index) => {
				const formattedKey =
					key.charAt(0).toUpperCase() +
					key.slice(1).replace("_", " ");
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
		  })
		: null;

	const handlePrint = useReactToPrint({
		content: () => componentRef.current!,
		onAfterPrint: () => {
			router.push("/main");
		},
	});

	const fetchData = async (id: string) => {
		try {
			const response = await request(
				`http://localhost:8000/api/receipt/get-by-id/${id}`
			).then((res) => res.json());
			setPrintData(response);
		} catch (error) {
			console.error("Error fetching data:", error);
		}
	};

	useEffect(() => {
		if (id) {
			fetchData(id);
		}
	}, [id]);

	useEffect(() => {
		if (printData) {
			handlePrint();
		}
	}, [handlePrint, printData]);

	return (
		<div className="printer-component">
			<div ref={componentRef}>{printLabels}</div>
		</div>
	);
};

const SuspenseComponent = () => (
	<Suspense fallback={<div>Loading...</div>}>
		<PrinterComponent></PrinterComponent>
	</Suspense>
);
export default SuspenseComponent;
