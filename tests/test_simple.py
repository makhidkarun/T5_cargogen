'''simple.py tests'''

import sys
import logging

if sys.version_info[0] == 3:
    import unittest
    from unittest.mock import patch
else:
    import unittest
    from mock import patch

from T5_cargogen.simple import TradeCargo
from T5_cargogen.simple import BrokerSale

LOGGER = logging.getLogger(__name__)
logging.basicConfig(
    # format='%(asctime)-15s %(name)s %(funcName)s(): %(message)s',
    format='%(relativeCreated)d %(name)s %(funcName)s(): %(message)s',
    level=logging.INFO
)


class TestTradeCargo(unittest.TestCase):
    '''Test trade good class'''
    def test_trade_codes(self):
        '''Test trade codes reduction for Efate'''
        uwp = 'A646930-D'
        trade_codes = ['Hi', 'In', 'An']
        cargo = TradeCargo()
        cargo.generate_cargo(uwp, trade_codes)
        self.assertTrue(cargo.trade_codes == ['Hi', 'In'])

    def test_purchase(self):
        '''Test purchase on Efate'''
        cargo = TradeCargo()
        # Test with Efat data
        uwp = 'A646930-D'
        trade_codes = ['Hi', 'In', 'An']
        cargo.generate_cargo(uwp, trade_codes)
        self.assertTrue(cargo.cost == 2300)

    def test_sale(self):
        '''Test purchase of Efate cargo on Alell'''
        cargo = TradeCargo()
        source_uwp = 'A646930-D'
        source_trade_codes = ['Hi', 'In', 'An']
        market_uwp = 'B56789C-A'
        market_trade_codes = ['Ri', 'Pa', 'Ph']
        cargo.generate_cargo(source_uwp, source_trade_codes)
        cargo.generate_sale(market_uwp, market_trade_codes)
        self.assertTrue(cargo.price == 7800)


class TestBroker(unittest.TestCase):
    '''Test broker'''
    class MockFlux(object):
        '''Mock flux roll'''
        @staticmethod
        def flux(_):
            '''Roll, return -1'''
            return -1

    @patch('T5_cargogen.simple.BrokerSale.flux', MockFlux.flux)
    def test_broker_sale(self):
        '''Test sale with broker'''
        cargo = TradeCargo()
        source_uwp = 'A646930-D'
        source_trade_codes = ['Hi', 'In', 'An']
        market_uwp = 'B56789C-A'
        market_trade_codes = ['Ri', 'Pa', 'Ph']
        cargo.generate_cargo(source_uwp, source_trade_codes)
        cargo.generate_sale(market_uwp, market_trade_codes)
        broker = BrokerSale(4, cargo)
        broker.sale()
        self.assertTrue(broker.actual_value == 8580)
