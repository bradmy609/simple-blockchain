#This module defines what a block is by creating a "Block" class
import datetime
from hashlib import sha256

class Block:
#instantiates the blockchain with a genesis block -- the first block in any BC is 
#referred to as the genesis block
    def __init__(self, transactions, previous_hash):
        self.time_stamp = datetime.datetime.now() #<- Records the current date+time
        self.transactions = transactions #<- This is where you may input data -- for cryptos, the data is typically transaction(s)
        self.previous_hash = previous_hash #<- The previous blocks sha256 hash
        self.nonce = 0 #<- Nonce value is used as an arbitrary integer that is incremented in a function to provide proof of work
        self.hash = self.generate_hash() #<- Stores generated

# Generates hash using datetime, transactions, previous hash, and nonce value
    def generate_hash(self):
        block_header = str(self.time_stamp) + str(self.transactions) +str(self.previous_hash) + str(self.nonce)
        block_hash = sha256(block_header.encode())
        return block_hash.hexdigest()

# Prints the contents of a block
    def print_contents(self):
        print("timestamp:", self.time_stamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())
        print("previous hash:", self.previous_hash) 
