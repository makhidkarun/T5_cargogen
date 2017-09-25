'''test_trade_codes.py'''

import unittest
from app.main.trade_codes import Uwp, TradeCodes


class TestUwp(unittest.TestCase):
    '''Test UWP methods'''
    def test_valid_uwp(self):
        '''Test UWP for validity'''
        uwp = Uwp('B655404-A')
        print uwp.starport
        self.assertTrue(uwp.starport == 'B')
        self.assertTrue(uwp.size == '6')
        self.assertTrue(uwp.atmosphere == '5')
        self.assertTrue(uwp.hydrographics == '5')
        self.assertTrue(uwp.population == '4')
        self.assertTrue(uwp.government == '0')
        self.assertTrue(uwp.law_level == '4')
        self.assertTrue(uwp.tech_level == 'A')

    def test_invalid_uwp_type(self):
        '''Test UWP for TypeError'''
        with self.assertRaises(TypeError):
            uwp = Uwp(6)

    def test_invalid_uwp_string(self):
        '''Test UWP for malformed string'''
        with self.assertRaises(ValueError):
            uwp = Uwp('Not a valid UWP')

    def test_str(self):
        '''Test Uwp str()'''
        planet = 'B655404-A'
        uwp = Uwp(planet)
        self.assertTrue(str(uwp) == planet)


class TestTradeCodes(unittest.TestCase):
    '''Test TradeCodes class'''
    def test_list(self):
        '''Test TradeCodes list()'''
        # TCs for B655404-A are [Ga Ni Pa]
        tcs = TradeCodes(Uwp('B655404-A'))
        self.assertIsInstance(tcs.list(), list)
        self.assertTrue('Ga' in tcs.list())
        self.assertTrue('Ni' in tcs.list())
        self.assertTrue('Pa' in tcs.list())

    def test_str(self):
        '''Test TradeCodes str()'''
        # TCs for B655404-A are [Ga Ni Pa]
        tcs = TradeCodes(Uwp('B655404-A'))
        self.assertIsInstance(str(tcs), str)
        self.assertTrue(str(tcs) == 'Ga Ni Pa')


class TestTradeCodesPlanetary(unittest.TestCase):
    '''Test planetary trade codes'''
    def test_as(self):
        '''Test trade code As'''
        tcs = TradeCodes(Uwp('A000000-0'))
        self.assertTrue('As' in tcs.trade_codes)

    def test_de(self):
        '''Test trade code De'''
        uwp = Uwp('A400000-0')
        for atm in '23456789':
            uwp.atmosphere = atm
            tcs = TradeCodes(uwp)
            self.assertTrue('De' in tcs.trade_codes)

    def test_fl(self):
        '''Test trade code Fl'''
        uwp = Uwp('A400000-0')
        for atm in 'ABC':
            for hyd in '123456778A':
                uwp.atmosphere = atm
                uwp.hydrographics = hyd
                tcs = TradeCodes(uwp)
                self.assertTrue('Fl' in tcs.trade_codes)

    def test_ga(self):
        '''Test trade code Ga'''
        uwp = Uwp('A000000-0')
        for siz in '678':
            for atm in '568':
                for hyd in '567':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertTrue('Ga' in tcs.trade_codes)

    def test_he(self):
        '''Test trade code He'''
        uwp = Uwp('A000000-0')
        for siz in '3456789ABC':
            for atm in '2479ABC':
                for hyd in '012':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertTrue('He' in tcs.trade_codes)

    def test_ic(self):
        '''Test trade code Ic'''
        uwp = Uwp('A400000-0')
        for atm in '01':
            for hyd in '123456789A':
                uwp.atmosphere = atm
                uwp.hydrographics = hyd
                tcs = TradeCodes(uwp)
                self.assertTrue('Ic' in tcs.trade_codes)

    def test_oc(self):
        '''Test trade code Oc'''
        uwp = Uwp('A00A000-0')
        for siz in 'ABCDEF':
            for atm in '3456789ABC':
                uwp.size = siz
                uwp.atmosphere = atm
                tcs = TradeCodes(uwp)
                self.assertTrue('Oc' in tcs.trade_codes)

    def test_va(self):
        '''Test trade code Va'''
        uwp = Uwp('A401000-0')
        tcs = TradeCodes(uwp)
        self.assertTrue('Va' in tcs.trade_codes)

    def test_wa(self):
        '''Test trade code Wa'''
        uwp = Uwp('A40A000-0')
        for siz in '3456789A':
            for atm in '3456789':
                uwp.size = siz
                uwp.atmosphere = atm
                tcs = TradeCodes(uwp)
                self.assertTrue('Wa' in tcs.trade_codes)


class TestTradeCodesPlanetaryExclude(unittest.TestCase):
    '''Test planetary trade codes - exclusion'''
    def test_not_as(self):
        '''Test trade code not As'''
        uwp = Uwp('A000000-0')
        for siz in '123456789A':
            for atm in '123456789ABC':
                for hyd in '123456789A':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertFalse('As' in tcs.trade_codes)

    def test_not_de(self):
        '''Test trade code not De'''
        uwp = Uwp('A700000-0')
        for atm in '0123456789':
            for hyd in '123456789A':
                uwp.atmosphere = atm
                uwp.hydrographics = hyd
                tcs = TradeCodes(uwp)
                self.assertFalse('De' in tcs.trade_codes)

    def test_not_fl(self):
        '''Test trade code not Fl'''
        uwp = Uwp('A700000-0')
        for atm in '01234567899':
            uwp.atmosphere = atm
            tcs = TradeCodes(uwp)
            self.assertFalse('Fl' in tcs.trade_codes)

    def test_not_ga(self):
        '''Test trade code not Ga'''
        uwp = Uwp('A000000-0')
        for siz in '0123459ABC':
            for atm in '0123459ABC':
                for hyd in '0123489A':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Ga' in tcs.trade_codes)

    def test_not_he(self):
        '''Test trade code not He'''
        uwp = Uwp('A000000-0')
        for siz in '01':
            for atm in '013568':
                for hyd in '3456789A':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertFalse('He' in tcs.trade_codes)

    def test_not_ic(self):
        '''Test trade code not Ic'''
        uwp = Uwp('A600000-0')
        for atm in '23456789ABC':
            uwp.atmosphere = atm
            tcs = TradeCodes(uwp)
            self.assertFalse('Ic' in tcs.trade_codes)

    def test_not_oc(self):
        '''Test trade code not Oc'''
        uwp = Uwp('A000000-0')
        for siz in '0123456789':
            for atm in '012':
                for hyd in '0123456789':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Oc' in tcs.trade_codes)

    def test_not_va(self):
        '''Test trade code not Va'''
        uwp = Uwp('A600000-0')
        for atm in '123456789ABC':
            for hyd in '123456789A':
                uwp.atmosphere = atm
                uwp.hydrographics = hyd
                tcs = TradeCodes(uwp)
                self.assertFalse('Va' in tcs.trade_codes)

    def test_not_wa(self):
        '''Test trade code not Wa'''
        uwp = Uwp('A000000-0')
        for siz in '012BC':
            for atm in '012ABC':
                for hyd in '0123456789':
                    uwp.size = siz
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Wa' in tcs.trade_codes)


class TestTradeCodesPopulation(unittest.TestCase):
    '''Test population trade codes'''
    def test_di(self):
        '''Test trade code Di'''
        uwp = Uwp('X600000-2')
        tcs = TradeCodes(uwp)
        self.assertTrue('Di' in tcs.trade_codes)

    def test_ba(self):
        '''Test trade code Ba'''
        uwp = Uwp('X766000-0')
        tcs = TradeCodes(uwp)
        self.assertTrue('Ba' in tcs.trade_codes)

    def test_lo(self):
        '''Test trade code Lo'''
        uwp = Uwp('D644000-0')
        for pop in '123':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertTrue('Lo' in tcs.trade_codes)

    def test_ni(self):
        '''Test trade code Ni'''
        uwp = Uwp('D644000-0')
        for pop in '456':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertTrue('Ni' in tcs.trade_codes)

    def test_ph(self):
        '''Test trade code Ph'''
        uwp = Uwp('B755888-4')
        tcs = TradeCodes(uwp)
        self.assertTrue('Ph' in tcs.trade_codes)

    def test_hi(self):
        '''Test trade code Hi'''
        uwp = Uwp('D755099-9')
        for pop in '9ABCDEF':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertTrue('Hi' in tcs.trade_codes)


class TestTradeCodesPopulationExclude(unittest.TestCase):
    '''Test population trade codes -- exclusion'''
    def test_not_di(self):
        '''Test trade code not Di'''
        uwp = Uwp('X766000-0')
        for pop in '123456789ABCDEF':
            for gov in '123456789ABCDEF':
                for law in '123456789ABCDEFGHJ':
                    uwp.population = pop
                    uwp.government = gov
                    uwp.law_level = law
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Di' in tcs.trade_codes)

    def test_not_ba(self):
        '''Test trade code not Ba'''
        uwp = Uwp('X755000-0')
        for pop in '123456789A':
            for gov in '123456789AB':
                for law in '123456789A':    # Assume the rest are OK
                    for tech in '123456':   # Assume the rest are OK
                        for starport in 'ABCD':
                            uwp.starport = starport
                            uwp.population = pop
                            uwp.government = gov
                            uwp.law_level = law
                            uwp.tech_level = tech
                            tcs = TradeCodes(uwp)
                            self.assertFalse('Ba' in tcs.trade_codes)

    def test_not_lo(self):
        '''Test trade code not Lo'''
        uwp = Uwp('C755055-5')
        for pop in '0456789ABCDEF':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertFalse('Lo' in tcs.trade_codes)

    def test_not_ni(self):
        '''Test trade code not Ni'''
        uwp = Uwp('C755055-5')
        for pop in '0123789ABC':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertFalse('Ni' in tcs.trade_codes)

    def test_not_ph(self):
        '''Test trade code not Ph'''
        uwp = Uwp('C755055-5')
        for pop in '012345679ABCDEF':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertFalse('Ph' in tcs.trade_codes)

    def test_not_hi(self):
        '''Test trade code not Hi'''
        uwp = Uwp('C755055-5')
        for pop in '012345678':
            uwp.population = pop
            tcs = TradeCodes(uwp)
            self.assertFalse('Hi' in tcs.trade_codes)


class TestTradeCodesEconomic(unittest.TestCase):
    '''Test economic trade codes'''
    def test_pa(self):
        '''Test trade code Pa'''
        uwp = Uwp('C700055-5')
        for atm in '456789':
            for hyd in '45678':
                for pop in '48':
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    uwp.population = pop
                    tcs = TradeCodes(uwp)
                    self.assertTrue('Pa' in tcs.trade_codes)

    def test_ag(self):
        '''Test trade code Ag'''
        uwp = Uwp('C700055-5')
        for atm in '456789':
            for hyd in '45678':
                for pop in '567':
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    uwp.population = pop
                    tcs = TradeCodes(uwp)
                    self.assertTrue('Ag' in tcs.trade_codes)

    def test_na(self):
        '''Test trade code Na'''
        uwp = Uwp('C700055-5')
        for atm in '0123':
            for hyd in '0123':
                for pop in '6789ABCDEF':
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    uwp.population = pop
                    tcs = TradeCodes(uwp)
                    self.assertTrue('Na' in tcs.trade_codes)

    def test_px(self):
        '''Test trade code Px'''
        uwp = Uwp('C700055-5')
        for atm in '23AB':
            for hyd in '12345':
                for pop in '3456':
                    for law in '6789':
                        # Also need to check MW
                        uwp.atmosphere = atm
                        uwp.hydrographics = hyd
                        uwp.population = pop
                        uwp.law_level = law
                        tcs = TradeCodes(uwp)
                        self.assertTrue('Px' in tcs.trade_codes)

    def test_pi(self):
        '''Test trade code Pi'''
        uwp = Uwp('C700055-5')
        for atm in '012479':
            for pop in '78':
                uwp.atmosphere = atm
                uwp.population = pop
                tcs = TradeCodes(uwp)
                self.assertTrue('Pi' in tcs.trade_codes)

    def test_in(self):
        '''Test trade code In'''
        uwp = Uwp('C700055-5')
        for atm in '012479':
            for pop in '9ABCDEF':
                uwp.atmosphere = atm
                uwp.population = pop
                tcs = TradeCodes(uwp)
                self.assertTrue('In' in tcs.trade_codes)

    def test_po(self):
        '''Test trade code Po'''
        uwp = Uwp('C700055-5')
        for atm in '2345':
            for hyd in '0123':
                uwp.atmosphere = atm
                uwp.hydrographics = hyd
                tcs = TradeCodes(uwp)
                self.assertTrue('Po' in tcs.trade_codes)

    def test_ri(self):
        '''Test trade code Ri'''
        uwp = Uwp('C700055-5')
        for atm in '68':
            for pop in '678':
                for gov in '456789':
                    uwp.atmosphere = atm
                    uwp.population = pop
                    uwp.government = gov
                    tcs = TradeCodes(uwp)
                    self.assertTrue('Ri' in tcs.trade_codes)


class TestTradeCodesEconomicExclude(unittest.TestCase):
    '''Test economic trade codes -- exclusion'''
    def test_not_pa(self):
        '''Test trade code not Pa'''
        uwp = Uwp('C755000-0')
        for atm in '0123ABC':
            for hyd in '01239A':
                for pop in '01235679ABCDEF':
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    uwp.population = pop
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Pa' in tcs.trade_codes)

    def test_not_ag(self):
        '''Test trade code not Ag'''
        uwp = Uwp('C700055-5')
        for atm in '0123ABC':
            for hyd in '01239A':
                for pop in '012389ABCDEF':
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    uwp.population = pop
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Ag' in tcs.trade_codes)

    def test_not_na(self):
        '''Test trade code not Na'''
        uwp = Uwp('C700055-5')
        for atm in '456789ABC':
            for hyd in '456789A':
                for pop in '012345':
                    uwp.atmosphere = atm
                    uwp.hydrographics = hyd
                    uwp.population = pop
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Na' in tcs.trade_codes)

    def test_not_px(self):
        '''Test trade code not Px'''
        uwp = Uwp('C700055-5')
        for atm in '01456789C':
            for hyd in '6789A':
                for pop in '012789ABCDEF':
                    for law in '012345ABCDEF':
                        uwp.atmosphere = atm
                        uwp.hydrographics = hyd
                        uwp.population = pop
                        uwp.law_level = law
                        tcs = TradeCodes(uwp)
                        self.assertFalse('Px' in tcs.trade_codes)

    def test_not_pi(self):
        '''Test trade code not Pi'''
        uwp = Uwp('C700055-5')
        for atm in '3568ABC':
            for pop in '01234569ABC':
                uwp.atmosphere = atm
                uwp.population = pop
                tcs = TradeCodes(uwp)
                self.assertFalse('Pi' in tcs.trade_codes)

    def test_not_in(self):
        '''Test trade code not In'''
        uwp = Uwp('C700055-5')
        for atm in '3568ABC':
            for pop in '012345678':
                uwp.atmosphere = atm
                uwp.population = pop
                tcs = TradeCodes(uwp)
                self.assertFalse('In' in tcs.trade_codes)

    def test_not_po(self):
        '''Test trade code not Po'''
        uwp = Uwp('C700055-5')
        for atm in '016789ABC':
            for hyd in '456789A':
                uwp.atmosphere = atm
                uwp.hydrographics = hyd
                tcs = TradeCodes(uwp)
                self.assertFalse('Po' in tcs.trade_codes)

    def test_not_ri(self):
        '''Test trade code not Ri'''
        uwp = Uwp('C700055-5')
        for atm in '01234579ABC':
            for pop in '0123459ABCDEF':
                for gov in '012ABCDEF':
                    uwp.atmosphere = atm
                    uwp.population = pop
                    uwp.government = gov
                    tcs = TradeCodes(uwp)
                    self.assertFalse('Ri' in tcs.trade_codes)
