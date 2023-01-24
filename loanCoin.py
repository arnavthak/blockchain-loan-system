import hashlib
import time

class Block:
    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no,
                                              self.prev_hash,
                                              self.data, self.timestamp)
        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no,
                                               self.prev_hash,
                                               self.data, self.timestamp)

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data
        )
        self.current_data = []

        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False
        elif prev_block.calculate_hash != block.prev_hash:
            return False
        elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
            return False
        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    def new_data(self, sender, recipient, description):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'description': description
        })
        print("JUST APPENDED TO CURRENT DATA: {}, {}, {}".format(sender, recipient, description))
        print("Current data in loanCoin.py: {}".format(self.current_data))
        return True

    def whoOwnsWhat(self, list_of_descriptions):
        items_owned = {}
        '''for description in list_of_descriptions:
            items_owned[description] = None'''

        curr_desc_data = []
        for dictionary in self.current_data:
                curr_desc_data.append(dictionary['description'])
        curr_recipient_data = []
        for dictionary in self.current_data:
            curr_recipient_data.append(dictionary['recipient'])
        print("Current Description Data: {}".format(curr_desc_data))
        print("Current Recipient Data: {}".format(curr_recipient_data))

        next = 0
        next_owner = 0
        for desc in list_of_descriptions:
            print("Description this iteration is {}".format(desc))
            while next != 0.01:
                try:
                    next = curr_desc_data.index(desc)
                    next_owner = curr_recipient_data[next]
                    print("Next owner this iteration is {}".format(next_owner))
                    curr_desc_data.pop(next)
                    curr_recipient_data.pop(next)
                except ValueError:
                    next = 0.01
            print("Final next owner is {}".format(next_owner))
            print("Final description is {}".format(desc))
            if desc not in items_owned:
                items_owned[desc] = next_owner
            else:
                print("Condition failed. Items owned dict: {}".format(items_owned))

        print("Final items owned dict: {}".format(items_owned))
        return items_owned


    @staticmethod
    def proof_of_work(last_proof):
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def lastest_block(self):
        return self.chain[-1]
