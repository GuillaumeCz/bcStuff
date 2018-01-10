import hashlib

max_nonce = 2 ** 32   # 4 billion


def proof_of_work(header, difficulty_bits):
    target = 2 ** (256-difficulty_bits)

    for nonce in xrange(max_nonce):
        header['nonce'] = nonce
        hash_result = hashlib.sha256(str(header)).hexdigest()

        # check if this is a valid result, below target
        if long(hash_result, 16) < target:
            # print "Success with nonce %d" % nonce
            # print "Hash is %s" % hash_result
            return nonce

    print "Fail after %d (max_nonce) tries" % nonce
    return nonce
