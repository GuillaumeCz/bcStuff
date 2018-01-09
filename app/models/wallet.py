from fileTransaction import FileTransaction
from node import Node

class Wallet:

    def __init__(self, node_pf):
        self.fileTransactions = []
        self.nodes = [node_pf]

    def create_fileTx(self, filePath_pf):
        """
        creation d'une tx avec simplement les utxo dispos
        Test avec la premiere utxo dispo a evoluer
        """
        fileTx = FileTransaction(filePath_pf)
        self.fileTransactions.append(fileTx)

    def send_fileTx(self):
        """ Envoie nouvelle tx au premier des noeuds connus """
        for fTx in self.fileTransactions:
            self.nodes[0].add_fileTx(fTx)
        self.fileTransactions = []
