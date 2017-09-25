'''trade_codes'''

import re
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)


class Uwp(object):
    '''UWP class'''
    def __init__(self, uwp=None):
        if not isinstance(uwp, str):
            raise TypeError
        else:
            re_uwp = re.compile(
                r'([A-HX])([0-9A-Z])([0-9A-Z])([0-9A-Z])' +
                r'([0-9A-Z])([0-9A-Z])([0-9A-Z])\-([0-9A-Z])')
            chars = re_uwp.match(uwp)
            if chars:
                self.starport = chars.group(1)
                self.size = chars.group(2)
                self.atmosphere = chars.group(3)
                self.hydrographics = chars.group(4)
                self.population = chars.group(5)
                self.government = chars.group(6)
                self.law_level = chars.group(7)
                self.tech_level = chars.group(8)
            else:
                raise ValueError
                LOGGER.debug('Invalid UWP %s', uwp)

    def __str__(self):
        '''repr'''
        return '{}{}{}{}{}{}{}-{}'.format(
            self.starport,
            self.size,
            self.atmosphere,
            self.hydrographics,
            self.population,
            self.government,
            self.law_level,
            self.tech_level)


class TradeCodes(object):
    '''Trade codes'''
    def __init__(self, uwp):
        self.uwp = uwp
        self.trade_codes = self.generate()

    def generate(self):
        '''Generate'''
        trade_codes = []
        trade_codes.extend(self._planetary())
        trade_codes.extend(self._population())
        trade_codes.extend(self._economic())
        trade_codes.extend(self._secondary())
        trade_codes.extend(self._political())
        return trade_codes

    def _planetary(self):
        '''Set planetary trade codes'''
        trade_codes = []
        # As - asteroid belt
        if (
                str(self.uwp.size) == '0' and
                str(self.uwp.atmosphere) == '0' and
                str(self.uwp.hydrographics) == '0'):
            trade_codes.append('As')
        # De - desert
        if (str(self.uwp.atmosphere) in '234566789' and
                str(self.uwp.hydrographics) == '0'):
            trade_codes.append('De')
        # Fl - fluid oceans
        if (
                str(self.uwp.atmosphere) in 'ABC' and
                str(self.uwp.hydrographics) in '123456789A'):
            trade_codes.append('Fl')
        # Ga - garden world
        if (
                str(self.uwp.size) in '678' and
                str(self.uwp.atmosphere) in '568' and
                str(self.uwp.hydrographics) in '567'):
            trade_codes.append('Ga')
        # He - hellworld
        if (
                str(self.uwp.size) in '3456789ABC' and
                str(self.uwp.atmosphere) in '2479ABC' and
                str(self.uwp.hydrographics) in '012'):
            trade_codes.append('He')
        # Ic - ice-capped
        if (
                str(self.uwp.atmosphere) in '01' and
                str(self.uwp.hydrographics) in '123456789A'):
            trade_codes.append('Ic')
        # Oc - ocean world
        if (
                str(self.uwp.size) in 'ABCDEF' and
                str(self.uwp.atmosphere) in '3456789ABC' and
                str(self.uwp.hydrographics) == 'A'):
            trade_codes.append('Oc')
        # Va - vacuum
        if str(self.uwp.atmosphere) == '0':
            trade_codes.append('Va')
        # Wa - water world
        if (
                str(self.uwp.size) in '3456789A' and
                str(self.uwp.atmosphere) in '3456789' and
                str(self.uwp.hydrographics) == 'A'):
            trade_codes.append('Wa')
        return trade_codes

    def _population(self):
        '''Set population-related trade codes'''
        trade_codes = []
        # Di - Dieback
        if (
                str(self.uwp.population) == '0' and
                str(self.uwp.government) == '0' and
                str(self.uwp.law_level) == '0' and
                str(self.uwp.tech_level) != '0'):
            trade_codes.append('Di')
        # Ba - barren
        if (
                str(self.uwp.population) == '0' and
                str(self.uwp.government) == '0' and
                str(self.uwp.law_level) == '0' and
                str(self.uwp.tech_level) == '0'):
            trade_codes.append('Ba')
        # Lo - low population
        if str(self.uwp.population) in '123':
            trade_codes.append('Lo')
        # Ni - non-industrial
        if str(self.uwp.population) in '456':
            trade_codes.append('Ni')
        # Ph - pre-high population
        if str(self.uwp.population) == '8':
            trade_codes.append('Ph')
        # Hi - high population
        if str(self.uwp.population) >= '9':
            trade_codes.append('Hi')
        return trade_codes

    def _economic(self):
        '''Set economic trade codes'''
        trade_codes = []
        # Pa - pre-agricultural
        if (
                str(self.uwp.atmosphere) in '456789' and
                str(self.uwp.hydrographics) in '45678' and
                str(self.uwp.population) in '48'):
            trade_codes.append('Pa')
        # Ag - agricultural
        if (
                str(self.uwp.atmosphere) in '456789' and
                str(self.uwp.hydrographics) in '45678' and
                str(self.uwp.population) in '567'):
            trade_codes.append('Ag')
        # Na - non-agricultural
        if (
                str(self.uwp.atmosphere) in '0123' and
                str(self.uwp.hydrographics) in '0123' and
                str(self.uwp.population) >= '6'):
            trade_codes.append('Na')
        # Px - prison or exile camp
        if (
                str(self.uwp.atmosphere) in '23AB' and
                str(self.uwp.hydrographics) in '12345' and
                str(self.uwp.population) in '3456' and
                str(self.uwp.law_level) in '6789'):
            trade_codes.append('Px')
        # Pi - pre-industrial
        if (
                str(self.uwp.atmosphere) in '012479' and
                str(self.uwp.population) in '78'):
            trade_codes.append('Pi')
        # In - industrial
        if (
                str(self.uwp.atmosphere) in '012479ABC' and
                str(self.uwp.population) >= '9'):
            trade_codes.append('In')
        # Po - poor
        if (
                str(self.uwp.atmosphere) in '2345' and
                str(self.uwp.hydrographics) in '0123'):
            trade_codes.append('Po')
        # Pr - pre-rich
        if (
                str(self.uwp.atmosphere) in '68' and
                str(self.uwp.population) in '59'):
            trade_codes.append('Pr')
        # Ri - rich
        if (
                str(self.uwp.atmosphere) in '68' and
                str(self.uwp.population) in '678'):
            trade_codes.append('Ri')
        # Owning system
        if str(self.uwp.government) == '6':
            trade_codes.append('O:0101')
        return trade_codes

    def _secondary(self):
        '''Set secondary codes'''
        trade_codes = []
        # Fa - farming
        # Mi - mining
        # Mr - military rule
        # Pe - penal colony
        # Re - reserve
        if (
                str(self.uwp.population) in '1234' and
                str(self.uwp.government) == '6' and
                str(self.uwp.law_level) in '45'):
            trade_codes.append('Re')
        return trade_codes

    def _political(self):
        '''Set political codes'''
        trade_codes = []
        # Cy - colony
        if (
                str(self.uwp.population) in '56789A' and
                str(self.uwp.government) == 6 and
                str(self.uwp.law_level) in '0123'):
            trade_codes.append('Cy')
        return trade_codes

    def list(self):
        '''repr'''
        return self.trade_codes

    def __str__(self):
        '''str'''
        return ' '.join(self.trade_codes)
