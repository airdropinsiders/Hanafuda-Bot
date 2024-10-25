from web3 import Web3
import json
import time
from colorama import init, Fore, Style

init(autoreset=True)

# Constants
RPC_URL = "https://mainnet.base.org"
CONTRACT_ADDRESS = "0xC5bf05cD32a14BFfb705Fb37a9d218895187376c"
AMOUNT_ETH = 0.0000000001  # Jumlah ETH yang akan didepositkan

# Contract ABI
CONTRACT_ABI = '''
[
    {
        "constant": false,
        "inputs": [],
        "name": "depositETH",
        "outputs": [],
        "stateMutability": "payable",
        "type": "function"
    }
]
'''

# Web3 Connection
web3 = Web3(Web3.HTTPProvider(RPC_URL))
amount_wei = web3.to_wei(AMOUNT_ETH, 'ether')
contract = web3.eth.contract(address=CONTRACT_ADDRESS, abi=json.loads(CONTRACT_ABI))

# Load Private Keys
with open("pvkey.txt", "r") as file:
    private_keys = [line.strip() for line in file if line.strip()]
nonces = {key: web3.eth.get_transaction_count(web3.eth.account.from_key(key).address) for key in private_keys}

# Display Header
def display_header():
    print(Fore.CYAN + Style.BRIGHT + """\n
    *********************************************
              Welcome to HANA Auto Depositor
                t.me/AirdropInsiderID
    *********************************************
    """ + Style.RESET_ALL)

# Display Footer
def display_footer(start_time):
    elapsed_time = time.time() - start_time
    print(Fore.MAGENTA + Style.BRIGHT + f"\nAll transactions completed in {elapsed_time:.2f} seconds.\n")
    print(Fore.CYAN + "**************************************************" + Style.RESET_ALL)
    print(Fore.CYAN + "Thank you for using HANA Auto Depositor!\n" + Style.RESET_ALL)
    print(Fore.CYAN + "**************************************************" + Style.RESET_ALL)

# Send Transactions
def send_transactions(num_transactions):
    tx_count = 0
    for i in range(num_transactions):
        for private_key in private_keys:
            from_address = web3.eth.account.from_key(private_key).address
            short_from_address = f"{from_address[:4]}...{from_address[-4:]}"
            try:
                tx_hash = execute_transaction(private_key, from_address, short_from_address)
                tx_count += 1

                # Batasi batch transaksi
                if tx_count >= 50:
                    tx_count = 0
                time.sleep(1)  # Sesuaikan delay jika diperlukan

            except Exception as e:
                handle_exception(e, private_key, from_address, short_from_address)

# Execute Transaction
def execute_transaction(private_key, from_address, short_from_address):
    transaction = contract.functions.depositETH().build_transaction({
        'from': from_address,
        'value': amount_wei,
        'gas': 100000,
        'gasPrice': web3.eth.gas_price,
        'nonce': nonces[private_key]
    })

    signed_txn = web3.eth.account.sign_transaction(transaction, private_key=private_key)
    tx_hash = web3.eth.send_raw_transaction(signed_txn.raw_transaction)
    tx_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(Fore.GREEN + f"[{tx_time}] Transaction sent from {short_from_address} - Hash: {tx_hash.hex()}")

    # Update nonce
    nonces[private_key] += 1
    return tx_hash

# Handle Exceptions
def handle_exception(e, private_key, from_address, short_from_address):
    if 'nonce too low' in str(e):
        print(Fore.YELLOW + f"[Warning] Nonce too low for {short_from_address}. Updating nonce...")
        nonces[private_key] = web3.eth.get_transaction_count(from_address)
    else:
        print(Fore.RED + f"[Error] Transaction failed from {short_from_address}: {str(e)}")

# Main Execution
if __name__ == "__main__":
    display_header()
    num_transactions = int(input(Fore.YELLOW + "Enter the number of transactions to be executed: " + Style.RESET_ALL))
    print(Fore.CYAN + "\nStarting Transactions...\n" + Style.RESET_ALL)
    
    start_time = time.time()
    send_transactions(num_transactions)
    display_footer(start_time)
