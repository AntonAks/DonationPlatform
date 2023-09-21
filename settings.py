import json
from web3 import Web3


# Connect to an Ethereum node
WEB3_PROVIDER_URL = ""
w3 = Web3(Web3.HTTPProvider(WEB3_PROVIDER_URL))

# Your Ethereum address (owner's address)
OWNER_ADDRESS = ''

# Your private key (keep this secret)
PRIVATE_KEY = ''

# Smart contract ABI and address
with open('contract_abi.json') as f:
    contract_abi = json.load(f)

CONTRACT_ADDRESS = '0xB0628ee92134b58Cd88eF36020c0DDA49bD97eb9'  # Replace with your contract's address (existing address is a Sepolia testnet contract

nonce = w3.eth.get_transaction_count(OWNER_ADDRESS)

# Create a contract instance
contract = w3.eth.contract(address=CONTRACT_ADDRESS, abi=contract_abi)


try:
    from local_settings import *
except ImportError:
    pass
