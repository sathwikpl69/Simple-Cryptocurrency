from flask import Flask, request, jsonify
from blockchain.blockchain import Blockchain
from wallet.transaction import Transaction

app = Flask(__name__)
bc = Blockchain()

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    tx_data = request.json
    tx = Transaction(tx_data['sender'], tx_data['recipient'], tx_data['amount'])
    bc.add_transaction(tx.to_dict())
    return jsonify({"message": "Transaction added"}), 201

@app.route('/mine', methods=['POST'])
def mine():
    data = request.json
    miner = data['miner']
    index = bc.mine(miner)
    return jsonify({"message": f"Block #{index} mined."})

@app.route('/chain', methods=['GET'])
def chain():
    return jsonify([block.__dict__ for block in bc.chain])

@app.route('/balance/<address>', methods=['GET'])
def balance(address):
    return jsonify({"balance": bc.get_balance(address)})

if __name__ == '__main__':
    app.run(port=5000)