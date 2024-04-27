import numberToWords from "number-to-words";

export const getCurrentDate = () => {
	const currentDate = new Date();
	const year = currentDate.getFullYear();
	const month = `${currentDate.getMonth() + 1}`.padStart(2, "0");
	const day = `${currentDate.getDate()}`.padStart(2, "0");
	return `${year}-${month}-${day}`;
	
};

export const numberToText = (value: string) => {
	try {
		return numberToWords.toWords(value);
	} catch (error) {
		return "";
	}
};
