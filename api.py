import json
import os
from web3 import Web3, HTTPProvider


class EduPart:
    ganache_url = os.getenv('GANACHE_URL')
    w3 = Web3(HTTPProvider(ganache_url))

    admin_address = os.getenv('ADMIN_ADDRESS')
    address_contract = Web3.toChecksumAddress(os.getenv('CONTRACT_ADDRESS'))

    def __init__(self):
        with open('API/abi.json', 'r') as file:
            abi = json.loads(file.read())

        self.contract = self.w3.eth.contract(address=self.address_contract, abi=abi)

    def accounts(self):
        return self.w3.eth.accounts

    def get_balance(self, address):
        address = Web3.toChecksumAddress(address)
        return Web3.fromWei(self.w3.eth.getBalance(address), 'ether')

    def add_group(self, group):
        tx = self.contract.functions.addGroup(group).transact({'from': self.admin_address})

    def get_group(self, group):
        return self.contract.functions.getGroup(group).call()

    def payment(self, name, user_adr):
        tx = self.contract.functions.Payment(name).transact({'from': user_adr, 'value': self.value)

