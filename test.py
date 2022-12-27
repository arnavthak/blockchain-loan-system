from loanCoin import BlockChain
from loanCoin import Block
from login import Login

blockchain = BlockChain()

cred_list = {
    "A": "a",
    "B": "b",
    "C": "c",
    "South Windsor High School": "SWHS"
}

login = Login(cred_list)

def test(description, recipient):
    last_block = blockchain.lastest_block
    last_proof_no = last_block.proof_no
    proof_no = blockchain.proof_of_work(last_proof_no)

    blockchain.new_data(
        sender="South Windsor High School",
        recipient=recipient,
        description=description
    )

    last_hash = last_block.calculate_hash
    block = blockchain.construct_block(proof_no, last_hash)

    print(blockchain.chain)

test("D", "A")
print("Past Data from test.py: {}".format(blockchain.past_data))
while not (login.getLoggedIn()):
    login.LogIn()

list_of_desc = ['D']
print(blockchain.whoOwnsWhat(list_of_desc))
