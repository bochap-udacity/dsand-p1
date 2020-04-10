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

The solution uses a set and makes use of recursion to check the paths. The recursion uses the call stack which is the equivalent or O(n) for each of the file or path in the system. It makes use of a set to keep track of the paths found and is O(1) on average and O(N) for the worst cast. At the end we perform a sort to get the result which is O(nlogn). So the worst case time complexity will be O(nlogn)
