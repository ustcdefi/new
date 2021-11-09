from web3 import Web3
import json
import config
import argparse
import time


def get_args():
    
    parser = argparse.ArgumentParser(description='Monitor a contract using web3py',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    # Get token address, 'Dinosaur Egg' address in default
    parser.add_argument('-ad', '--address', metavar='A', type=str, default='0x9a78649501bbaac285ea4187299471b7ad4abd35',
                        help='The contract, you want to monitor')

    parser.add_argument('-b', '--block', metavar='B', type=str, nargs='?', default='latest',
                        help='The block you want to check')
    
    # Get the account address : bitfatty in default
    parser.add_argument('-ac', '--account', metavar='C', type=str, nargs='?', default='0xF1aC2C73D2e5d30b78874552E640D48490f9fe42',
                        help='The account you want to filter')
    
    # Get main net information
    parser.add_argument('-m', '--mainnet', metavar='m', type=str, nargs='?', default='https://bsc-dataseed.binance.org/',
                        help='Main-net you want to connect')

    parser.add_argument('-i', '--abifile', metavar='m', type=str, nargs='?', default='./dinosaur_abi.txt',
                        help='ABI File')


    return parser.parse_args()


def handle_event(event):
    print(event)

def log_loop(event_filter, poll_interval):
    while True:
        for event in event_filter.get_new_entries():
            handle_event(event)
        time.sleep(poll_interval)

if __name__ == "__main__":

    args = get_args()
    
    

    
    web3 = Web3(Web3.HTTPProvider(args.mainnet))
    print('The Network is ' + 'Connected' if web3.isConnected() else 'Not Connected')
    # Check whether the main network is connected
    print('The current block is ' + '%d' %web3.eth.block_number)
    # Show the latest block number

    contract_address = Web3.toChecksumAddress(args.address)
    abi_file = open(args.abifile,'r')
    contract_abi = json.loads(abi_file.read())
    abi_file.close()

    contract = web3.eth.contract(address = contract_address, abi = contract_abi)
    # test whether the abi works
    print('The total supply of %s is ' %contract.functions.symbol().call() + '%d' %contract.functions.totalSupply().call())

    # for i in range(1, (web3.eth.block_number - 11583439) // 100):
    #     print(i)

        # TransferEvent = web3.eth.get_logs({"address": contract_address,
        #                   "fromBlock": 11583439 + i * 100,
        #                   "toBlock": 11583439 + (i + 1)* 100,
        #                   'from': '0xF1aC2C73D2e5d30b78874552E640D48490f9fe42'})
    TransferEvent = contract.events.Transfer.createFilter(fromBlock = 'latest', argument_filters={'from': args.account})
    log_loop(TransferEvent,2)
    
    
    
    
    




