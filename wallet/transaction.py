import json
from ecdsa import SigningKey, VerifyingKey

class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def to_dict(self):
        return {
            "sender": self.sender,
            "recipient": self.recipient,
            "amount": self.amount
        }

    def sign_transaction(self, private_key_file):
        sk = SigningKey.from_pem(open(private_key_file).read())
        message = json.dumps(self.to_dict()).encode()
        return sk.sign(message)

    @staticmethod
    def verify_signature(transaction_dict, signature, public_key_file):
        vk = VerifyingKey.from_pem(open(public_key_file).read())
        return vk.verify(signature, json.dumps(transaction_dict).encode())