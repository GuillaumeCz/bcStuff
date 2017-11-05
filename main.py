from wallet import Wallet
from transaction import Utxo
from node import Node

ut1 = Utxo(12)
node = Node()
w = Wallet(node)
w.utxo.append(ut1)

w.create_tx(10)
w.send_tx()

node.process()
w.create_tx(1)
w.send_tx()

node.process()

node.blockchain.display_blocks()
