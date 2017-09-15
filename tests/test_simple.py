'''simple.py tests'''

from __future__ import print_function
from T5_cargogen.simple import TradeCargo, BrokerSale
import sys
import logging
import json

if sys.version_info[0] == 3:
    import unittest
    from unittest.mock import patch
else:
    import unittest
    from mock import patch

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

    def test_json_export(self):
        '''Test TradeCargo JSON export'''
        cargo = TradeCargo()
        source_uwp = 'A646930-D'
        source_trade_codes = ['Hi', 'In', 'An']
        cargo.generate_cargo(source_uwp, source_trade_codes)
        jdata = cargo.json_export()
        jdict = json.loads(jdata)
        self.assertTrue(jdict['description'] == cargo.description)
        self.assertTrue(jdict['tech_level'] == cargo.tech_level)
        self.assertTrue(jdict['cost'] == cargo.cost)
        self.assertTrue(jdict['trade_codes'] == cargo.trade_codes)

    def test_json_import(self):
        '''Test TradeCargo JSON import'''
        cargo = TradeCargo()
        jdata = '{"trade_codes": ["Hi", "In"], "cost": 2300, ' +\
            '"description": "Archeologicals", "tech_level": "D"}'
        cargo.json_import(jdata)
        self.assertTrue(cargo.cost == 2300)
        self.assertTrue(cargo.description == 'Archeologicals')
        self.assertTrue(cargo.tech_level == 'D')
        self.assertTrue(cargo.trade_codes == ['Hi', 'In'])

    def test_json_reimport(self):
        '''Test TradeCargo JSON reimport'''
        cargo1 = TradeCargo()
        source_uwp = 'A646930-D'
        source_trade_codes = ['Hi', 'In', 'An']
        cargo1.generate_cargo(source_uwp, source_trade_codes)
        jdata = cargo1.json_export()
        cargo2 = TradeCargo()
        cargo2.json_import(jdata)
        self.assertTrue(cargo1.tech_level == cargo2.tech_level)
        self.assertTrue(cargo1.trade_codes == cargo2.trade_codes)
        self.assertTrue(cargo1.cost == cargo2.cost)
        self.assertTrue(cargo1.description == cargo2.description)


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

    def test_json_export(self):
        '''Test BrokerSale JSON export'''
        cargo = TradeCargo()
        source_uwp = 'A646930-D'
        source_trade_codes = ['Hi', 'In', 'An']
        market_uwp = 'B56789C-A'
        market_trade_codes = ['Ri', 'Pa', 'Ph']
        cargo.generate_cargo(source_uwp, source_trade_codes)
        cargo.generate_sale(market_uwp, market_trade_codes)
        broker = BrokerSale(4, cargo)
        broker.sale()

        jdata = broker.json_export()
        jdict = json.loads(jdata)
        self.assertTrue(broker.skill == jdict['skill'])
        self.assertTrue(broker.commission == jdict['commission'])
        self.assertTrue(broker.actual_value == jdict['actual_value'])
        self.assertTrue(broker.cargo == cargo)

    def test_json_import(self):
        '''Test BrokerSale JSON import'''
        cargo = TradeCargo()
        broker = BrokerSale(0, cargo)

        jdata = '{"cargo": "{\\"price\\": 0, \\"trade_codes\\": [\\"Hi\\", ' +\
                '\\"In\\"], \\"cost\\": 2300, \\"tech_level\\": \\"D\\", ' +\
                '\\"description\\": \\"Exotic Flora\\"}", "skill": 4, ' +\
                '"actual_value": 15600, "commission": 1560}'
        broker.json_import(jdata)
        self.assertTrue(broker.skill == 4)
        self.assertTrue(broker.actual_value == 15600)
        self.assertTrue(broker.commission == 1560)
        self.assertTrue(broker.cargo.tech_level == 'D')
        self.assertTrue(broker.cargo.cost == 2300)
        self.assertTrue(broker.cargo.description == 'Exotic Flora')
        self.assertTrue(broker.cargo.trade_codes == ['Hi', 'In'])

    def test_json_reimport(self):
        '''Test BrokerSale JSON reimport'''
        cargo = TradeCargo()
        empty_cargo = TradeCargo()
        source_uwp = 'A646930-D'
        source_trade_codes = ['Hi', 'In', 'An']
        market_uwp = 'B56789C-A'
        market_trade_codes = ['Ri', 'Pa', 'Ph']
        cargo.generate_cargo(source_uwp, source_trade_codes)
        cargo.generate_sale(market_uwp, market_trade_codes)
        broker1 = BrokerSale(4, cargo)
        broker1.sale()
        jdata = broker1.json_export()
        broker2 = BrokerSale(0, empty_cargo)
        broker2.json_import(jdata)

        self.assertTrue(broker1.skill == broker2.skill)
        self.assertTrue(broker1.actual_value == broker2.actual_value)
        self.assertTrue(broker1.commission == broker2.commission)
        # Can't directly compare cargo as we don't have market world
        self.assertTrue(broker1.cargo.description == broker2.cargo.description)
        self.assertTrue(broker1.cargo.tech_level == broker2.cargo.tech_level)
        self.assertTrue(broker1.cargo.trade_codes == broker2.cargo.trade_codes)
        self.assertTrue(broker1.cargo.cost == broker2.cargo.cost)
