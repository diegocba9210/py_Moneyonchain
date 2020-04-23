"""
        GNU AFFERO GENERAL PUBLIC LICENSE
           Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN
 @2020
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import os
import logging

from web3 import Web3
from moneyonchain.contract import Contract


class BaseChanger(Contract):
    log = logging.getLogger()

    contract_abi = None
    contract_bin = None

    contract_governor_abi = None
    contract_governor_bin = None

    mode = 'MoC'

    def __init__(self, connection_manager, contract_address=None, contract_abi=None, contract_bin=None):

        super().__init__(connection_manager,
                         contract_address=contract_address,
                         contract_abi=contract_abi,
                         contract_bin=contract_bin)

    def fnx_constructor(self, *tx_parameters, wait_receipt=True):
        """ Constructor deploy """
        sc, content_abi, content_bin = self.connection_manager.load_bytecode_contract(self.contract_abi,
                                                                                      self.contract_bin)
        tx_hash = self.connection_manager.fnx_constructor(sc, *tx_parameters)

        tx_receipt = None
        if wait_receipt:
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)

        return tx_hash, tx_receipt

    def load_governor(self):
        """ Load governor contract"""

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['governor']
        result = self.connection_manager.load_contract(self.contract_governor_abi, contract_address)
        return result


class RDOCMoCSettlementChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCSettlementChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCSettlementChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, input_block_span, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCSettlement']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, input_block_span)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class RDOCMoCInrateStableChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCInrateStableChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/MoCInrateStableChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_rdoc/Governor.bin'))

    mode = 'RDoC'

    def constructor(self, t_min, t_max, t_power, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCInrate']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, t_min, t_max, t_power)

        self.log.info("Deployed contract done!")
        self.log.info(tx_hash)
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(tx_hash)
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class MoCPriceProviderChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/PriceProviderChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/PriceProviderChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi/Governor.bin'))

    mode = 'MoC'

    def constructor(self, price_provider, execute_change=False):

        network = self.connection_manager.network
        contract_address = self.connection_manager.options['networks'][network]['addresses']['MoCState']

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address, Web3.toChecksumAddress(price_provider))

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt


class DexAddTokenPairChanger(BaseChanger):
    log = logging.getLogger()

    contract_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/AddTokenPairChanger.abi'))
    contract_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/AddTokenPairChanger.bin'))

    contract_governor_abi = Contract.content_abi_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.abi'))
    contract_governor_bin = Contract.content_bin_file(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), 'abi_dex/Governor.bin'))

    mode = 'DEX'

    def constructor(self,
                    base_token,
                    secondary_address,
                    init_price,
                    price_precision,
                    execute_change=False):

        network = self.connection_manager.network
        contract_address = Web3.toChecksumAddress(self.connection_manager.options['networks'][network]['addresses']['dex'])

        self.log.info("Deploying new contract...")

        tx_hash, tx_receipt = self.fnx_constructor(contract_address,
                                                   [Web3.toChecksumAddress(base_token)],
                                                   [Web3.toChecksumAddress(secondary_address)],
                                                   [init_price],
                                                   [price_precision])

        self.log.info("Deployed contract done!")
        self.log.info(Web3.toHex(tx_hash))
        self.log.info(tx_receipt)

        self.log.info("Changer Contract Address: {address}".format(address=tx_receipt.contractAddress))

        if execute_change:
            self.log.info("Executing change....")
            governor = self.load_governor()
            tx_hash = self.connection_manager.fnx_transaction(governor, 'executeChange', tx_receipt.contractAddress)
            tx_receipt = self.connection_manager.wait_transaction_receipt(tx_hash)
            self.log.info(Web3.toHex(tx_hash))
            self.log.info(tx_receipt)
            self.log.info("Change successfull!")

        return tx_hash, tx_receipt
