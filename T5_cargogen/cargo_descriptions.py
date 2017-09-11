'''
Cargo description tables
'''

from random import randint, seed
from T5_cargogen.util import Table


class TradeGood(object):
    '''Trade goods base class'''
    def __init__(self):
        self.tables = []

    @staticmethod
    def make_table(table):
        '''Make table from array'''
        goods = Table()
        for indx, value in enumerate(table):
            goods.add_row(indx, value)
        goods.dice = 1
        return goods

    @staticmethod
    def add_detail(trade_codes):
        '''Add detail prefix based on trade code'''
        prefixes = {
            'As': 'Strange', 'Ba': 'Gathered', 'De': 'Mineral',
            'Di': 'Artifact', 'Fl': 'Unusual', 'Ga': 'Premium',
            'He': 'Strange', 'Hi': 'Processed', 'Ic': 'Cryo',
            'Ni': 'Unprocessed', 'Po': 'Obscure', 'Ri': 'Quality',
            'Va': 'Exotic', 'Wa': 'Infused'}

        descriptions = []
        for code in trade_codes:
            if code in prefixes:
                descriptions.append(prefixes[code])

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

    def get_trade_good(self, trade_codes=None):
        ''' Select trade good - trade_codes adds prefix'''
        seed()
        if not isinstance(trade_codes, list):
            trade_codes = []
        description = self.tables[randint(0, len(self.tables) - 1)].roll()
        prefix = self.add_detail(trade_codes)
        if prefix:
            return '{0} {1}'.format(prefix, description)
        else:
            return description


class Ag(TradeGood):
    '''Ag cargo description tables'''
    def __init__(self):
        super(Ag, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Protein', 'Bulk Carbs', 'Bulk Fats',
            'Bulk Pharma', 'Livestock', 'Seedstock']))
        self.tables.append(self.make_table([
            'Flavored Waters', 'Wines', 'Juices',
            'Nectars', 'Decoctions', 'Drinkable Lymphs']))
        self.tables.append(self.make_table([
            'Health Foods', 'Nutraceuticals', 'Fast Drug',
            'Painkillers', 'Antiseptic', 'Antibiotics']))
        self.tables.append(self.make_table([
            'Incenses', 'Iridescents', 'Photonics',
            'Pigments', 'Noisemakers', 'Soundmakers']))
        self.tables.append(self.make_table([
            'Fine Furs', 'Meat Delicacies', 'Fruit Delicacies',
            'Candies', 'Textiles', 'Exotic Sauces']))
        self.tables.append(self.make_table([
            As.get_trade_good, De.get_trade_good, Fl.get_trade_good,
            Ic.get_trade_good, Na.get_trade_good, In.get_trade_good]))
        self.tables.append(self.make_table([
            'Bulk Woods', 'Bulk Pets', 'Bulk Herbs',
            'Bulk Spices', 'Bulk Nitrates', 'Foodstufs']))
        self.tables.append(self.make_table([
            'Flowers', 'Aromatics', 'Pheromones',
            'Secretions', 'Adhesives', 'Novel Flavorings']))
        self.tables.append(self.make_table([
            'Antifungals', 'Antivirals', 'Panacea',
            'Pseudomones', 'Anagathics', 'Slow Drug']))
        self.tables.append(self.make_table([
            'Strange Seeds', 'Motile Plants', 'Reactive Plants',
            'IR Emitters', 'Lek Emitters']))
        self.tables.append(self.make_table([
            'Spices', 'Organic Gems', 'Flavorings',
            'Aged Meats', 'Fermented Fluids', 'Fine Aromatics']))
        self.tables.append(self.make_table([
            Po.get_trade_good, Ri.get_trade_good, Va.get_trade_good,
            Ic.get_trade_good, Na.get_trade_good, In.get_trade_good]))


class As(TradeGood):
    '''As cargo description tables'''
    def __init__(self):
        super(As, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Nitrates', 'Bulk Carbon', 'Bulk Iron',
            'Bulk Copper', 'Radioactive Ores', 'Bulk Ices']))
        self.tables.append(self.make_table([
            'Ores', 'Ices', 'Carbons',
            'Metals', 'Uranium', 'Chelates']))
        self.tables.append(self.make_table([
            'Platinum', 'Gold', 'Gallium',
            'Silver', 'Thorium', 'Radium']))
        self.tables.append(self.make_table([
            'Unusual Rocks', 'Fused Metals', 'Strange Crystals',
            'Fine Dusts', 'Magnetics', 'Light-Sensitives']))
        self.tables.append(self.make_table([
            'Gemstones', 'Alloys', 'Iridium Sponge',
            'Lanthanum', 'Isotopes', 'Anti-Matter']))
        self.tables.append(self.make_table([
            Ag.get_trade_good, De.get_trade_good, Na.get_trade_good,
            Po.get_trade_good, Ri.get_trade_good, Ic.get_trade_good]))


class De(TradeGood):
    '''De cargo description tables'''
    def __init__(self):
        super(De, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Nitrates', 'Bulk Minerals', 'Bulk Abrasives',
            'Bulk Particulates', 'Exotic Fauna', 'Exotic Flora']))
        self.tables.append(self.make_table([
            'Archeologicals', 'Fauna', 'Flora',
            'Minerals', 'Ephemerals', 'Polymers']))
        self.tables.append(self.make_table([
            'Stimulants', 'Bulk Herbs', 'Palliatives',
            'Pheromones', 'Antibiotics', 'Combat Drug']))
        self.tables.append(self.make_table([
            'Envirosuits', 'Reclamation Suits', 'Navigators',
            'Dupe Masterpieces', 'ShimmerCloth', 'ANIFX Blocker']))
        self.tables.append(self.make_table([
            'Excretions', 'Flavorings', 'Nectars',
            'Pelts', 'ANIFX Dyes', 'Seedstock']))
        self.tables.append(self.make_table([
            'Pheromones', 'Artifacts', 'Sparx',
            'Repulsant', 'Dominants', 'Fossils']))


class Fl(TradeGood):
    '''Fl cargo description tables'''
    def __init__(self):
        super(Fl, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Carbon', 'Bulk Petros', 'Bulk Precipitates',
            'Exotic Fluids', 'Organic Polymers', 'Bulk Synthetics']))
        self.tables.append(self.make_table([
            'Archeologicals', 'Fauna', 'Flora',
            'Germanes', 'Flill', 'Chelates']))
        self.tables.append(self.make_table([
            'Antifungals', 'Antivirals', 'Palliatives',
            'Counter-prions', 'Antibiotics', 'Cold Sleep Pills']))
        self.tables.append(self.make_table([
            'Silanes', 'Lek Emitters', 'Aware Blockers',
            'Soothants', 'Self-Solving Puzzles', 'Fluidic Timepieces']))
        self.tables.append(self.make_table([
            'Flavorings', 'Unusual Fluids', 'Encapsulants',
            'Insidiants', 'Corrosives', 'Exotic Aromatics']))
        self.tables.append(self.make_table([
            In.get_trade_good, Ri.get_trade_good, Ic.get_trade_good,
            Na.get_trade_good, Ag.get_trade_good, Po.get_trade_good]))


class Ic(TradeGood):
    '''Ic cargo description tables'''
    def __init__(self):
        super(Ic, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Ices', 'Bulk Precipitates', 'Bulk Ephermerals',
            'Exotic Flora', 'Bulk Gases', 'Bulk Oxygen']))
        self.tables.append(self.make_table([
            'Archeologicals', 'Fauna', 'Flora',
            'Minerals', 'Luminescents', 'Polymers']))
        self.tables.append(self.make_table([
            'Antifungals', 'Antivirals', 'Palliatives',
            'Restoratives', 'Antibiotics', 'Antiseptics']))
        self.tables.append(self.make_table([
            'Heat Pumps', 'Mag Emitters', 'Percept Blockers',
            'Silanes', 'Cold Light Blocks', 'VHDUS Blocker']))
        self.tables.append(self.make_table([
            'Unusual Ices', 'Cryo Alloys', 'Rare Minerals',
            'Unusual Fluids', 'Cryogems', 'VHDUS Blocker']))
        self.tables.append(self.make_table([
            'Fossils', 'Cryogems', 'Vision Suppressants',
            'Fission Suppressant', 'Wafers', 'Cold Sleep Pills']))


class Na(TradeGood):
    '''Na cargo description tables'''
    def __init__(self):
        super(Na, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Abrasives', 'Bulk Gases', 'Bulk Minerals',
            'Bulk Precipitates', 'Exotic Fauna', 'Exotic Flora']))
        self.tables.append(self.make_table([
            'Archeologicals', 'Fauna', 'Flora',
            'Minerals', 'Ephemerals', 'Polymers']))
        self.tables.append(self.make_table([
            'Branded Tools', 'Drinkable Lymphs', 'Strange Seeds',
            'Pattern Creators', 'Pigments', 'Warm Leather']))
        self.tables.append(self.make_table([
            'Hummingsand', 'Masterpieces', 'Fine Carpets',
            'Isotopes', 'Pelts', 'Seedstock']))
        self.tables.append(self.make_table([
            'Masterpieces', 'Unusual Rocks', 'Artifacts',
            'Non-fossil Carcasses', 'Replicating Clays', 'ANIFX EMitter']))
        self.tables.append(self.make_table([
            Ag.get_trade_good, Ri.get_trade_good, In.get_trade_good,
            Ic.get_trade_good, De.get_trade_good, Fl.get_trade_good]))


class In(TradeGood):
    '''In cargo description tables'''
    def __init__(self):
        super(In, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Electronics', 'Photonics', 'Magnetics',
            'Fluidics', 'Polymers', 'Gravitics']))
        self.tables.append(self.make_table([
            'Obsoletes', 'Used Goods', 'Reparables',
            'Radioactives', 'Metals', 'Sludges']))
        self.tables.append(self.make_table([
            'Biologics', 'Mechanicals', 'Textiles',
            'Weapons', 'Armor', 'Robots']))
        self.tables.append(self.make_table([
            'Nostrums', 'Restoratives', 'Palliatives',
            'Chelates', 'Antidotes', 'Antitoxins']))
        self.tables.append(self.make_table([
            'Software', 'Databases', 'Expert Systems',
            'Upgrades', 'Backups', 'Raw Sensings']))
        self.tables.append(self.make_table([
            'Disposables', 'Respirators', 'Filter Masks',
            'Combination', 'Parts', 'Improvements']))


class Po(TradeGood):
    '''Po cargo description tables'''
    def __init__(self):
        super(Po, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Nutrients', 'Bulk Fibers', 'Bulk Organics',
            'Bulk Minerals', 'Bulk Textiles', 'Exotic Flora']))
        self.tables.append(self.make_table([
            'Art', 'Recordings', 'Writings',
            'Tactiles', 'Osmancies', 'Wafers']))
        self.tables.append(self.make_table([
            'Strange Crystals', 'Strange Seeds', 'Pigments',
            'Emotion Lighting', 'Silanes', 'Flora']))
        self.tables.append(self.make_table([
            'Gemstones', 'Antiques', 'Collectibles',
            'Allotropes', 'Spices', 'Seedstock']))
        self.tables.append(self.make_table([
            'Masterpieces', 'Exotic Flora', 'Antiques',
            'Incomprehensibles', 'Fossils', 'VHDUS Emitter']))
        self.tables.append(self.make_table([
            In.get_trade_good, Ri.get_trade_good, Fl.get_trade_good,
            Ic.get_trade_good, Ag.get_trade_good, Va.get_trade_good]))


class Ri(TradeGood):
    '''Ri cargo description tables'''
    def __init__(self):
        super(Ri, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Foodstuffs', 'Bulk Protein', 'Bulk Carbs',
            'Bulk Fats', 'Exotic Flora', 'Exotic Fauna']))
        self.tables.append(self.make_table([
            'Echostones', 'Self-Defenders', 'Attractants',
            'Sophont Cuisine', 'Sophont Hats', 'Variable Tattoos']))
        self.tables.append(self.make_table([
            'Branded Foods', 'Branded Drinks', 'Branded Clothes',
            'Flavored Drinks', 'Flowers', 'Music']))
        self.tables.append(self.make_table([
            'Delicacies', 'Spices', 'Tisanes',
            'Nectars', 'Pelts', 'Variable Tattoos']))
        self.tables.append(self.make_table([
            'Antique Art', 'Masterpieces', 'Artifacts',
            'Fine Art', 'Meson Barriers', 'Famous Wafers']))
        self.tables.append(self.make_table([
            'Edutainments', 'Recordings', 'Writings',
            'Tactiles', 'Osmancies', 'Wafers']))


class Va(TradeGood):
    '''Va cargo description tables'''
    def __init__(self):
        super(Va, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Bulk Dusts', 'Bulk Minerals', 'Bulk Metals',
            'Radioactive Ores', 'Bulk Particulates', 'Ephemerals']))
        self.tables.append(self.make_table([
            'Branded Vacc Suits', 'Awareness Pinger', 'Strange Seeds',
            'Pigments', 'Unusual Minerals', 'Exotic Crystals']))
        self.tables.append(self.make_table([
            'Branded Oxygen', 'Vacc Suit Scents', 'Vacc Suit Patches',
            'Branded Tools', 'Holo-Companions', 'Flavored Air']))
        self.tables.append(self.make_table([
            'Vacc Gems', 'Unusual Dusts', 'Insulants',
            'Crafted Devices', 'Rare Minerals', 'Catalysts']))
        self.tables.append(self.make_table([
            'Archeologicals', 'Fauna', 'Flora',
            'Minerals', 'Ephemerals', 'Polymers']))
        self.tables.append(self.make_table([
            'Obsoletes', 'Used Goods', 'Reparables',
            'Plutonium', 'Metals', 'Sludges']))


class Cp(TradeGood):
    '''Cp cargo description tables'''
    def __init__(self):
        super(Cp, self).__init__()
        self.tables = []
        self.tables.append(self.make_table([
            'Software', 'Expert Systems', 'Databases',
            'Upgrades', 'Backups', 'Raw Sensings']))
        self.tables.append(self.make_table([
            'Incenses', 'Contemplatives', 'Cold Welders',
            'Polymer Sheets', 'Hats', 'Skin Tones']))
        self.tables.append(self.make_table([
            'Branded Clothes', 'Branded Devices', 'Flavored Drinks',
            'Flavorings', 'Decorations', 'Group Symbols']))
        self.tables.append(self.make_table([
            'Monumental Art', 'Holo Sculpture', 'Collectible Books',
            'Jewelry', 'Museum Items', 'Monumental Art']))
        self.tables.append(self.make_table([
            'Coinage', 'Currency', 'Money Cards',
            'Gold', 'Silver', 'Platinum']))
        self.tables.append(self.make_table([
            'Regulations', 'Synchronizations', 'Expert Systems',
            'Educationals', 'Mandates', 'Accountings']))
