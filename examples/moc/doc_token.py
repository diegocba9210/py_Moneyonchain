from moneyonchain.manager import ConnectionManager
from moneyonchain.token import DoCToken


network = 'mocTestnet'
connection_manager = ConnectionManager(network=network)
print("Connecting to %s..." % network)
print("Connected: {conectado}".format(conectado=connection_manager.is_connected))

account = '0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3'

print("Connecting to DoCToken")
doc_token = DoCToken(connection_manager)
print("Token Name: {0}".format(doc_token.name()))
print("Token Symbol: {0}".format(doc_token.symbol()))
print("Total Supply: {0}".format(doc_token.total_supply()))
print("Account: {0} Balance DOC: {1}".format(account, doc_token.balance_of(account)))

"""
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3101.857468416503539918
Insert:
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3088.857468416503539918
Match:
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3068.857468416503539918

1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3068.857468416503539918
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3055.857468416503539918
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3055.857468416503539918


1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3055.857468416503539918
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3055.857468416503539918
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3068.844468416503539918

1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3068.844468416503539918
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3068.844468416503539918


1.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3068.844468416503539918
2.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3055.844468416503539918
3.
Account: 0xCD8A1c9aCc980ae031456573e34dC05cD7daE6e3 Balance DOC: 3055.844468416503539918

"""