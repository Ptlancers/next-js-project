import { getToken } from "@/app/lib/token";

const request = async (
	url: string,
	method: string = "GET",
	body: object | null = null
): Promise<Response> => {
	
	const config: RequestInit = {
		method: method,
		headers: {
			"Content-Type": "application/json",
			Authorization: `Bearer ${getToken()}`,
		},
	};

	if (body) {
		config.body = JSON.stringify(body);
	}

	return fetch(url, config);
};

export default request;

// const verifyToken = async (navigate, to = null, failed = null) => {
// 	const token = getToken();
// 	if (token === "") {
// 		return false;
// 	}
// 	getConfig.headers.Authorization = `bearer ${token}`;
// 	fetch(URL.token, getConfig)
// 		.then((res) => {
// 			if (res.status === 200) {
// 				if (to !== null) {
// 					navigate(to);
// 				}
// 			}
// 		})
// 		.catch((error) => {
// 			if (failed !== null) {
// 				navigate(failed);
// 			}
// 		});
// };
// export default verifyToken;
