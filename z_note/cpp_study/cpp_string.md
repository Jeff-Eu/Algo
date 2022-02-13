# C++ String

* int to string => `std::to_string(168)`
	* 使用在 [[572_Subtree of Another Tree]]

* 找子字串 => find 回傳 index；或是找不到則回傳 `std::string::npos`
	* 範例 `s1.find(s2) != std::string::npos` (使用在 [[572_Subtree of Another Tree]])
	* 說明 `string::npos`: https://www.cplusplus.com/reference/string/string/npos/