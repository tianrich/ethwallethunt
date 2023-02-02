import requests

def check_address_transactions(address):
    # make a request to the blockcypher API for the given address
    url = f"https://api.blockcypher.com/v1/eth/main/addrs/{address}/full"
    response = requests.get(url)

    # check if there are any transactions for the given address
    if response.json().get("txs"):
        return True
    return False

def save_to_file(address):
    with open("hunted.txt", "a") as f:
        f.write(address + "\n")

with open("generated.txt") as f:
    addresses = f.readlines()

for address in addresses:
    address = address.strip()
    if check_address_transactions(address):
        save_to_file(address)
    else:
        print(f"{address} has no transactions.")