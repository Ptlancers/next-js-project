"use client";
import { useRouter } from "next/navigation";
import React, { useEffect, useRef } from "react";
import { useReactToPrint } from "react-to-print";

interface PrinterComponentProps {
	children: React.ReactNode;
}

const PrinterComponent: React.FC<PrinterComponentProps> = ({ children }) => {
	const router = useRouter();
	const componentRef = useRef<HTMLDivElement>(null);

	const handlePrint = useReactToPrint({
		content: () => componentRef.current,
		onAfterPrint: () => router.push("/main"),
	});

	useEffect(() => {
		handlePrint();
	}, [handlePrint]);

	return (
		<div style={{ display: "none" }}>
			<div ref={componentRef}>{children}</div>
		</div>
	);
};

export default PrinterComponent;
