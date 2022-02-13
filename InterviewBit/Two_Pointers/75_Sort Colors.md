# Leetcode-75. Sort Colors
Q: Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
```
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
```
Follow up:

* A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
* Could you come up with a one-pass algorithm using only constant space? (In place sort)

## Answer
高手解:

Swap the 0s to the start of the array maintaining a pointer, and 2s to the end of the array. 1s will automatically be in their right position. 

Java code:

```java
class Solution {
    public void sortColors(int[] nums) {
        int high = nums.length-1;
        int low = 0;
        int p = 0;
        while(p<=high){
            if(nums[p]==0){
                swap(nums,p,low);
                low++;
                p++;
                continue;
            }
            if(nums[p]==2){
                swap(nums,p,high);
                high--;
                continue;
            }
            if(nums[p]==1){
                p++;
                continue;
            }
        }
    }
    
    private void swap(int[]nums, int x, int y){
        if(x==y)
            return;
        int temp = nums[x];
        nums[x] = nums[y];
        nums[y] = temp;
    }
}
```