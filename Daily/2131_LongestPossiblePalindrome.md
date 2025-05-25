# 2131. Longest Palindrome by Concatenating Two Letter Words

## LeetCode Link
[2131. Longest Palindrome by Concatenating Two Letter Words](https://leetcode.com/problems/longest-palindrome-by-concatenating-two-letter-words/description/)

## Problem Description
You are given an array of strings words. Each element of words consists of two lowercase English letters.

Create the longest possible palindrome by selecting some elements from words and concatenating them in any order. Each element can be selected at most once.

Return the length of the longest palindrome that you can create. If it is impossible to create any palindrome, return 0.

A palindrome is a string that reads the same forward and backward.

Example 1:  

    Input: words = ["lc","cl","gg"]
    Output: 6
    Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of length 6.
    Note that "clgglc" is another longest palindrome that can be created.
    Example 2:

Example 2:  

    Input: words = ["ab","ty","yt","lc","cl","ab"]
    Output: 8
    Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt", of length 8.
    Note that "lcyttycl" is another longest palindrome that can be created.
    Example 3:

Example 3:  

    Input: words = ["cc","ll","xx"]
    Output: 2
    Explanation: One longest palindrome is "cc", of length 2.
    Note that "ll" is another longest palindrome that can be created, and so is "xx".

## Approach
Going line by line.  

        word_counts = Counter(words)

Creates a dictionary-like object where keys are unique words and values are their frequencies.  

        length = 0

Initializes a variable to track the total length of the palindrome being built.  

        has_center = False

A boolean flag to check if there's a leftover word like "gg" that can be used in the middle of the palindrome.  

        for word in word_counts:

Loops through each unique word in the word count dictionary.  

            reverse = word[::-1]

Reverses the current word using Python slicing.  

            if word != reverse and reverse in word_counts:

Checks if the word has a non-palindromic reverse also present in the dictionary.  

            pairs = min(word_counts[word], word_counts[reverse])

Finds how many such reversible pairs can be formed.  

                length += pairs * 4

Each pair adds 4 characters to the palindrome (2 at the start, 2 at the end).

                word_counts[word] = 0
                word_counts[reverse] = 0

Marks both the word and its reverse as used by setting their counts to 0.  

            elif word == reverse:

Handles palindromic words like "gg", "cc", etc.  

                pairs = word_counts[word] // 2

Calculates how many full pairs can be made from the palindromic word.  

                length += pairs * 4

Each such pair adds 4 characters to the palindrome.  

                word_counts[word] %= 2 

Updates the count to show whether one unpaired word is left.  

                if word_counts[word] == 1:
                    has_center = True

If one is left, mark that we can use it in the middle of the palindrome.  

        if has_center:
            length += 2

Add 2 to the palindrome length if there is a central palindromic word left.  

        return length

Return the total length of the longest palindrome that can be formed.  

### Time Complexity
$O(N)$ 

### Space Complexity
$O(1)$ 

## Code
```python
# Python solution
from collections import Counter

class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_counts = Counter(words)
        length = 0
        has_center = False

        for word in word_counts:
            reverse = word[::-1]
            if word != reverse and reverse in word_counts:
                pairs = min(word_counts[word], word_counts[reverse])
                length += pairs * 4
                word_counts[word] = 0
                word_counts[reverse] = 0
            elif word == reverse:
                pairs = word_counts[word] // 2
                length += pairs * 4
                word_counts[word] %= 2 
                if word_counts[word] == 1:
                    has_center = True
        if has_center:
            length += 2
        return length