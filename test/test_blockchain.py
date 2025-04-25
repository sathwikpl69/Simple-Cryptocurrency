from blockchain.block import Block

def test_hash_consistency():
    block = Block(1, [{"sender": "a", "recipient": "b", "amount": 10}], 0, "0")
    hash1 = block.compute_hash()
    hash2 = block.compute_hash()
    assert hash1 == hash2
