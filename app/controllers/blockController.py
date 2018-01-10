from flask import render_template
from ..models.block import Block
from ..helpers.hashes import getHashBlock


def blockCtrl():
    block = Block(0)
    block.validateSelf()
    return render_template(
        'blockPage.html',
        title='Block',
        block=block,
        block_hash=getHashBlock(block))
