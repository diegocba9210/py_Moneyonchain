"""
                    GNU AFFERO GENERAL PUBLIC LICENSE
                       Version 3, 19 November 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

 THIS IS A PART OF MONEY ON CHAIN PACKAGE
 by Martin Mulone (martin.mulone@moneyonchain.com)

"""

import logging
from web3 import Web3
from web3.exceptions import BlockNotFound
import datetime


class BaseEvent(object):
    name = "BaseEvent"
    hours_delta = 0

    def print_row(self):
        print('\t'.join(self.columns()))
        print('\t'.join(str(v) for v in self.row()))


class MoCExchangeRiskProMint(BaseEvent):

    name = "RiskProMint"

    def __init__(self, connection_manager, event):

        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'Amount', 'reserveTotal', 'commission', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCExchangeRiskProWithDiscountMint(BaseEvent):
    name = "RiskProWithDiscountMint"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        ts = connection_manager.block_timestamp(self.blockNumber)
        dt = ts - datetime.timedelta(hours=self.hours_delta)
        self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        self.riskProTecPrice = event['args']['riskProTecPrice']
        self.riskProDiscountPrice = event['args']['riskProDiscountPrice']
        self.amount = event['args']['amount']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'riskProTecPrice', 'riskProDiscountPrice', 'amount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['riskProTecPrice'] = Web3.fromWei(self.riskProTecPrice, 'ether')
        d_event['riskProDiscountPrice'] = Web3.fromWei(self.riskProDiscountPrice, 'ether')
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['riskProTecPrice']), '.18f'),
                format(float(d_event['riskProDiscountPrice']), '.18f'),
                format(float(d_event['amount']), '.18f')]


class MoCExchangeRiskProRedeem(BaseEvent):
    name = "RiskProRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'amount', 'reserveTotal', 'commission', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCExchangeStableTokenMint(BaseEvent):
    name = "StableTokenMint"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'amount', 'reserveTotal', 'commission', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCExchangeStableTokenRedeem(BaseEvent):
    name = "StableTokenRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'amount', 'reserveTotal', 'commission', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCExchangeFreeStableTokenRedeem(BaseEvent):
    name = "FreeStableTokenRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.commission = event['args']['commission']
        self.interests = event['args']['interests']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Account', 'Amount', 'ReserveTotal', 'Commission', 'Interests', 'ReservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['interests'] = Web3.fromWei(self.interests, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['interests']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCExchangeRiskProxMint(BaseEvent):
    name = "RiskProxMint"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.bucket = 'X2'
        self.account = event['args']['account']
        self.amount = event['args']['amount']
        self.reserveTotal = event['args']['reserveTotal']
        self.interests = event['args']['interests']
        self.leverage = event['args']['leverage']
        self.commission = event['args']['commission']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Bucket', 'Account', 'Amount', 'Reserve Total', 'Interests',  'Leverage',  'Commission',  'Reserve Price']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['bucket'] = self.bucket
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['interests'] = Web3.fromWei(self.interests, 'ether')
        d_event['leverage'] = Web3.fromWei(self.leverage, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['bucket'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['interests']), '.18f'),
                format(float(d_event['leverage']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCExchangeRiskProxRedeem(BaseEvent):
    name = "RiskProxRedeem"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.bucket = 'X2'
        self.account = event['args']['account']
        self.amount = Web3.fromWei(event['args']['amount'], 'ether')
        self.reserveTotal = Web3.fromWei(event['args']['reserveTotal'], 'ether')
        self.interests = Web3.fromWei(event['args']['interests'], 'ether')
        self.leverage = Web3.fromWei(event['args']['leverage'], 'ether')
        self.commission = Web3.fromWei(event['args']['commission'], 'ether')
        self.reservePrice = Web3.fromWei(event['args']['reservePrice'], 'ether')

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'Bucket', 'Account', 'Amount', 'Reserve Total', 'Interests',  'Leverage',  'Commission',  'Reserve Price']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['bucket'] = self.bucket
        d_event['account'] = self.account
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')
        d_event['reserveTotal'] = Web3.fromWei(self.reserveTotal, 'ether')
        d_event['interests'] = Web3.fromWei(self.interests, 'ether')
        d_event['leverage'] = Web3.fromWei(self.leverage, 'ether')
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['bucket'],
                d_event['account'],
                format(float(d_event['amount']), '.18f'),
                format(float(d_event['reserveTotal']), '.18f'),
                format(float(d_event['interests']), '.18f'),
                format(float(d_event['leverage']), '.18f'),
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


# SETTLEMENT

class MoCSettlementRedeemRequestProcessed(BaseEvent):
    name = "RedeemRequestProcessed"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''

        self.redeemer = event['args']['redeemer']
        self.commission = event['args']['commission']
        self.amount = event['args']['amount']

    @staticmethod
    def columns():
        columns = ['Block Nº',  'Timestamp', 'Account', 'Commission', 'Amount']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['redeemer'] = self.redeemer
        d_event['commission'] = Web3.fromWei(self.commission, 'ether')
        d_event['amount'] = Web3.fromWei(self.amount, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['redeemer'],
                format(float(d_event['commission']), '.18f'),
                format(float(d_event['amount']), '.18f')]


class MoCSettlementSettlementRedeemStableToken(BaseEvent):
    name = "SettlementRedeemStableToken"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''

        self.queueSize = event['args']['queueSize']
        self.accumCommissions = event['args']['accumCommissions']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'queueSize', 'accumCommissions', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['queueSize'] = self.queueSize
        d_event['accumCommissions'] = Web3.fromWei(self.accumCommissions, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['queueSize'],
                format(float(d_event['accumCommissions']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCSettlementSettlementCompleted(BaseEvent):
    name = "SettlementCompleted"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''
        self.commissionsPayed = event['args']['commissionsPayed']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp', 'commissionsPayed']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['commissionsPayed'] = Web3.fromWei(self.commissionsPayed, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['commissionsPayed']), '.18f')]


class MoCSettlementSettlementDeleveraging(BaseEvent):
    name = "SettlementDeleveraging"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''

        self.leverage = event['args']['leverage']
        self.riskProxPrice = event['args']['riskProxPrice']
        self.reservePrice = event['args']['reservePrice']
        self.startBlockNumber = event['args']['startBlockNumber']

    @staticmethod
    def columns():
        columns = ['Block Nº',  'Timestamp', 'leverage', 'riskProxPrice', 'reservePrice', 'startBlockNumber']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['leverage'] = Web3.fromWei(self.leverage, 'ether')
        d_event['riskProxPrice'] = Web3.fromWei(self.riskProxPrice, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')
        d_event['startBlockNumber'] = self.startBlockNumber

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                format(float(d_event['leverage']), '.18f'),
                format(float(d_event['riskProxPrice']), '.18f'),
                format(float(d_event['reservePrice']), '.18f'),
                d_event['startBlockNumber']]


class MoCSettlementSettlementStarted(BaseEvent):
    name = "SettlementStarted"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''

        self.stableTokenRedeemCount = event['args']['stableTokenRedeemCount']
        self.deleveragingCount = event['args']['deleveragingCount']
        self.riskProxPrice = event['args']['riskProxPrice']
        self.reservePrice = event['args']['reservePrice']

    @staticmethod
    def columns():
        columns = ['Block Nº',  'Timestamp', 'stableTokenRedeemCount', 'deleveragingCount', 'riskProxPrice', 'reservePrice']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['stableTokenRedeemCount'] = self.stableTokenRedeemCount
        d_event['deleveragingCount'] = self.deleveragingCount
        d_event['riskProxPrice'] = Web3.fromWei(self.riskProxPrice, 'ether')
        d_event['reservePrice'] = Web3.fromWei(self.reservePrice, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['stableTokenRedeemCount'],
                d_event['deleveragingCount'],
                format(float(d_event['riskProxPrice']), '.18f'),
                format(float(d_event['reservePrice']), '.18f')]


class MoCSettlementRedeemRequestAlter(BaseEvent):
    name = "RedeemRequestAlter"

    def __init__(self, connection_manager, event):
        self.blockNumber = event['blockNumber']
        try:
            ts = connection_manager.block_timestamp(self.blockNumber)
            dt = ts - datetime.timedelta(hours=self.hours_delta)
            self.timestamp = dt.strftime("%Y-%m-%d %H:%M:%S")
        except BlockNotFound:
            self.timestamp = ''

        self.redeemer = event['args']['redeemer']
        self.isAddition = event['args']['isAddition']
        self.delta = event['args']['delta']

    @staticmethod
    def columns():
        columns = ['Block Nº', 'Timestamp',  'address', 'isAddition', 'delta']
        return columns

    def formatted(self):
        d_event = dict()
        d_event['blockNumber'] = self.blockNumber
        d_event['timestamp'] = self.timestamp
        d_event['redeemer'] = self.redeemer
        d_event['isAddition'] = self.isAddition
        d_event['delta'] = Web3.fromWei(self.delta, 'ether')

        return d_event

    def row(self):
        d_event = self.formatted()
        return [d_event['blockNumber'],
                d_event['timestamp'],
                d_event['redeemer'],
                d_event['isAddition'],
                format(float(d_event['delta']), '.18f')]
