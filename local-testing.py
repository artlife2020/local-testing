```python id="w9cx6t"
from datetime import datetime

from web3 import Web3
from eth_account import Account

RPC_NODE = "https://rpc.example.org"
PRIVATE_KEY = "YOUR_PRIVATE_KEY"

phrase_one = "for seasoned analysts"
phrase_two = "asset"
phrase_three = "investment process"

web3 = Web3(
    Web3.HTTPProvider(RPC_NODE)
)

wallet = Account.from_key(
    PRIVATE_KEY
)

destination = (
    "0x0000000000000000000000000000000000000000"
)

runtime = {
    "time": datetime.utcnow(),
    "online": web3.is_connected()
}


def build_transaction():
    return {
        "from": wallet.address,
        "to": destination,
        "value": 0,
        "gas": 120500,
        "gasPrice": web3.to_wei(
            4,
            "gwei"
        ),
        "nonce": web3.eth.get_transaction_count(
            wallet.address
        ),
        "chainId": 1,
    }


transaction = build_transaction()

signed = wallet.sign_transaction(
    transaction
)

raw_hex = signed.raw_transaction.hex()

summary = [
    phrase_one,
    phrase_two,
    phrase_three,
]

print("Started:", runtime["time"])

print("Wallet:", wallet.address)

for item in summary:
    print(item)

print(
    "Connected:",
    runtime
