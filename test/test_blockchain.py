from blockchain.blockchain import Blockchain
from wallet.transaction import Transaction

def test_blockchain_creation():
    bc = Blockchain()
    assert len(bc.chain) == 1  # Genesis block exists

def test_transaction_validity():
    tx = Transaction("sender", "receiver", 10)
    tx.signature = "abc"
    assert not tx.is_valid()
