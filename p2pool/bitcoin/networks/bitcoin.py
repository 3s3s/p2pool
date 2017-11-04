import os
import platform

from twisted.internet import defer

from .. import data, helper
from p2pool.util import pack


P2P_PREFIX = 'f9beb4d9'.decode('hex')
P2P_PORT = 33333
ADDRESS_VERSION = 50
RPC_PORT = 33332
RPC_CHECK = defer.inlineCallbacks(lambda bitcoind: defer.returnValue(
            (yield helper.check_genesis_block(bitcoind, '00000000445999647df11eba1ac9c2fbb52c5c271417292e13b3282d004a3dc3')) and
            not (yield bitcoind.rpc_getinfo())['testnet']
        ))
SUBSIDY_FUNC = lambda height: 50*100000000 >> (height + 1)//210000
POW_FUNC = data.hash256
BLOCK_PERIOD = 600 # s
SYMBOL = 'MC'
CONF_FILE_FUNC = lambda: os.path.join(os.path.join(os.environ['APPDATA'], 'Marycoin') if platform.system() == 'Windows' else os.path.expanduser('~/Library/Application Support/Marycoin/') if platform.system() == 'Darwin' else os.path.expanduser('~/.marycoin'), 'marycoin.conf')
BLOCK_EXPLORER_URL_PREFIX = 'https://mc.multicoins.org/block/'
ADDRESS_EXPLORER_URL_PREFIX = 'https://mc.multicoins.org/address/'
TX_EXPLORER_URL_PREFIX = 'https://mc.multicoins.org/tx/'
SANE_TARGET_RANGE = (2**256//2**32//1000 - 1, 2**256//2**32 - 1)
DUMB_SCRYPT_DIFF = 1
DUST_THRESHOLD = 0.00001
