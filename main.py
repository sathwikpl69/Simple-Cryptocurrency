from blockchain.blockchain import Blockchain
from wallet.transaction import Transaction
import json

blockchain = Blockchain()

print("🚀 Welcome to CEC — Crypto Education Coin 💰")

while True:
    print("\n=== MENU ===")
    print("1. Add transaction")
    print("2. Mine block")
    print("3. View blockchain")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        sender = input("Sender name or wallet: ")
        recipient = input("Recipient name or wallet: ")
        amount = input("Amount in CEC: ")
        tx = Transaction(sender, recipient, amount)
        blockchain.add_transaction(tx.to_dict())
        print("✅ Transaction added.")
    
    elif choice == "2":
        address = input("Enter your wallet address to receive mining reward (CEC): ")
        blockchain.add_transaction({
            'sender': 'MINING',
            'recipient': address,
            'amount': '10 CEC'
        })
        blockchain.mine()
        print("✅ Block successfully mined.")

    elif choice == "3":
        for block in blockchain.chain:
            print("\n🧱", block.__dict__)

    elif choice == "4":
        print("👋 Exiting CEC CLI. Thank you!")
        break
