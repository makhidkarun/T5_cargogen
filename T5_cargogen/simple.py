'''Simple list/dict solution'''

from __future__ import print_function
from random import seed, randint
import logging
import re
import json

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class TradeCargo(object):
    '''Simple approach'''
    def __init__(self):
        self.tech_level = 0
        self.trade_codes = []
        self.cost = 0
        self.description = ''
        self.price = 0
        self._codes = {
            'Ga': [
                ['Bulk Protein', 'Bulk Carbs', 'Bulk Fats',
                 'Bulk Pharma', 'Livestock', 'Seedstock'],
                ['Flavored Waters', 'Wines', 'Juices',
                 'Nectars', 'Decoctions', 'Drinkable Lymphs'],
                ['Health Foods', 'Nutraceuticals', 'Fast Drug',
                 'Painkillers', 'Antiseptic', 'Antibiotics'],
                ['Incenses', 'Iridescents', 'Photonics',
                 'Pigments', 'Noisemakers', 'Soundmakers'],
                ['Fine Furs', 'Meat Delicacies', 'Fruit Delicacies',
                 'Candies', 'Textiles', 'Exotic Sauces'],
                ['_As', '_De', '_Fl', '_Ic', '_Na', '_In']],
            'Fa': [
                ['Bulk Woods', 'Bulk Pets', 'Bulk Herbs',
                 'Bulk Spices', 'Bulk Nitrates', 'Foodstuffs'],
                ['Flowers', 'Aromatics', 'Pheromones',
                 'Secretions', 'Adhesives', 'Novel Flavorings'],
                ['Antifungals', 'Antivirals', 'Panacea',
                 'Pseudomones', 'Anagathics', 'Slow Drug'],
                ['Strange Seeds', 'Motile Plants', 'Reactive Plants',
                 'IR Emitters', 'Lek Emitters'],
                ['Spices', 'Organic Gems', 'Flavorings',
                 'Aged Meats', 'Fermented Fluids', 'Fine Aromatics'],
                ['_Po', '_Ri', '_Va', '_Ic', '_Na', '_In']],
            'As': [
                ['Bulk Nitrates', 'Bulk Carbon', 'Bulk Iron',
                 'Bulk Copper', 'Radioactive Ores', 'Bulk Ices'],
                ['Ores', 'Ices', 'Carbons',
                 'Metals', 'Uranium', 'Chelates'],
                ['Platinum', 'Gold', 'Gallium',
                 'Silver', 'Thorium', 'Radium'],
                ['Unusual Rocks', 'Fused Metals', 'Strange Crystals',
                 'Fine Dusts', 'Magnetics', 'Light-Sensitives'],
                ['Gemstones', 'Alloys', 'Iridium Sponge',
                 'Lanthanum', 'Isotopes', 'Anti-Matter'],
                ['_Ag', '_De', '_Na', '_Po', '_Ri', '_Ic']],
            'De': [
                ['Bulk Nitrates', 'Bulk Minerals', 'Bulk Abrasives',
                 'Bulk Particulates', 'Exotic Fauna', 'Exotic Flora'],
                ['Archeologicals', 'Fauna', 'Flora',
                 'Minerals', 'Ephemerals', 'Polymers'],
                ['Stimulants', 'Bulk Herbs', 'Palliatives',
                 'Pheromones', 'Antibiotics', 'Combat Drug'],
                ['Envirosuits', 'Reclamation Suits', 'Navigators',
                 'Dupe Masterpieces', 'ShimmerCloth', 'ANIFX Blocker'],
                ['Excretions', 'Flavorings', 'Nectars',
                 'Pelts', 'ANIFX Dyes', 'Seedstock'],
                ['Pheromones', 'Artifacts', 'Sparx',
                 'Repulsant', 'Dominants', 'Fossils']],
            'Fl': [
                ['Bulk Carbon', 'Bulk Petros', 'Bulk Precipitates',
                 'Exotic Fluids', 'Organic Polymers', 'Bulk Synthetics'],
                ['Archeologicals', 'Fauna', 'Flora',
                 'Germanes', 'Flill', 'Chelates'],
                ['Antifungals', 'Antivirals', 'Palliatives',
                 'Counter-prions', 'Antibiotics', 'Cold Sleep Pills'],
                ['Silanes', 'Lek Emitters', 'Aware Blockers',
                 'Soothants', 'Self-Solving Puzzlies', 'Fluidic Timepieces'],
                ['Flavorings', 'Unusual Fluids', 'Encapsulants',
                 'Insidiants', 'Corrosives', 'Exotic Aromatics'],
                ['_In', '_Ri', '_Ic', '_Na', '_Ag', '_Po']],
            'Ic': [
                ['Bulk Ices', 'Bulk Precipitates', 'Bulk Ephemerals',
                 'Exotic Flora', 'Bulk Gases', 'Bulk Oxygen'],
                ['Archeologicals', 'Fauna', 'Flora',
                 'Minerals', 'Luminescents', 'Polymers'],
                ['Antifungals', 'Antivirals', 'Palliatives',
                 'Counter-prions', 'Antibiotics', 'Cold Sleep Pills'],
                ['Silanes', 'Lek Emitters', 'Aware Blockers',
                 'Soothants', 'Self-Solving Puzzlies', 'Fluidic Timepieces'],
                ['Unusual Ices', 'Cryo Alloys', 'Rare Minerals',
                 'Unusual Fluids', 'Cryogems', 'VHDUS Dyes'],
                ['Fossils', 'Cryogems', 'Vision Suppressant',
                 'Fission Suppressant', 'Wafers', 'Cold Sleep Pills']],
            'In': [
                ['Electronics', 'Photonics', 'Magnetics',
                 'Fluidics', 'Polymers', 'Gravitics'],
                ['Obsoletes', 'Used Goods', 'Reparables',
                 'Radioactives', 'Metals', 'Sludges'],
                ['Biologics', 'Mechanicals', 'Textiles',
                 'Weapons', 'Armor', 'Robots'],
                ['Nostrums', 'Restoratives', 'Palliatives',
                 'Chelates', 'Antidotes', 'Antitoxins'],
                ['Software', 'Databases', 'Expert Systems',
                 'Upgrades', 'Backups', 'Raw Sensings'],
                ['Disposables', 'Respirators', 'Filter Masks',
                 'Combination', 'Parts', 'Improvements']],
            'Na': [
                ['Bulk Abrasives', 'Bulk Gases', 'Bulk Minerals',
                 'Bulk Precipitates', 'Exotic Fauna', 'Exotic Flora'],
                ['Archeologicals', 'Fauna', 'Flora',
                 'Minerals', 'Ephemerals', 'Polymers'],
                ['Branded Tools', 'Drinkable Lymphs', 'Strange Seeds',
                 'Pattern Creators', 'Pigments', 'Warm Leather'],
                ['Hummingsand', 'Masterpieces', 'Fine Carpets',
                 'Isotopes', 'Pelts', 'Seedstock'],
                ['Masterpieces', 'Unusual Rocks', 'Artifacts',
                 'Non-fossil Carcasses', 'Replicating Clays', 'ANIFX EMitter'],
                ['_Ag', '_Ri', '_In', '_Ic', '_De', '_Fl']],
            'Po': [
                ['Bulk Nutrients', 'Bulk Fibers', 'Bulk Organics',
                 'Bulk Minerals', 'Bulk Textiles', 'Exotic Flora'],
                ['Art', 'Recordings', 'Writings',
                 'Tactiles', 'Osmancies', 'Wafers'],
                ['Strange Crystals', 'Strange Seeds', 'Pigments',
                 'Emotion Lighting', 'Silanes', 'Flora'],
                ['Gemstones', 'Antiques', 'Collectibles',
                 'Allotropes', 'Spices', 'Seedstock'],
                ['Masterpieces', 'Exotic Flora', 'Antiques',
                 'Incomprehensibles', 'Fossils', 'VHDUS Emitter'],
                ['_In', '_Ri', '_Fl', '_Ic', '_Ag', '_Va']],
            'Ri': [
                ['Bulk Foodstuffs', 'Bulk Protein', 'Bulk Carbs',
                 'Bulk Fats', 'Exotic Flora', 'Exotic Fauna'],
                ['Echostones', 'Self-Defenders', 'Attractants',
                 'Sophont Cuisine', 'Sophone Hats', 'Variable Tattoos'],
                ['Branded Foods', 'Branded Drinks', 'Branded Clothes',
                 'Flavored Drinks', 'Flowers', 'Music'],
                ['Delicacies', 'Spices', 'Tisanes',
                 'Nectars', 'Pelts', 'Variable Tattoos'],
                ['Antique Art', 'Masterpieces', 'Artifacts',
                 'Fine Art', 'Meson Barriers', 'Famous Wafers'],
                ['Edutainments', 'Recordings', 'Writings',
                 'Tactiles', 'Osmancies', 'Wafers']],
            'Va': [
                ['Bulk Dusts', 'Bulk Minerals', 'Bulk Metals',
                 'Radioactive Ores', 'Bulk Particulates', 'Ephererals'],
                ['Branded Vacc Suits', 'Awareness Pinger', 'Strange Seeds',
                 'Pigments', 'Unusual Minerals', 'Exotic Crystals'],
                ['Branded Oxygen', 'Vacc Suit Scents', 'Vacc Suit Patches',
                 'Branded Tools', 'Holo-Companions', 'Flavored Air'],
                ['Vacc Gems', 'Unusual Dusts', 'Insulants',
                 'Crafted Devices', 'Rare Minerals', 'Catalysts'],
                ['Archeologicals', 'Fauna', 'Flora',
                 'Minerals', 'Ephemerals', 'Polymers'],
                ['Obsoletes', 'Used Goods', 'Reparables',
                 'Plutonium', 'Metals', 'Sludges']],
            'Cp': [
                ['Software', 'Expert Systems', 'Databases',
                 'Upgrades', 'Backups', 'Raw Sensings'],
                ['Incenses', 'Contemplatives', 'Cold Welders',
                 'Polymer Sheets', 'Hats', 'Skin Tones'],
                ['Branded Clothes', 'Branded Devices', 'Flavored Drinks',
                 'Flavorings', 'Decorations', 'Group Symbols'],
                ['Monumental Art', 'Holo Sculpture', 'Collectible Books',
                 'Jewelry', 'Museum Items', 'Monumental Art'],
                ['Coinage', 'Currency', 'Money Cards',
                 'Gold', 'Silver', 'Platinum'],
                ['Regulations', 'Synchronzations', 'Expert Systems',
                 'Educationals', 'Mandates', 'Accountings']]
        }
        self._match_uwp = re.compile(r'[A-HX][0-9A-Z]{6}\-([0-9A-Z])')
        seed()

    def generate_cargo(self, uwp, trade_codes=None):
        '''Generate cargo based on UWP, TCs'''

        # Extract TL from UWP
        self.cost = 3000
        self.tech_level = self.get_tl(uwp)
        self.cost += 100 * self._tech_level_as_int(self.tech_level)
        LOGGER.debug('Cost = %s', self.cost)
        # Get useful trade codes
        if isinstance(trade_codes, list):
            self.determine_cost(trade_codes)
        else:
            self.trade_codes = list()
        self.description = self.select_cargo_name(self.trade_codes)

    def generate_sale(self, market_uwp, market_trade_codes=None):
        '''Determine sale price based on market UWP, trade codes'''
        self.price = 5000
        market_tech_level = self.get_tl(market_uwp)
        # Get market trade codes
        if market_trade_codes is None:
            market_trade_codes = list()
        self.determine_price(market_trade_codes)

        # TL effect
        tl_mod = 0.1 * (
            self._tech_level_as_int(self.tech_level) -
            self._tech_level_as_int(market_tech_level))
        self.price = int(self.price * (1 + tl_mod))
        LOGGER.debug('Price = %s', self.price)

    def determine_cost(self, trade_codes):
        ''' Process trade codes - add valid TCs to self.trade_codes'''
        cost_mods = {
            'Ag': -1000, 'As': -1000, 'Ba': +1000, 'De': +1000,
            'Fl': +1000, 'Hi': -1000, 'Ic': 0, 'In': -1000,
            'Lo': +1000, 'Na': 0, 'Ni': +1000, 'Po': -1000,
            'Ri': +1000, 'Va': +1000
        }
        valid_trade_codes = []
        for trade_code in trade_codes:
            if trade_code in cost_mods.keys():
                LOGGER.debug('Adding trade code %s', trade_code)
                valid_trade_codes.append(trade_code)
            else:
                LOGGER.debug('Ignoring trade code %s', trade_code)
        self.trade_codes = sorted(list(set(valid_trade_codes)))

        # Add cost modifiers
        for trade_code in self.trade_codes:
            LOGGER.debug(
                'Processing trade code %s (cost mod = Cr %s)',
                trade_code,
                cost_mods[trade_code])
            self.cost += cost_mods[trade_code]

    def determine_price(self, market_trade_codes):
        '''Determine price based on source TCs, market TCs'''
        market_mods = {
            'Ag': (['Ag', 'As', 'De', 'Hi', 'In', 'Ri', 'Va'], 1000),
            'As': (['As', 'In', 'Ri', 'Va'], 1000),
            'Ba': (['In'], 1000),
            'De': (['De'], 1000),
            'Fl': (['Fl' 'In'], 1000),
            'Hi': (['Hi'], 1000),
            'In': (['Ag', 'As', 'De', 'Fl', 'Hi', 'In', 'Ri', 'Va'], 1000),
            'Na': (['As', 'De', 'Va'], 1000),
            'Po': (['Ag', 'Hi', 'In', 'Ri'], -1000),
            'Ri': (['Ag', 'De', 'Hi', 'In', 'Ri'], 1000),
            'Va': (['As', 'In', 'Va'], 1000)
        }
        for trade_code in self.trade_codes:
            if trade_code in market_mods:
                for code in market_mods[trade_code][0]:
                    LOGGER.debug(
                        'Checking source TC %s market TC %s',
                        trade_code,
                        code)
                    if code in market_trade_codes:
                        LOGGER.debug(
                            'Found match: adjustment = %s',
                            market_mods[trade_code][1])
                        self.price += market_mods[trade_code][1]
                        LOGGER.debug('Price = Cr%s', self.price)

    def select_cargo_name(self, trade_codes, add_detail_flag=True):
        '''Select cargo based on [trade_codes]'''
        # Pick trade code at random
        LOGGER.debug('Supplied trade codes = %s', trade_codes)
        trade_code = trade_codes[randint(0, len(trade_codes) - 1)]
        LOGGER.debug('Selected trade code %s', trade_code)

        # Ag => pick either Ga or Fa at random
        if trade_code == 'Ag':
            LOGGER.debug('Trade code is Ag, select either Ga or Fa')
            trade_code = ['Ga', 'Fa'][randint(0, 1)]
            LOGGER.debug('Trade code is %s', trade_code)

        # Validate trade code -- use Na if it's not in the list
        if trade_code not in self._codes:
            LOGGER.debug(
                '%s not in supported trade codes, using Na instead',
                trade_code)
            trade_code = 'Na'

        # Pick cargo at random
        LOGGER.debug('Picking cargo description for %s', trade_code)
        cargo = self._codes[trade_code][randint(0, 5)][randint(0, 5)]
        LOGGER.debug('Selected %s', cargo)

        # Deal with imbalance results (_Xx)
        if cargo.startswith('_'):
            LOGGER.debug('Imbalance cargo %s', cargo)
            add_detail_flag = False
            code = cargo.replace('_', '')
            LOGGER.debug('Rerunning with imbalance')
            cargo = self.select_cargo_name([code])

        # Classification-specific prefix
        prefix = None
        if add_detail_flag:
            prefix = self.add_detail([trade_code])
        if prefix:
            return '{} {}'.format(prefix, cargo)
        else:
            return cargo

    @staticmethod
    def add_detail(trade_codes):
        '''Add detail prefix based on trade code'''
        LOGGER.debug('Supplied trade_codes = %s', trade_codes)
        prefixes = {
            'As': 'Strange', 'Ba': 'Gathered', 'De': 'Mineral',
            'Di': 'Artifact', 'Fl': 'Unusual', 'Ga': 'Premium',
            'He': 'Strange', 'Hi': 'Processed', 'Ic': 'Cryo',
            'Ni': 'Unprocessed', 'Po': 'Obscure', 'Ri': 'Quality',
            'Va': 'Exotic', 'Wa': 'Infused'}

        descriptions = []
        for code in trade_codes:
            LOGGER.debug('Processing code %s', code)
            if code in prefixes:
                LOGGER.debug(
                    'Found description %s for code %s', prefixes[code], code)
                descriptions.append(prefixes[code])
        LOGGER.debug('Available descriptions = %s', descriptions)

        # Weed out In/Processed
        if 'Processed' in descriptions and 'In' in trade_codes:
            descriptions.remove('Processed')
        # Weed out As/Exotic
        if 'Exotic' in descriptions and 'As' in trade_codes:
            descriptions.remove('Exotic')

        # Pick one
        if len(descriptions) != 0:
            return descriptions[randint(0, len(descriptions) - 1)]
        else:
            return None

    def get_tl(self, uwp):
        ''''Extract TL from UWP, return hexit'''
        try:
            tech_level = self._match_uwp.match(uwp).group(1)
            LOGGER.debug(
                'TL = %s (%s)',
                tech_level,
                self._tech_level_as_int(tech_level))
            return tech_level
        except AttributeError:
            print('Invalid UWP {} (should be StSzAHPGL-T'.format(uwp))
            raise

    @staticmethod
    def _tech_level_as_int(tech_level):
        '''Return int representation of tech_level'''
        if tech_level in '0123456789':
            return int(tech_level)
        else:
            return ord(tech_level) - 55

    def __repr__(self):
        '''Represent cargo'''
        return '{}-{} Cr{:,} {}\nSale price: Cr{:,}'.format(
            self.tech_level,
            ' '.join(self.trade_codes),
            self.cost,
            self.description,
            self.price)

    def json_export(self):
        '''Export JSON'''
        jdata = {
            'tech_level': self.tech_level,
            'trade_codes': self.trade_codes,
            'description': self.description,
            'cost': self.cost,
            'price': 0
        }
        return json.dumps(jdata)

    def json_import(self, jdata):
        '''Import JSON'''
        try:
            jdict = json.loads(jdata)
        except ValueError:
            raise
        try:
            self.tech_level = jdict['tech_level']
            self.trade_codes = jdict['trade_codes']
            self.description = jdict['description']
            self.cost = jdict['cost']
            self.price = 0
        except KeyError:
            raise


class BrokerSale(object):
    '''Broker-assisted sale'''
    def __init__(self, skill=0, cargo=None):
        self.cargo = cargo
        self.skill = max(skill, 4)
        LOGGER.debug('Cargo = %s', cargo)
        LOGGER.debug('Broker skill = %d', self.skill)
        self._commission_rate = 0.1
        self.actual_value = 0
        self.commission = 0

    def sale(self):
        '''Offer for sale'''
        actual_value_table = [
            0.4, 0.5, 0.7, 0.8, 0.9,
            1.0,
            1.1, 1.2, 1.3, 1.5, 1.7,
            2.0, 3.0, 4.0
        ]
        flux = self.flux()
        roll = flux + int(self.skill / 2)
        LOGGER.debug(
            'Flux() = %s, broker DM = %s',
            flux,
            (int(self.skill / 2)))
        LOGGER.debug('Actual value %s', actual_value_table[roll + 5])
        self.actual_value = int(
            actual_value_table[roll + 5] * self.cargo.price)
        self.commission = int(self._commission_rate * self.actual_value)

    @staticmethod
    def flux():
        '''Flux die roll'''
        return randint(1, 6) - randint(1, 6)

    def __repr__(self):
        '''Represent sale'''
        return '{}\nActual price Cr{:,}\nCommission Cr{:,}'.format(
            self.cargo,
            self.actual_value,
            self.commission)

    def json_export(self):
        '''Export Json'''
        jdict = {
            'cargo': self.cargo.json_export(),
            'skill': self.skill,
            'actual_value': self.actual_value,
            'commission': self.commission
        }
        return json.dumps(jdict)

    def json_import(self, jdata):
        '''JSON import'''
        try:
            jdict = json.loads(jdata)
        except ValueError:
            raise
        try:
            self.skill = jdict['skill']
            self.actual_value = jdict['actual_value']
            self.commission = jdict['commission']
            self.cargo.json_import(jdict['cargo'])
        except KeyError:
            raise
