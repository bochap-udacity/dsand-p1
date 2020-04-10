import hashlib
import time
from datetime import datetime


class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.nextBlock = None

    def calc_hash(self):
        sha = hashlib.sha256()
        hash_str = f"{self.data}-{time.strftime('%Y%m%d%H%M%S', self.timestamp)}-{self.previous_hash}".encode(
            "utf-8"
        )
        sha.update(hash_str)
        return sha.hexdigest()

    def linkChain(self, nextBlock):
        self.nextBlock = nextBlock

    def __str__(self):
        return f"{self.data}-{time.strftime('%Y-%m-%d %H:%M:%S', self.timestamp)}-{self.previous_hash}"


class BlockChain:
    def __init__(self):
        self.genesis_block = None
        self.tail = None

    def addBlock(self, data):
        if self.genesis_block == None:
            self.genesis_block = Block(time.gmtime(), data, 0)
            self.tail = self.genesis_block
        else:
            newBlock = Block(time.gmtime(), data, self.tail.hash)
            self.tail.linkChain(newBlock)
            self.tail = newBlock

    def __str__(self):
        currentBlock = self.genesis_block
        output = ["Chain has the following blocks:"]
        output.append("-------------------------------")
        while currentBlock != None:
            output.append(str(currentBlock))
            currentBlock = currentBlock.nextBlock

        return "\n".join(output) if len(output) else "No blocks added"


def testCreateChain():
    """
      Test that new chain has no blocks
    """
    print("BlockChain test creation")
    chain = BlockChain()
    assert chain.genesis_block == None
    assert chain.tail == None
    print(f"New chain should have 'genesis_block' and 'tail' both equal to None")
    print(str(chain))
    print()


def testAddBlockWithNoneValue():
    """
      Test adding genesis block to chain with data equals to None
    """
    print("BlockChain test adding a block with data as None")
    chain = BlockChain()
    chain.addBlock(None)
    assert chain.genesis_block == chain.tail
    assert chain.genesis_block.data == None
    assert chain.genesis_block.nextBlock == None
    print(
        f"Adding first block should set 'genesis_block' and 'tail' to the same values"
    )
    print(str(chain))
    print()


def testAddBlockWithNonNoneValue():
    """
      Test adding genesis block to chain with data not equal to None
    """
    print("BlockChain test adding a block with data not equal to None")
    chain = BlockChain()
    chain.addBlock(1)
    assert chain.genesis_block == chain.tail
    assert chain.genesis_block.data == 1
    assert chain.genesis_block.nextBlock == None
    print(
        f"Adding first block should set 'genesis_block' and 'tail' to the same values"
    )
    print(str(chain))
    print()


def testAddMultipleBlockWithNonNoneValue():
    """
      Test adding genesis block to chain with data not equal to None for multiple blocks
    """
    print(
        "BlockChain test adding a block with data not equal to None for multiple blocks"
    )
    chain = BlockChain()
    chain.addBlock(1)
    chain.addBlock(2)
    assert chain.genesis_block != chain.tail
    assert chain.genesis_block.data == 1
    assert chain.genesis_block.nextBlock == chain.tail
    assert chain.tail.data == 2
    assert chain.tail.nextBlock == None
    print(
        f"Adding first block should set 'genesis_block' and 'tail' to different values"
    )
    print(str(chain))
    print()


def testBlockChain():
    testCreateChain()
    testAddBlockWithNoneValue()
    testAddBlockWithNonNoneValue()
    testAddMultipleBlockWithNonNoneValue()


testBlockChain()
