const Page = () => {
	return (
		<main className="w-screen h-screen overflow-x-hidden overflow-y-auto flex flex-col items-center justify-center p-3">
			
			<div className="w-full h-auto outline-2 p-3 flex flex-col justify-center gap-4 items-center ">
				<div className="row1 flex flex-col justify-center items-center">
					<h1 className="text-2xl font-bold ">
						SENGOTTAI SRI SHARADAMBA CHARITABLE TRUST
					</h1>
					<h5 className=" text-base font-semibold ">No.9,Premier Chambers,Tenkasi Road ,Sengottai-627809</h5>
				</div>
				<div className="row2 w-full  flex flex-row justify-around items-center">
					<div id="Date">
						<label id="LableDate">Date : </label> <label htmlFor="LabelDate" className="w-auto border-b-4 border-dotted border-black" >25/apr/2024</label>
					</div>
					<h2 className="text-lg font-semibold">Receipt</h2>
					<div id="Rno">
						<label id="Rno">Receipt Number </label> <label htmlFor="Rno" className="w-auto border-b-4 border-dotted border-black">1234</label>
					</div>
				</div>
				<div className="RowWrappwe1 w-full flex flex-row">
					<div className="row3 w-full  flex flex-row justify-start items-center">
						<div id="name">
							<label id="Name">Name : </label> <label htmlFor="Name" className="w-auto border-b-4 border-dotted border-black" >Padmanabhan.S</label>
						</div>
					
					</div>
					<div className="row4 w-full  flex flex-row justify-start items-center">
						<div id="URN">
							<label id="URNlabel">URN :  </label> <label htmlFor="URNlabel" className="w-auto border-b-4 border-dotted border-black">1234</label>
						</div>
					</div>
				</div>
				<div className="row5 w-full  flex flex-row justify-start items-center">
					<div id="Address" className="flex w-auto gap-2">
							<label htmlFor="Address"> Address : </label>
						<address className="flex h-auto w-auto flex-col w-auto border-b-4 border-dotted border-black">
							28,Sannathi Street,							
							Courtallam-627802
						</address>
					</div>
				</div>
				<div className="RowWrapper2 flex w-full h-auto flex-row">
					<div className="row6 w-full  flex flex-row justify-start items-center">
						<div id="Donated_Amount">
							<label id="Donated_Amountlabel">Donated Amount : </label> <label htmlFor="Donated_Amountlabel" className="w-auto border-b-4 border-dotted border-black">1234</label>
						</div>
					</div>
					<div className="row7 w-full  flex flex-row justify-start items-center">
						<div id="Donated_AmountLetters">
							<label id="Donated_Amountletterlabel">Donated Amount in letters  : </label> <label htmlFor="Donated_Amountletterlabel" className="w-auto border-b-4 border-dotted border-black">one thousand and  two hundread and thirty four</label>
						</div>
					</div>
				</div>
				<div className="RowWrapper3 flex flex-row w-full h-auto">
					<div className="row8 w-full  flex flex-row justify-start items-center">
						<div id="Transaction_Id">
							<label id="Transaction_IDlabel"> Transaction Id : </label> <label htmlFor="Transaction_IDlabel" className="w-auto border-b-4 border-dotted border-black">1234</label>
						</div>
					</div>
					<div className="row9 w-full  flex flex-row justify-start items-center">
						<div id="Transaction_towards">
							<label id="Towrdslabel"> Towards : </label> <label htmlFor="Transaction_IDlabel" className="w-auto border-b-4 border-dotted border-black">corpose</label>
						</div>
					</div>
				</div>			<div className="row10 w-full   flex flex-row justify-between items-center">
					<div id="Trust details " className="h-auto border-black border-4 rounded-md p-2">
						<div><label id="LableDate">Pan No: </label> <label htmlFor="LabelDate" className="w-auto" >AAUTS9053P</label></div>
						<div><p>
							Donations Exempt u/s 80G of the IT act 1961 <br></br>
							Provisional Approval Number AAUTS9053PF20214 <b>Dated : </b> 31/05/2021
						</p>
						||- Clause (|) of first proviso to Sub-Section(5) of section80G
						</div>
					</div>

					<div id="signature">
						<div className="flex flex-col justify-center items-center h-auto w-auto ">
							<label id="signature">
							For <b>Sengottai Sri Sharadamba Charitable Trust</b></label>
							<br></br>
							<br></br>
							<br></br>
							<br></br>
							<label htmlFor="signature">Trustee/Treasurer</label>
						</div>
					</div>
				</div>

			</div>
		</main>
	);
};

export default Page;
