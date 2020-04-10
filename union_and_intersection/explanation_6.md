# Union and Intersection of Two Linked Lists

## Problem
Your task for this problem is to fill out the union and intersection functions. The union of two sets A and B is the set of elements which are in A, in B, or in both A and B. The intersection of two sets A and B, denoted by A ∩ B, is the set of all objects that are members of both the sets A and B.

You will take in two linked lists and return a linked list that is composed of either the union or intersection, respectively. Once you have completed the problem you will create your own test cases and perform your own run time analysis on the code.

## Solution

The intersection and union functions uses a dictionary to check for unions and intersections. The worst case will be O(n + m) with n for the number of items in list 1 and m for list 2. This is the time complexity to run the final dictionary to produce the list of outputs for both the unions and intersection. Space complexity of this solution is O(n) where n is the combined number of unique items in the 2 lists.