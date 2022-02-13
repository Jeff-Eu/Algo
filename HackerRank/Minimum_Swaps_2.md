# Minimum Swaps 2
Q: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?isFullScreen=true

## Answer
The best explanation I found so far is from the Youtuber - [HackerRank Interview Prep Kit - Problem 8: Minimum Swaps 2](https://www.youtube.com/watch?v=mmQyxyHoR5Y)

My Kotlin code (note, the Youtuber's code is cleaner than mine.)
```kotlin
fun minimumSwaps(arr: Array<Int>): Int {

    var ans = 0
    var i = 0
    var curr = 0
    while(i < arr.size){
        
        if(arr[i] != i+1) {
            var currVal = arr[i]
            // Kotlin swap trick
			arr[i] = arr[currVal-1].also{ arr[currVal-1] = arr[i] }
            ans+=1
            i=curr
        }else {
            i+=1
            curr = i  
        }
    }

    return ans
}
```

## Reference
- Extended problem - [If array is not from [1~n]](https://www.geeksforgeeks.org/minimum-number-swaps-required-sort-array/)
- [This appeared in Google interview](https://leetcode.com/discuss/interview-question/153179/google-onsite-min-swaps-to-make-sorted).

#google
