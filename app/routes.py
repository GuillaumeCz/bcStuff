from app import app
from controllers.indexController import indexCtrl
from controllers.blockController import blockCtrl
from controllers.blockchainController import blockchainCtrl

@app.route('/')
@app.route('/index')
def index():
    return indexCtrl()

@app.route('/block')
def block():
    return blockCtrl()

@app.route('/blockchain')
def blockchain():
    return blockchainCtrl()
