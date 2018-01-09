import hashlib

def getHash(toHash):
    return hashlib.sha256(toHash).hexdigest()

def getHashBlock(block):
    return getHash(str(block.header))
