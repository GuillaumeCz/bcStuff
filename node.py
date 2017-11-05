from blockchain import Blockchain
from block import Block
from proof_of_work import *

class Node:

    def __init__(self):
        self.blockchain = Blockchain()
        self.memPool = [];

    def create_block(self):
        """ Creation d'un bloc avec tx de memPool """ 
        if len(self.blockchain.blocks) != 0:
            self.new_block = Block(self.blockchain.get_topBlock().getHash())
        else:
            self.new_block = Block('00')
        
        for tx in self.memPool:
            self.new_block.transactions.append(tx)

        self.clear_memPool()
    
    def add_tx(self, tx_pf):
        """ Ajout d'une tx dans memPool """
        self.memPool.append(tx_pf)

    def clear_memPool(self):
        """ vide memPool """
        self.memPool = []

    def mine(self):
        """ Minage, renvoie bloc finalise et pret a envoyer dans bc """
        if self.new_block:
            self.new_block.validateSelf()

    def add_blockToBlockchain(self):
        """ Ajoute un bloc a la bc """
        self.blockchain.add_block(self.new_block)

    def process(self):
        """ shortcut pour exec process crea + minage + ajout dans bc """ 
        self.create_block()
        self.mine()
        self.add_blockToBlockchain()

