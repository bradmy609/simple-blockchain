# This module creates a blockchain class that creates a list with a Block at each index
from block import Block

class Blockchain:
# Instantiates the blockchain with a genesis block -- the first block in any BC is referred to as the genesis block, 
# which does not contain transaction data.
  def __init__(self):
    self.chain = [] #<- The actual blockchain, each block will be added onto to the next available index position
    self.all_transactions = []
    self.genesis_block()

#Creates the genesis block anytime the blockchain is instantiated
  def genesis_block(self):
    transactions = {}
    genesis_block = Block(transactions, "0")
    self.chain.append(genesis_block)
    return self.chain

  # prints each block in the blockchain's data
  def print_blocks(self):
    for i in range(len(self.chain)):
      current_block = self.chain[i]
      print("Block {} {}".format(i, current_block))
      current_block.print_contents()
      print('\n')
  
  # add block to blockchain `chain`
  def add_block(self, transactions):
    previous_block_hash = self.chain[len(self.chain)-1].hash
    new_block = Block(transactions, previous_block_hash)
    # modify this method
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block

# Checks that the blockchain has not been compromised by recalculating each block's hash and comparing 
# the resulting hash with the value found in the self.previous_hash variable for the subsequent block
  def validate_chain(self):
    for i in range(1, len(self.chain)):
      current = self.chain[i]
      previous = self.chain[i-1]
      if(current.hash != current.generate_hash()):
        print("The current hash of the block does not equal the generated hash of the block.")
        return False
      if(current.previous_hash != previous.generate_hash()):
        print("The previous block's hash does not equal the previous hash value stored in the current block.")
        return False
    return True

# Attempts to find a nonce value that will change the specified block's hash so that it 
# starts with the first X characters being 0's. Difficulty = X. So if Difficulty = 2,
# the function will generate new hashes, incrementing the nonce value after each one, until 
# a hash starting with '00' is found. 
  def proof_of_work(self, block, difficulty=2):
    proof = block.generate_hash()
    while proof[:difficulty] != '0'*difficulty:
      block.nonce += 1
      proof = block.generate_hash()
    block.nonce = 0
    return proof