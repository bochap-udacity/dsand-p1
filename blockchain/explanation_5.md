# Blockchain

## Problem

A Blockchain is a sequential chain of records, similar to a linked list. Each block contains some information and how it is connected related to the other blocks in the chain. Each block contains a cryptographic hash of the previous block, a timestamp, and transaction data. For our blockchain we will be using a SHA-256 hash, the Greenwich Mean Time when the block was created, and text strings as the data.

Use your knowledge of linked lists and hashing to create a blockchain implementation.

## Solution

A linked list was chosen to implement the block chain. This allows O(1) to add a new block to the end of the chain. This is made possible with the tail block reference to access the block's hash required for the new block and add the new block to the tail of chain.. It takes O(n) to find a block but that could be solve with a dictionary in the chain that stores blocks by the hash keys. This was not implemented but can be easily added. The linked list uses O(n) in space complexity where n is the number of blocks in the chain.