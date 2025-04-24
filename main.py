from blockchain.blockchain import Blockchain
from wallet.transaction import Transaction

blockchain = Blockchain()

while True:
    print("1. Add transaction\n2. Mine block\n3. View chain\n4. Exit")
    choice = input("> ")
    if choice == "1":
        sender = input("Sender: ")
        recipient = input("Recipient: ")
        amount = input("Amount: ")
        tx = Transaction(sender, recipient, amount)
        blockchain.add_transaction(tx.to_dict())
        print("✅ Transaction added.")
    elif choice == "2":
        index = blockchain.mine()
        print(f"⛏️ Block #{index} mined.")
    elif choice == "3":
        for block in blockchain.chain:
            print(vars(block))
    else:
        break
