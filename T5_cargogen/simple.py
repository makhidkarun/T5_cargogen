'''Simple list/dict solution'''

from __future__ import print_function
from random import seed, randint
import logging

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)


class TradeCargo(object):
    '''Simple approach'''
    def __init__(self):
        self.codes = {
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
        seed()

    def select_cargo(self, trade_codes, add_detail_flag=True):
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
        if trade_code not in self.codes:
            LOGGER.debug(
                '%s not in supported trade codes, using Na instead',
                trade_code)
            trade_code = 'Na'

        # Pick cargo at random
        LOGGER.debug('Picking cargo description for %s', trade_code)
        cargo = self.codes[trade_code][randint(0, 5)][randint(0, 5)]
        LOGGER.debug('Selected %s', cargo)

        # Deal with imbalance results (_Xx)
        if cargo.startswith('_'):
            LOGGER.debug('Imbalance cargo %s', cargo)
            add_detail_flag = False
            code = cargo.replace('_', '')
            LOGGER.debug('Rerunning with imbalance')
            cargo = self.select_cargo([code])

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
