# 2942. Find Words Containing Character

## LeetCode Link
[2942. Find Words Containing Character](https://leetcode.com/problems/find-words-containing-character/description/)

## Problem Description
You are given a 0-indexed array of strings words and a character x.

Return an array of indices representing the words that contain the character x.

Note that the returned array may be in any order.

Example 1:

Input: words = ["leet","code"], x = "e"
Output: [0,1]
Explanation: "e" occurs in both words: "leet", and "code". Hence, we return indices 0 and 1.
Example 2:

Input: words = ["abc","bcd","aaaa","cbc"], x = "a"
Output: [0,2]
Explanation: "a" occurs in "abc", and "aaaa". Hence, we return indices 0 and 2.
Example 3:

Input: words = ["abc","bcd","aaaa","cbc"], x = "z"
Output: []
Explanation: "z" does not occur in any of the words. Hence, we return an empty array.

## Initial Thought Process & Brute Force
Got optimized approach from the start.

## Optimized Approach
Iterate through array. Check for element. Add index to sol array if found. Can be one liner solution with list comprehension and enumerate but didnt bother.

### Time Complexity
$O(N * M)$ 

### Space Complexity
$O(1)$ 

## Code
```python
# Python solution
class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        # Created a array called solution where i will append index numbers
        sol = []
        # Taking length of array words
        n = len(words)
        # Iternating through array 
        for i in range(n):
            # If character x is present in element
            if x in words[i]:
                # Append index number to sol array
                sol.append(i)
        # Return sol array 
        return sol