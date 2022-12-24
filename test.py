from loanCoin import BlockChain
from loanCoin import Block

blockchain = BlockChain()

def create_block(description, recipient):
    last_block = blockchain.lastest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    blockchain.new_data(
        sender="South Windsor High School",
        recipient=recipient,
        description=description
    )

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash, description)

    print(blockchain.chain)

create_block("Physics by Giancoli loaned by Mr. Fazzino with no 18-12", "Arnav Thakrar")
