import hashlib
import time
from merkle import *
from proof_of_work import *

class Block:

    def __init__(self, prevBlockH_pf):
        self.header = {
            'version' : 2,
            'prevBlockH' : prevBlockH_pf,
            'timestamp' : time.time(),
            'difficultyTarget' : 15,
            'nonce' : 0,
            'merkleRoot' : ""
        }
        self.transactions = []

    def getHash(self):
        """ retourne le H du block """
        return hashlib.sha256(str(self.header)).hexdigest()

    def calculate_merkleRoot(self):
        """ calcul markle tree root et le place dans le header """
        mt = MerkleTree(str(self.transactions))
        mt.build()
        self.header['merkleRoot'] = mt.root.val.encode('hex')

    def calculate_pow(self):
        """ calcul du bon nonce en fonction du bloc et de la difficulte  et le place dans header """
        self.header['nonce'] = proof_of_work(self.header, self.header['difficultyTarget'])

    def validateSelf(self):
        """ shortcut pour process validation, MAJ merkle + calcul nonce """
        self.calculate_merkleRoot()
        self.calculate_pow()

