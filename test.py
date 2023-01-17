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

test("Textbook", "A")
print("Past Data from test.py: {}".format(blockchain.past_data))
while not (login.getLoggedIn()):
    login.LogIn()

list_of_desc = ['Textbook']
list_of_what_you_own = []
print(blockchain.whoOwnsWhat(list_of_desc))
for key, value in blockchain.whoOwnsWhat(list_of_desc).items():
    if (value == login.getUsername()):
        list_of_what_you_own.append(key)

print("You currently own: {}".format(list_of_what_you_own))

while True:
    answer = input("Do you want to transfer something you own to someone else (Y/N/LOGOUT)? ")
    if answer == "Y":
        recipient = input("Who's the recipient? Type in their username exactly correct: ")
        description = input("What is the description? Type in exactly as stated in your list of assets printed above: ")
        login.new_data(recipient, description, blockchain, list_of_desc)
        print("DONE!!!")
    elif answer == "LOGOUT":
        login.logout()
        while not (login.getLoggedIn()):
            login.LogIn()
        for key, value in blockchain.whoOwnsWhat(list_of_desc).items():
            if (value == login.getUsername()):
                list_of_what_you_own.append(key)
        print("You currently own: {}".format(list_of_what_you_own))
    else:
        print("Exiting now!")
        break