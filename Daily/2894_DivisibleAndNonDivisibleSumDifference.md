# 2894. Divisible and Non-divisible Sums Difference

## LeetCode Link
[2894. Divisible and Non-divisible Sums Difference](https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/description/)

## Problem Description
You are given positive integers n and m.

Define two integers as follows:

num1: The sum of all integers in the range [1, n] (both inclusive) that are not divisible by m.
num2: The sum of all integers in the range [1, n] (both inclusive) that are divisible by m.
Return the integer num1 - num2.


Example 1:  

Input: n = 10, m = 3  
Output: 19  
Explanation: In the given example:
- Integers in the range [1, 10] that are not divisible by 3 are [1,2,4,5,7,8,10], num1 is the sum of those integers = 37.
- Integers in the range [1, 10] that are divisible by 3 are [3,6,9], num2 is the sum of those integers = 18.
We return 37 - 18 = 19 as the answer.  

Example 2:  

Input: n = 5, m = 6  
Output: 15  
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 6 are [1,2,3,4,5], num1 is the sum of those integers = 15.
- Integers in the range [1, 5] that are divisible by 6 are [], num2 is the sum of those integers = 0.
We return 15 - 0 = 15 as the answer.  

Example 3:  

Input: n = 5, m = 1  
Output: -15  
Explanation: In the given example:
- Integers in the range [1, 5] that are not divisible by 1 are [], num1 is the sum of those integers = 0.
- Integers in the range [1, 5] that are divisible by 1 are [1,2,3,4,5], num2 is the sum of those integers = 15.
We return 0 - 15 = -15 as the answer.  

## Initial Thought Process & Brute Force
No need to overcomplicate this one going to approach straight away.

## Optimized Approach
Iterate based on range given (1,n) including both. if divisible by m then add to num2 else add to num1. Return num1-num2

### Time Complexity
$O(N)$ 

### Space Complexity
$O(1)$ 

## Code
```python
# Python solution
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        num1,num2 = 0,0
        for i in range(1,n+1):
            if i % m == 0:
                num2+=i
            else: 
                num1+=i
        return num1-num2