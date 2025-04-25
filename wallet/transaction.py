import json
from ecdsa import VerifyingKey, SigningKey, SECP256k1

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': f"{self.amount} CEC"
        }

    def sign_transaction(self, private_key):
        sk = SigningKey.from_pem(private_key)
        message = json.dumps(self.to_dict()).encode()
        return sk.sign(message)

    @staticmethod
    def verify_transaction(transaction_dict, signature, public_key):
        vk = VerifyingKey.from_pem(public_key)
        message = json.dumps(transaction_dict).encode()
        return vk.verify(signature, message)
