# Kotlin Flow Control

* From https://kotlinlang.org/docs/ranges.html
	```java kotlin
	for (i in 1..8 step 2) print(i)
	// output: 1357
	println()
	for (i in 8 downTo 1 step 2) print(i)
	// output: 8642
	```

* To iterate a number range which does not include its end element, use the until function:
	```java kotlin
	for (i in 1 until 10) {  // i in [1, 10), 10 is excluded
		print(i)
	}
	// output: 123456789
	```