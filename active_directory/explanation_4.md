# Active Directory

## Problem

In Windows Active Directory, a group can consist of user(s) and group(s) themselves. We can construct this hierarchy as such. Where User is represented by str representing their ids.

Write a function that provides an efficient look up of whether the user is in a group.

## Requirements

1. Python version 3.6 and above

## Solution

The solution makes use of a Python set that allows the handling of duplicated users found in different groups. Adding to a set and finding if an item exists takes an average of O(1). The set requires O(n) for space complexity where n = number of unique entires
