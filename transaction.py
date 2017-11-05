
class Transaction:

    def __init__(self, inputs_pf, outputs_pf):
        self.version = "2"
        self.inputCpt = len(inputs_pf)
        self.inputs = inputs_pf
        self.outputCpt = len(outputs_pf)
        self.outputs = outputs_pf
        self.locktime = 0

    def getHash(self):
        return hashlib.sha256(str(self)).hexdigest()

    
class Utxo:
    def __init__(self, montant_pf):
        self.montant = montant_pf

