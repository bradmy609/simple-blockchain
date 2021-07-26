#This module imports and utilizes the Blockchain module to initialize and fill a local blockchain
from blockchain import Blockchain

#Arbitrary transaction data stored in each block after the genesis block
block_one_transactions = {"sender":"Alice", "receiver": "Bob", "amount":"50"}
block_two_transactions = {"sender": "Bob", "receiver":"Cole", "amount":"25"}
block_three_transactions = {"sender":"Alice", "receiver":"Cole", "amount":"35"}

#A fake transaction that we will use in an attempt to alter the existing blockchain
fake_transactions = {"sender": "Bob", "receiver":"Cole, Alice", "amount":"25"}

local_blockchain = Blockchain()
local_blockchain.print_blocks()
local_blockchain.add_block(block_one_transactions)
local_blockchain.add_block(block_two_transactions)
local_blockchain.add_block(block_three_transactions)
local_blockchain.print_blocks()

# assign a difficulty number (the lower the number the faster the function) and uncomment
# the following line to have the proof hash printed to the console.
difficulty = 3
#print(local_blockchain.proof_of_work(local_blockchain.chain[1], difficulty))

# Uncommenting the following line will attempt to add an invalid transaction to the BC

# local_blockchain.chain[2].transactions = fake_transactions 
# local_blockchain.print_blocks()
# local_blockchain.chain[2].print_contents()
# print(' ')
# local_blockchain.validate_chain() <-- This line will print a message to the console stating whether the BC is valid or not