import Cookies from "js-cookie";

// Function to set a token in a cookie with an expiry of 7 days
export const setToken = (token: string): void => {
	Cookies.set("token", token, { expires: 7 });
};

// Function to get the token from the cookie
export const getToken = (): string | undefined => {
	return Cookies.get("token");
};

// Function to remove the token from the cookie
export const removeToken = (): void => {
	Cookies.remove("token");
};
