# Explain in detail the workings of a dynamic array:

## What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

Inserting/deleting anywhere but the end has a runtime complexity of O(n), because every subsequent element needs to be shifted over after the new element gets added.

Adding to/deleting from the back is O(1) unless the array needs to be resized. When it does need to be resized, it's an O(n) operation. On average though, it's O(1), because over time, at least in Python's implementation of lists, it gets less and less likely that you will need to resize the array on an append call.

## What is the worse case scenario if you try to extend the storage size of a dynamic array?

When the array does need to be resized, it's an O(n) operation.

## Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

The chain is the total collection of transactions.

Each link in the chain is a block. Each block contains the index, the timestamp, the transactions that are proofed by the block, the proof itself, and the previous hash.

The previous hash in a block leads to the previous block and is how the blockchain stays connected/protected.

## Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Proof of Work makes it so you cannot change the hashes in the chain easily. This disallows someone from changing the block and editing the hashes stored in the next blocks to match. POW is a piece of data that takes a lot of effort to generate, forcing the miner to spend time to add a block. It's essentially the solution to a difficult problem. The block is only added if the solution is valid. Because it takes so long to compute, it's not really possible for one thief to out perform the whole community of people mining.
