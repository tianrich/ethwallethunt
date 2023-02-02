import hashlib
import os

with open("made.txt", "r") as seedkeys_file:
    seedkeys = seedkeys_file.readlines()

addresses = []
for seedkey in seedkeys:
    seedkey = seedkey.strip().encode()
    private_key = hashlib.sha256(seedkey).hexdigest()
    public_key = hashlib.sha256(private_key.encode()).hexdigest()
    address = '0x' + public_key[-40:]
    addresses.append(address)

with open("generated.txt", "w") as generated_file:
    for address in addresses:
        generated_file.write(address + os.linesep)
