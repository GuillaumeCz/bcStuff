from flask import render_template
from ..models.block import *
from ..helpers.hashes import *

def blockCtrl():
    block = Block(0)
    block.validateSelf()
    return render_template('block.html', title='Block', block=block, block_hash=getHashBlock(block))
