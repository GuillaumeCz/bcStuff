from block import Block 

class Blockchain:
    blocks = []
    
    def add_block(self, block_pf):
        """ Ajoute un block en param à la chaine de blocks """

        # test si il s'agit du bloc genesis
        if len(self.blocks) != 0:
            # check si previous H est coherent avant ajout a chaine 
            if self.check_previousBlockH(block_pf.header['prevBlockH']):
                block_pf.validateSelf()
                self.blocks.append(block_pf)
            else:
                print "== Probleme de parent"
                print "= %s" % block_pf.header['prevBlockH']
                print "= %s" % self.get_topBlock().getHash()
        else:
            block_pf.validateSelf()
            self.blocks.append(block_pf)

    def get_topBlock(self):
        """ Retourne dernier bloc de la chaine """
        return self.blocks[len(self.blocks)-1]

    def check_previousBlockH(self, previousBlockH):
        """ verification si le H du bloc parent du nouveau bloc correspond a celui du dernier bloc de la chaine """
        if self.get_topBlock().getHash() == previousBlockH:
            return True
        else:
            return False

    def chainIsValid(self):
        """ Verification que chaque bloc reference bien celui le precedant dans la chaine """
        for i in range(1, len(self.blocks)):
            prev_block = self.blocks[i-1]
            cur_block = self.blocks[i]
            if cur_block.header['prevBlockH'] != prev_block.getHash():
                return False
        return True
    
    def display_blocks(self):
        """ Affichage des blocks de la chaine """
        buf = ""
        cpt = 0

        for block in self.blocks:
            buf += "Block N. %d\n" % cpt
            buf += "H \t%s\n" % block.getHash()
            buf += "Header \t%s \n\n" % str(block.header)
            cpt += 1

        buf += "Is chain valid ? %r" % self.chainIsValid()
        print buf

