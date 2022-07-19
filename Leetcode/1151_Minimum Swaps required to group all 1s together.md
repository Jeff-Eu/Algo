# 1151. Minimum Swaps required to group all 1s together

Given a binary array data, return the **minimum** number of swaps required to group all 1’s present in the array together in any place in the array.

Example 1:

```
Input: [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
```

Example 2:

```
Input: [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
```

Example 3:

```
Input: [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
```

Note:

1 <= data.length <= 10^5  
0 <= data[i] <= 1

## Answer

[Leetcode隱藏題，故取自GeeksForGeeks相同的題目有線上測驗](https://www.geeksforgeeks.org/minimum-swaps-required-group-1s-together/)

[這影片有不錯的講解，大概看到5:37就知道該怎麼寫了](https://www.youtube.com/watch?v=VXi_-2CmitM)

```cpp
int minSwaps(int arr[], int n) {
    
    // Complete the function
    
    int windowSz = 0;
    for(int i=0; i<n; i++)
        if(arr[i]==1)
            windowSz++;
            
    if(windowSz == 0)
        return -1;
    else if(windowSz == 1)
        return 0;
    
    int szOfZero = 0;
    for(int i=0; i<windowSz; i++)
        if(arr[i]==0)
            szOfZero++;
            
    int ans = szOfZero;            

    int idxL = 0, idxR = windowSz-1;
    while(idxR < n-1) {
        if(arr[idxL++]==0)
            szOfZero -= 1;
        if(arr[++idxR]==0)
            szOfZero += 1;
        
        ans = min(szOfZero, ans);
    }
    return ans;
}
```