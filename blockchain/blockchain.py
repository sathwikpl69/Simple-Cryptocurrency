from .block import Block
import time

class Blockchain:
    difficulty = 2
    mining_reward = 10

    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()
        self.balances = {}

    def create_genesis_block(self):
        genesis = Block(0, [], time.time(), "0")
        genesis.hash = genesis.compute_hash()
        self.chain.append(genesis)

    def last_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def proof_of_work(self, block):
        block.nonce = 0
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash

    def add_block(self, block, proof):
        if block.previous_hash != self.last_block().compute_hash():
            return False
        if not proof.startswith('0' * Blockchain.difficulty):
            return False
        block.hash = proof
        self.chain.append(block)
        for tx in block.transactions:
            sender = tx['sender']
            recipient = tx['recipient']
            amount = float(tx['amount'])
            if sender != "SYSTEM":
                self.balances[sender] = self.balances.get(sender, 0) - amount
            self.balances[recipient] = self.balances.get(recipient, 0) + amount
        return True

    def mine(self, miner_address):
        if not self.unconfirmed_transactions:
            return False
        reward_tx = {"sender": "SYSTEM", "recipient": miner_address, "amount": self.mining_reward}
        self.unconfirmed_transactions.append(reward_tx)

        last = self.last_block()
        new_block = Block(index=last.index + 1,
                          transactions=self.unconfirmed_transactions,
                          timestamp=time.time(),
                          previous_hash=last.compute_hash())
        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.unconfirmed_transactions = []
        return new_block.index

    def get_balance(self, address):
        return self.balances.get(address, 0.0)