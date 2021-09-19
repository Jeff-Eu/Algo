# Rearrange Array
Q: Rearrange a given array so that Arr[i] becomes Arr[Arr[i]] with O(1) extra space.

```
Input: arr[]  = {3, 2, 0, 1}
Output: arr[] = {1, 0, 3, 2}

Input: arr[] = {4, 0, 2, 1, 3}
Output: arr[] = {3, 4, 2, 0, 1}

Input: arr[] = {0, 1, 2, 3}
Output: arr[] = {0, 1, 2, 3}
```
Lets say N = size of the array. Then, following holds true :
- All elements in the array are in the range [0, N-1]
- N * N does not overflow for a signed integer

## 思路
Consider
 a[]={4,2,0,1,3}

i=0; a[i]=a[0]=4; a[a[i]]=a[4]=3\
i=1; a[i]=2; 	  a[a[i]]=a[2]=0\
i=2; a[i]=0; 	  a[a[i]]=a[0]=4\
i=3; a[i]=1; 	  a[a[i]]=a[1]=2\
i=4; a[i]=3; 	  a[a[i]]=a[3]=1

So result array is : a[]={3,0,4,2,1}

for every index i in the array our goal is to transform
 a[i]------->a[a[i]]

the solution to this problem consists of 2 steps:
step 1: for(i=0 upto n-1)
 a[i]=a[i]+(a[a[i]]%n)*n

what does this step do? let us see.

1.0: a[0]=a[0]+(a[a[0]]%n)*n\
 =4+(3%5)*5\
 =4+3*5 =19\
 =a[0]+a[a[0]]*n\
So the array now becomes {19,2,0,1,3}

1.1: a[1]=a[1]+(a[a[1]]%n)*n\
 =2+(0%5)*5\
 =2+0*5 =2\
 =a[1]+a[a[1]]*n\
So the array now becomes {19,2,0,1,3}

1.2: a[2]=a[2]+(a[a[2]]%n)*n\
 =0+(19%5)*5\
 =0+((4+3*5)%5)*5\
 =0+((4%5)+(3*5)%5)%5*5   // (a+b)%c=(a%c + b%c)%c\
 =0+(4+0)%5*5\
 =0+ 4*5=20\
 =a[2]+a[a[2]]*n *note: Here a[a[2]] in this line refers to the original value of a[a[2]] (which is 4) given in the input arr*
 
 ```
 摘錄自wiki中關於mod的分配律
 
 Distributive:
(a + b) mod n = [(a mod n) + (b mod n)] mod n.
ab mod n = [(a mod n)(b mod n)] mod n.
 ```

So the array now becomes {19,2,20,1,3}

1.3: a[3]=a[3]+(a[a[3]]%n)*n\
 a[3]=1+(a[1]%n)*n\
 a[3]=1+((2+0*5)%5)*5\
 =1+2*5=11\
 =a[3]+a[a[3]]*n

So the array now becomes {19,2,20,11,3}

1.4: a[4]=a[4]+(a[a[4]]%n)*n\
 a[4]=3+(a[3]%5)*5\
 =3+((1+2*5)%5)*5\
 =3+1*5=8

So the array now becomes {19,2,20,11,3}

what did we do?\
initial arr is { 4,2,0,1,3}\
the current state of arr is\
{ 4+3*5(=19), 2+0*5(=2), 0+4*5(=20), 1+2*5(=11), 3+0*5(=3) }

in essence for every index i in the array we have transformed 
 a[i]---->a[i] + a[a[i]]*n

but remember our goal was to transform a[i]--->a[a[i]]\
How do we do this?\
We can do this by dividing each element of array by n(Step 2)

(a[i] + a[a[i]]*n)/n = a[i]/n + (a[a[i]]*n)/n

Now a[i] is a number between 0 to n-1. so, a[i]/n will be between 0 and 1\
Since we are doing integer division the answer will be truncated to 0.
i.e a[i]/n=0

also a[a[i]]*n/n =a[a[i]]

So
 (a[i] + a[a[i]]*n)/n = a[i]/n + (a[a[i]]*n)/n = 0 +a[a[i]] =a[a[i]]

## Answer

```python
class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        n = len(A)
        for i in range(n):
            A[i] += (A[A[i]] % n)*n
        for i in range(n):
            A[i] /= n
```