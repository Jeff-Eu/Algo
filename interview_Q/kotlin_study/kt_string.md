## Kotlin String
// 假設 c 是一個 Char，而 s 是一個字串
* 字串<->int
    * 字串轉int => `s.toInt()`, `c.toString().toInt()`
		* 補充：[Convert a string to an integer in Kotlin](https://www.techiedelight.com/convert-string-to-integer-kotlin/)
    * int轉字串 => `n.toString()`
		* 補充：[Convert an integer to a string in Kotlin](https://www.techiedelight.com/convert-integer-to-string-kotlin/)
* 字元<->數字
    * 字元轉ASCII數字 `c.toInt()`, `s[2].toInt()`
    * ASCII數字轉字元 `65.toChar()`  // 秘技：在 Android Studio中，數字要加括號，dot下去才會跳出提示 e.g. `(65).toChar()`