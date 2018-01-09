from flask import render_template
from ..models.blockchain import *
from ..helpers.proof_of_work import *
from ..helpers.hashes import *
from ..models.block import Block

blockchain = Blockchain()
t_hashes = []

def mine(block):
    """ Minage, renvoie bloc finalise et pret a envoyer dans bc """
    return block.validateSelf()

def create_block():
    if len(blockchain.blocks) != 0:
        new_block = Block(getHashBlock(blockchain.get_topBlock()))
    else:
        new_block = Block('00')

    new_block.validateSelf()
    t_hashes.append(getHashBlock(new_block))
    blockchain.add_block(new_block)

def blockchainCtrl():
    create_block()
    create_block()
    return render_template('blockchain.html', title="Blockchain", blockchain=blockchain, hashes=t_hashes)
