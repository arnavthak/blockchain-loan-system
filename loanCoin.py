import hashlib
import time

class Block:
    def __init__(self, index, proof_no, prev_hash, description, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.description = description
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no,
                                              self.prev_hash, self.description,
                                              self.data, self.timestamp)
        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no,
                                               self.prev_hash, self.description,
                                               self.data, self.timestamp)

class BlockChain:
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0, description=0)

    def construct_block(self, proof_no, prev_hash, description):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            description=description,
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
        return True

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
