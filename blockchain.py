import hashlib

#Basic Block

transaction_1 = "Wallet #1 paid 1 BTC to Wallet #2"
genesis_block=(transaction_1)
print(genesis_block)

def bit_hash(data):
    string_data=str(data)
    formatted_data = string_data.encode('utf-8')
    bit_hash = hashlib.sha256(formatted_data).hexdigest()
    return bit_hash

genesis_block_hash = bit_hash((0,transaction_1))
print(genesis_block_hash)

genesis_block=(0,transaction_1,genesis_block_hash)
print(genesis_block)

transaction_2 = "Wallet #1 paid 2 BTC to Wallet #2"

block_2_hash = bit_hash((genesis_block_hash, transaction_2))

block_2 = (genesis_block_hash, transaction_2, block_2_hash)
print(block_2)

def create_block(prior_block_hash, prior_block_number, transaction_data):
    block_number = prior_block_number + 1
    block_hash = bit_hash((prior_block_hash, block_number, transaction_data))
    new_block = (prior_block_hash, block_number, transaction_data, block_hash)
    return new_block

genesis_block = create_block(0, -1, "Wallet #1 paid 1 BTC to Wallet #2")
print(genesis_block)

prior_block = genesis_block
for i in range(3):
    prior_block_hash = prior_block[3]
    prior_block_number = prior_block[1]

    next_block = create_block(prior_block_hash, prior_block_number, "Wallet #1 paid " + str(i+2)+" BTC to Wallet #2")
    print(next_block)
    prior_block=next_block
