# Finding Files

## Problem

For this problem, the goal is to write code for finding all files under a directory (and all directories beneath it) that end with ".c"

Here is an example of a test directory listing,

```
./testdir
./testdir/subdir1
./testdir/subdir1/a.c
./testdir/subdir1/a.h
./testdir/subdir2
./testdir/subdir2/.gitkeep
./testdir/subdir3
./testdir/subdir3/subsubdir1
./testdir/subdir3/subsubdir1/b.c
./testdir/subdir3/subsubdir1/b.h
./testdir/subdir4
./testdir/subdir4/.gitkeep
./testdir/subdir5
./testdir/subdir5/a.c
./testdir/subdir5/a.h
./testdir/t1.c
./testdir/t1.h
```

## Requirements

1. Python version 3.6 and above
2. testdir and empty folders should be present for testing

## Solution

The solution uses a list a makes use of recursion to check the paths. The recursion uses the call stack which is the equivalent and has a time complexity O(n) where n is each of the file or path in the system. The space complexity will be O(n) for all the paths found in the tree for the list
