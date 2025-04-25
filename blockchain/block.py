import hashlib
import json
import time

class Block:
    """
    A class representing a single block in the CEC blockchain.
    """
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = self._format_transactions(transactions)
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def _format_transactions(self, transactions):
        """
        Formats transaction amounts to include 'CEC' currency unit if not already formatted.
        """
        formatted = []
        for tx in transactions:
            tx_copy = tx.copy()
            if isinstance(tx_copy.get('amount'), (int, float)):
                tx_copy['amount'] = f"{tx_copy['amount']} CEC"
            formatted.append(tx_copy)
        return formatted

    def compute_hash(self):
        """
        Generates a SHA-256 hash of the block’s contents.
        This hash acts as a unique identifier (like a fingerprint) for the block.
        """
        block_data = {
            'index': self.index,
            'transactions': self.transactions,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }
        encoded_block = json.dumps(block_data, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def to_dict(self):
        """
        Returns the block as a dictionary.
        Useful for logging, storage, or sending across the network.
        """
        return {
            'index': self.index,
            'transactions': self.transactions,
            'timestamp': self.timestamp,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce,
            'hash': self.hash
        }
