# example of proof-of-work

import hashlib
import time

max_nonce = 2 ** 32 # 4 billion

def proof_of_work(header, difficulty_bits):
    target = 2 ** (256-difficulty_bits)

    for nonce in xrange(max_nonce):
        hash_result = hashlib.sha256(str(header)+str(nonce)).hexdigest()

        # check if this is a valid result, below target
        if long(hash_result, 16) < target:
            print "Success with nonce %d" % nonce
            print "Hash is %s" % hash_result
            return (hash_result, nonce)

    print "Fail after %d (max_nonce) tries" % nonce
    return  nonce

if __name__ == '__main__':
    nonce = 0
    hash_result = ''

    # difficulty from 0 to 31 bits
    for difficulty_bits in xrange(32):
        difficulty = 2 ** difficulty_bits
        print "\n\nDifficulty: %ld (%d bits)" % (difficulty, difficulty_bits)

        print "Starting search..."

        # checkpoint the current time
        start_time = time.time()

        # New block witch includes H from previous block, ici block = string
        new_block = 'test block with tx' + hash_result

        # find a valid nonce for the new block
        (hash_result, nonce) = proof_of_work(new_block, difficulty_bits)

        # checkpoint how long it tooks
        end_time = time.time()

        elapsed_time = end_time - start_time
        print "Elapsed Time :  %.4f seconds" % elapsed_time

        if elapsed_time > 0:
            # estimated h/sec
            hash_power = float(long(nonce)/elapsed_time)
            print "Hash power : %ld hashes/sec" % hash_power
