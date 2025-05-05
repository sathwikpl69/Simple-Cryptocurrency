from blockchain.blockchain import Blockchain
from wallet.transaction import Transaction
import json

blockchain = Blockchain()

while True:
    print("1. Add transaction\n2. Mine block\n3. View chain\n4. Check balance\n5. Exit")
    choice = input("> ")
    if choice == "1":
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        amount = input("Amount: ")
        tx = Transaction(sender, recipient, amount)
        blockchain.add_transaction(tx.to_dict())
        print("Transaction added!")
    elif choice == "2":
        miner = input("Enter miner address: ")
        blockchain.mine(miner)
        print("Block mined.")
    elif choice == "3":
        for block in blockchain.chain:
            print(block.__dict__)
    elif choice == "4":
        addr = input("Enter address: ")
        print(f"Balance: {blockchain.get_balance(addr)}")
    else:
        break