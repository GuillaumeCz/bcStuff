from transaction import Utxo
from transaction import Transaction
from node import Node

class Wallet:

    def __init__(self, node_pf):
        self.utxo = []
        self.nodes = [node_pf]

    def create_tx(self, montant_pf):
        """ 
        creation d'une tx avec simplement les utxo dispos 
        Test avec la premiere utxo dispo a evoluer 
        """
        inputs = self.utxo
        outputs = []
        if inputs[0].montant > montant_pf:
            change = inputs[0].montant - montant_pf
            outputs.append(Utxo(change))
            outputs.append(Utxo(montant_pf))
            self.new_tx = Transaction(inputs, outputs)
        elif inputs.montant == montant_pf:
            outputs.append(inputs)
            self.new_tx = Transaction(inputs, outputs)
        else:
            print "Not enought cash bro..."
        
    def send_tx(self):
        """ Envoie nouvelle tx au premier des noeuds connus """
        self.nodes[0].add_tx(self.new_tx)
