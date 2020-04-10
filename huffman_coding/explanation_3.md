# Huffman Coding

## Problem

A Huffman code is a type of optimal prefix code that is used for compressing data. The Huffman encoding and decoding schema is also lossless, meaning that when compressing the data to make it smaller, there is no loss of information.

The Huffman algorithm works by assigning codes that correspond to the relative frequency of each character for each character. The Huffman code can be of any length and does not require a prefix; therefore, this binary code can be visualized on a binary tree with each encoded character being stored on leafs.

There are many types of pseudocode for this algorithm. At the basic core, it is comprised of building a Huffman tree, encoding the data, and, lastly, decoding the data.

Here is one type of pseudocode for this coding schema:

1. Take a string and determine the relevant frequencies of the characters.
2. Build and sort a list of tuples from lowest to highest frequencies.
3. Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
4. Trim the Huffman Tree (remove the frequencies from the previously built tree).
5. Encode the text into its compressed form.
6. Decode the text from its compressed form.

You then will need to create encoding, decoding, and sizing schemas.

## Requirements

Python version 3.6 and above

## Solution

The implementation uses a Counter which is a subclass of dict to calculate the distinct instances of characters that is in the string. The time complexity of that is O(n) to iterate all the characters in the string. The counter keys are then sort in an operation which is O(nlogn). The construction of the tree involves using a heap to store the weight of each tree, each iteration requires O(logn) to get and insert the cheapest weight and there are O(n) iterations which makes the worst case O(nlogn)