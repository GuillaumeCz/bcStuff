from hashes import *
from block import Block

class Blockchain:
    blocks = []

    def add_block(self, block_pf):
        """ Ajoute un block en param a la chaine de blocks """

        # test si il s'agit du bloc genesis
        if len(self.blocks) != 0:
            # check si previous H est coherent avant ajout a chaine
            if self.check_previousBlockH(block_pf.header['prevBlockH']):
                self.blocks.append(block_pf)
            else:
                print "== Probleme de parent"
                print "= %s" % block_pf.header['prevBlockH']
                print "= %s" % getHashBlock(self.get_topBlock())
        else:
            self.blocks.append(block_pf)

    def get_topBlock(self):
        """ Retourne dernier bloc de la chaine """
        return self.blocks[len(self.blocks)-1]

    def check_previousBlockH(self, previousBlockH):
        """ verification si le H du bloc parent du nouveau bloc correspond a celui du dernier bloc de la chaine """
        if getHashBlock(self.get_topBlock()) == previousBlockH:
            return True
        else:
            return False

    def chainIsValid(self):
        """ Verification que chaque bloc reference bien celui le precedant dans la chaine """
        for i in range(1, len(self.blocks)):
            prev_block = self.blocks[i-1]
            cur_block = self.blocks[i]
            if cur_block.header['prevBlockH'] != getHashBlock(prev_block):
                return False
        return True

    def getBlock(self, blocHash_pf):
        for block in self.blocks:
            if getHashBlock(block) == blocHash_pf:
                return block
        return None

    def getTx(self, txHash_pf):
        for block in self.blocks:
            for tx in block.transactionFiles:
                if getHash(tx) == txHash_pf:
                    return tx
        return None


    def isInBlockchain(self, txHash_pf):
        for block in self.blocks:
            for tx in block.transactionFiles:
                if getHash(tx) == txHash_pf:
                    return True

        return False

    def display_blocks(self):
        """ Affichage des blocks de la chaine """
        buf = ""
        cpt = 0

        for block in self.blocks:
            buf += "Block N. %d\n" % cpt
            buf += "H \t%s\n" % getHashBlock(block)
            buf += "Header \t%s \n\n" % str(block.header)
            cpt += 1

        buf += "Is chain valid ? %r" % self.chainIsValid()
        print buf
