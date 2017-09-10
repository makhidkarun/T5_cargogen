'''
Cargo description tables
'''

from random import seed, randint
from T5_cargogen.util import Die, Table


class DescriptionTable(Table):
    '''Cargo description table base class'''
    def __init__(self):
        super(DescriptionTable, self).__init__()
        seed()
        self.dice = 1

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

    def return_description(self, trade_codes):
        '''Return full description'''
        description = self.roll()
        prefix = self.add_detail(trade_codes)
        if prefix:
            return '{0} {1}'.format(prefix, description)
        else:
            return description


class TradeGood(object):
    '''Trade goods base class'''
    def __init__(self):
        self.table_1 = DescriptionTable()
        self.table_1.add_row(1, 'base class t1')
        self.table_2 = DescriptionTable()
        self.table_2.add_row(1, 'base class t2')
        self.table_3 = DescriptionTable()
        self.table_3.add_row(1, 'base class t3')
        self.table_4 = DescriptionTable()
        self.table_4.add_row(1, 'base class t4')
        self.table_4 = DescriptionTable()
        self.table_4.add_row(1, 'base class t5')
        self.table_6 = DescriptionTable()
        self.table_6.add_row(1, 'base class t6')

    @staticmethod
    def make_table(table):
        '''Make table from array'''
        goods = DescriptionTable()
        for indx, value in enumerate(table):
            goods.add_row(indx, value)
            return goods

    def get_trade_good(self):
        ''' Select trade good'''
        return self.types_table.roll()


class Ag(object):
    '''Ag description tables'''
    def __init__(self):
        self.table_1 = DescriptionTable()
        self.table_1.add_row(1, 'Bulk Protein')
        self.table_1.add_row(2, 'Bulk Carbs')
        self.table_1.add_row(3, 'Bulk Fats')
        self.table_1.add_row(4, 'Bulk Pharma')
        self.table_1.add_row(5, 'Livestock')
        self.table_1.add_row(6, 'Seedstock')

        self.table_2 = DescriptionTable()
        self.table_2.add_row(1, 'Flavored Waters')
        self.table_2.add_row(2, 'Wines')
        self.table_2.add_row(3, 'Juices')
        self.table_2.add_row(4, 'Nectars')
        self.table_2.add_row(5, 'Decoctions')
        self.table_2.add_row(6, 'Drinkable Lymphs')

        self.table_3 = DescriptionTable()
        self.table_3.add_row(1, 'Health Foods')
        self.table_3.add_row(2, 'Nutraceuticals')
        self.table_3.add_row(3, 'Fast Drug')
        self.table_3.add_row(4, 'Painkillers')
        self.table_3.add_row(5, 'Antiseptic')
        self.table_3.add_row(6, 'Antibiotics')

        self.table_4 = DescriptionTable()
        self.table_4.add_row(1, 'Incenses')
        self.table_4.add_row(2, 'Iridescents')
        self.table_4.add_row(3, 'Photonics')
        self.table_4.add_row(4, 'Pigments')
        self.table_4.add_row(5, 'Noisemakers')
        self.table_4.add_row(6, 'Soundmakers')

        self.table_5 = DescriptionTable()
        self.table_5.add_row(1, 'Fine Furs')
        self.table_5.add_row(2, 'Meat Delicacies')
        self.table_5.add_row(3, 'Fruit Delicacies')
        self.table_5.add_row(4, 'Candies')
        self.table_5.add_row(5, 'Textiles')
        self.table_5.add_row(6, 'Exotic Sauces')

        self.table_6 = DescriptionTable()
        self.table_6.add_row(1, 'As')
        self.table_6.add_row(2, 'De')
        self.table_6.add_row(3, 'Fl')
        self.table_6.add_row(4, 'Ic')
        self.table_6.add_row(5, 'Na')
        self.table_6.add_row(6, 'In')

        self.table_7 = DescriptionTable()
        self.table_7.add_row(1, 'Bulk Woods')
        self.table_7.add_row(2, 'Bulk Pelts')
        self.table_7.add_row(3, 'Bulk Herbs')
        self.table_7.add_row(4, 'Bulk Spices')
        self.table_7.add_row(5, 'Bulk Nitrates')
        self.table_7.add_row(6, 'Foodstuffs')

        self.table_8 = DescriptionTable()
        self.table_8.add_row(1, 'Flowers')
        self.table_8.add_row(2, 'Aromatics')
        self.table_8.add_row(3, 'Pheromones')
        self.table_8.add_row(4, 'Secretions')
        self.table_8.add_row(5, 'Adhesives')
        self.table_8.add_row(6, 'Novel Flacorings')

        self.table_9 = DescriptionTable()
        self.table_9.add_row(1, 'Antifungals')
        self.table_9.add_row(2, 'Anivirals')
        self.table_9.add_row(3, 'Panacea')
        self.table_9.add_row(4, 'Pseudomones')
        self.table_9.add_row(5, 'Anagathics')
        self.table_9.add_row(6, 'Slow Drug')

        self.table_10 = DescriptionTable()
        self.table_10.add_row(1, 'Strange Seeds')
        self.table_10.add_row(2, 'Motile Plants')
        self.table_10.add_row(3, 'Reactive Plants')
        self.table_10.add_row(4, 'Reactive Woods')
        self.table_10.add_row(5, 'IR Emitters')
        self.table_10.add_row(6, 'Lek Emitters')

        self.table_11 = DescriptionTable()
        self.table_11.add_row(1, 'Spices')
        self.table_11.add_row(2, 'Organic Gems')
        self.table_11.add_row(3, 'Flavorings')
        self.table_11.add_row(4, 'Aged Meats')
        self.table_11.add_row(5, 'Fermented Fluids')
        self.table_11.add_row(6, 'Fine Aromatics')

        self.table_12 = DescriptionTable()
        self.table_12.add_row(1, 'Po')
        self.table_12.add_row(2, 'Ri')
        self.table_12.add_row(3, 'Va')
        self.table_12.add_row(4, 'Ic')
        self.table_12.add_row(5, 'Na')
        self.table_12.add_row(6, 'In')

    def __init__(self):
        super(Ag, self).__init__()
        self.types_table.add_row(7, self.table_7.roll)
        self.types_table.add_row(8, self.table_8.roll)
        self.types_table.add_row(9, self.table_9.roll)
        self.types_table.add_row(10, self.table_10.roll)
        self.types_table.add_row(11, self.table_11.roll)
        self.types_table.add_row(12, self.table_12.roll)
        self.types_table.roller = Die(12)


class As(TradeGood):
    '''As cargo description tables'''
    def __init__(self):
        super(As, self).__init__()
        self.table_1 = self.make_table([
            'Bulk Nitrates', 'Bulk Carbon', 'Bulk Iron',
            'Bulk Copper', 'Radioactive Ores', 'Bulk Ices'])
        self.table_2 = self.make_table([
            'Ores', 'Ices', 'Carbons',
            'Metals', 'Uranium', 'Chelates'])
        self.table_3 = self.make_table([
            'Platinum', 'Gold', 'Gallium',
            'Silver', 'Thorium', 'Radium'])
        self.table_4 = self.make_table([
            'Unusual Rocks', 'Fused Metals', 'Strange Crystals',
            'Fine Dusts', 'Magnetics', 'Light-Sensitives'])
        self.table_5 = self.make_table([
            'Gemstones', 'Alloys', 'Iridium Sponge',
            'Lanthanum', 'Isotopes', 'Anti-Matter'])
        self.table_6 = self.make_table([
            'Ag', 'De', 'Na', 'Po', 'Ri', 'Ic'])

        self.types_table = Table()
        self.types_table.add_row(1, self.table_1.roll)
        self.types_table.add_row(2, self.table_2.roll)
        self.types_table.add_row(3, self.table_3.roll)
        self.types_table.add_row(4, self.table_4.roll)
        self.types_table.add_row(5, self.table_4.roll)
        self.types_table.add_row(6, self.table_6.roll)
        self.types_table.dice = 1


'''
class De(TradeGood):
    '''De cargo description tables'''
    def __init__(self):
        super(De, self).__init__()
        self.table_1 = DescriptionTable()
        self.table_1.add_row(1, 'Bulk Nitrates')
        self.table_1.add_row(2, 'Bulk Minerals')
        self.table_1.add_row(3, 'Bulk Abrasives')
        self.table_1.add_row(4, 'Bulk Particulates')
        self.table_1.add_row(5, 'Exotic Fauna')
        self.table_1.add_row(6, 'Exotic Flora')

        self.table_2 = DescriptionTable()
        self.table_2.add_row(1, 'Archeologicals')
        self.table_2.add_row(2, 'Fauna')
        self.table_2.add_row(3, 'Flora')
        self.table_2.add_row(4, 'Minerals')
        self.table_2.add_row(5, 'Ephemerals')
        self.table_2.add_row(6, 'Polymers')

        self.table_3 = DescriptionTable()
        self.table_3.add_row(1, 'Stimulants')
        self.table_3.add_row(2, 'Bulk Herbs')
        self.table_3.add_row(3, 'Palliatives')
        self.table_3.add_row(4, 'Pheromones')
        self.table_3.add_row(5, 'Antibiotics')
        self.table_3.add_row(6, 'Combat Drug')

        self.table_4 = DescriptionTable()
        self.table_4.add_row(1, 'Envirosuits')
        self.table_4.add_row(2, 'Reclamation Suits')
        self.table_4.add_row(3, 'Navigators')
        self.table_4.add_row(4, 'Dupe Masterpieces')
        self.table_4.add_row(5, 'ShimmerCloth')
        self.table_4.add_row(6, 'ANIFX Blocker')

        self.table_4 = DescriptionTable()
        self.table_4.add_row(1, 'Excretions')
        self.table_4.add_row(2, 'Flavorings')
        self.table_4.add_row(3, 'Nectars')
        self.table_4.add_row(4, 'Pelts')
        self.table_4.add_row(5, 'ANIFX Dyes')
        self.table_4.add_row(6, 'Seedstock')

        self.table_6 = DescriptionTable()
        self.table_6.add_row(1, 'Pheromones')
        self.table_6.add_row(2, 'Artifacts')
        self.table_6.add_row(3, 'Sparx')
        self.table_6.add_row(4, 'Repulsant')
        self.table_6.add_row(5, 'Dominant')
        self.table_6.add_row(6, 'Fossils')

        self.types_table = Table()
        self.types_table.add_row(1, self.table_1.roll)
        self.types_table.add_row(2, self.table_2.roll)
        self.types_table.add_row(3, self.table_3.roll)
        self.types_table.add_row(4, self.table_4.roll)
        self.types_table.add_row(5, self.table_4.roll)
        self.types_table.add_row(6, self.table_6.roll)
        self.types_table.dice = 1


class Fl(TradeGood):
    '''Fl cargo description tables'''
    def __init__(self):
        super(Fl, self).__init__()
        self.table_1 = DescriptionTable()        # raws
        self.table_1.add_row(1, 'Bulk Carbon')
        self.table_1.add_row(2, 'Bulk Petros')
        self.table_1.add_row(3, 'Bulk Precipitates')
        self.table_1.add_row(4, 'Exotic Fluids')
        self.table_1.add_row(5, 'Organic Polymers')
        self.table_1.add_row(6, 'Bulk Synthetics')

        self.table_2 = DescriptionTable()      # samples
        self.table_2.add_row(1, 'Archeologicals')
        self.table_2.add_row(2, 'Fauna')
        self.table_2.add_row(3, 'Flora')
        self.table_2.add_row(4, 'Germanes')
        self.table_2.add_row(5, 'Flill')
        self.table_2.add_row(6, 'Chelates')

        self.table_3 = DescriptionTable()       # pharma
        self.table_3.add_row(1, 'Antifungals')
        self.table_3.add_row(2, 'Antivirals')
        self.table_3.add_row(3, 'Palliatives')
        self.table_3.add_row(4, 'Counter-prions')
        self.table_3.add_row(5, 'Antibiotics')
        self.table_3.add_row(6, 'Cold Sleep Pills')

        self.table_4 = DescriptionTable()        # novelties
        self.table_4.add_row(1, 'Silanes')
        self.table_4.add_row(2, 'Lek Emitters')
        self.table_4.add_row(3, 'Aware Blockers')
        self.table_4.add_row(4, 'Soothants')
        self.table_4.add_row(5, 'Self-Solving Puzzles')
        self.table_4.add_row(6, 'Fluidic Timepieces')

        self.table_4 = DescriptionTable()        # rares
        self.table_4.add_row(1, 'Flavorings')
        self.table_4.add_row(2, 'Unusual Fluids')
        self.table_4.add_row(3, 'Encapsulants')
        self.table_4.add_row(4, 'Insidiants')
        self.table_4.add_row(5, 'Corrosives')
        self.table_4.add_row(6, 'Exotic Aromatics')

        self.table_6 = DescriptionTable()        # imbalances
        self.table_6.add_row(1, 'In')
        self.table_6.add_row(2, 'Ri')
        self.table_6.add_row(3, 'Ic')
        self.table_6.add_row(4, 'Na')
        self.table_6.add_row(5, 'Ag')
        self.table_6.add_row(6, 'Po')

        self.types_table = Table()
        self.types_table.add_row(1, self.table_1.roll)
        self.types_table.add_row(2, self.table_2.roll)
        self.types_table.add_row(3, self.table_3.roll)
        self.types_table.add_row(4, self.table_4.roll)
        self.types_table.add_row(5, self.table_4.roll)
        self.types_table.add_row(6, self.table_6.roll)
        self.types_table.dice = 1


class Ic(TradeGood):
    '''Fl cargo description tables'''
    def __init__(self):
        super(Fl, self).__init__()
        self.table_1 = DescriptionTable()     # raws
        self.table_1.add_row(1, 'Bulk Ices')
        self.table_1.add_row(2, 'Bulk Precipitants')
        self.table_1.add_row(3, 'Bulk Ephemerals')
        self.table_1.add_row(4, 'Exotic Flora')
        self.table_1.add_row(5, 'Bulk Gases')
        self.table_1.add_row(6, 'Bulk Oxygen')

        self.table_2 = DescriptionTable()      # samples
        self.table_2.add_row(1, 'Archeologicals')
        self.table_2.add_row(2, 'Fauna')
        self.table_2.add_row(3, 'Flora')
        self.table_2.add_row(4, 'Minerals')
        self.table_2.add_row(5, 'Luminescents')
        self.table_2.add_row(6, 'Polymers')

        self.table_3 = DescriptionTable()        # pharma
        self.table_3.add_row(1, 'Antifungals')
        self.table_3.add_row(2, 'Antivirals')
        self.table_3.add_row(3, 'Palliatives')
        self.table_3.add_row(4, 'Restoratives')
        self.table_3.add_row(5, 'Antibiotics')
        self.table_3.add_row(6, 'Antiseptics')

        self.table_4 = DescriptionTable()        # novelties
        self.table_4.add_row(1, 'Heat Pumps')
        self.table_4.add_row(2, 'Mag Emitters')
        self.table_4.add_row(3, 'Percept Blockers')
        self.table_4.add_row(4, 'Silanes')
        self.table_4.add_row(5, 'Cold Light Blocks')
        self.table_4.add_row(6, 'VDHUS Blocker')

        self.table_4 = DescriptionTable()        # rares
        self.table_4.add_row(1, 'Flavorings')
        self.table_4.add_row(2, 'Unusual Fluids')
        self.table_4.add_row(3, 'Encapsulants')
        self.table_4.add_row(4, 'Insidiants')
        self.table_4.add_row(5, 'Corrosives')
        self.table_4.add_row(6, 'Exotic Aromatics')

        self.table_6 = DescriptionTable()      # uniques
        self.table_6.add_row(1, 'Fossils')
        self.table_6.add_row(2, 'Cryogems')
        self.table_6.add_row(3, 'Vision Suppressant')
        self.table_6.add_row(4, 'Fission Suppressant')
        self.table_6.add_row(5, 'Wafers')
        self.table_6.add_row(6, 'Cold Sleep Pills')


class Na(TradeGood):
    '''Na cargo description tables'''
    def __init__(self):
        super(Fl, self).__init__()
        self.table_1 = DescriptionTable()        # raws
        self.table_1.add_row(1, 'Bulk Abrasives')
        self.table_1.add_row(2, 'Bulk Gases')
        self.table_1.add_row(3, 'Bulk Minerals')
        self.table_1.add_row(4, 'Bulk Precipitates')
        self.table_1.add_row(5, 'Exotic Fauna')
        self.table_1.add_row(6, 'Exotic Flora')

        self.table_2 = DescriptionTable()      # samples
        self.table_2.add_row(1, 'Archeologicals')
        self.table_2.add_row(2, 'Fauna')
        self.table_2.add_row(3, 'Flora')
        self.table_2.add_row(4, 'Minerals')
        self.table_2.add_row(5, 'Ephemerals')
        self.table_2.add_row(6, 'Polymers')

        self.table_3 = DescriptionTable()        # novelties
        self.table_3.add_row(1, 'Branded Tools')
        self.table_3.add_row(2, 'Drinkable Lymphs')
        self.table_3.add_row(3, 'Strange Seeds')
        self.table_3.add_row(4, 'Pattern Creators')
        self.table_3.add_row(5, 'Pigments')
        self.table_3.add_row(6, 'Warm Leather')

        self.table_4 = DescriptionTable()        # rares
        self.table_4.add_row(1, 'Hummingsand')
        self.table_4.add_row(2, 'Masterpieces')
        self.table_4.add_row(3, 'Fine Carpets')
        self.table_4.add_row(4, 'Isotopes')
        self.table_4.add_row(5, 'Pelts')
        self.table_4.add_row(6, 'Seedstock')

        self.table_5 = DescriptionTable()      # self.table_5
        self.table_5.add_row(1, 'Masterpieces')
        self.table_5.add_row(2, 'Unusual Rocks')
        self.table_5.add_row(3, 'Artifacts')
        self.table_5.add_row(4, 'Non-fossil Carcasses')
        self.table_5.add_row(5, 'Replicating Clays')
        self.table_5.add_row(6, 'ANIFX Emiiter')

        self.table_6 = DescriptionTable()
        self.table_6.add_row(1, 'Ag')
        self.table_6.add_row(2, 'Ri')
        self.table_6.add_row(3, 'In')
        self.table_6.add_row(4, 'Ic')
        self.table_6.add_row(5, 'De')
        self.table_6.add_row(6, 'Fl')


class In(TradeGood):
    '''In cargo description tables'''
    self.table_1 = DescriptionTable()        # manufactureds
    self.table_1.add_row(1, 'Electronics')
    self.table_1.add_row(2, 'Photonics')
    self.table_1.add_row(3, 'Magnetics')
    self.table_1.add_row(4, 'Fluidics')
    self.table_1.add_row(5, 'Polymers')
    self.table_1.add_row(6, 'Gravitics')

    self.table_2 = DescriptionTable()      # scrap/waste
    self.table_2.add_row(1, 'Obsoletes')
    self.table_2.add_row(2, 'Used Goods')
    self.table_2.add_row(3, 'Reparables')
    self.table_2.add_row(4, 'Radioactives')
    self.table_2.add_row(5, 'Metals')
    self.table_2.add_row(6, 'Sludges')

    self.table_3 = DescriptionTable()      # manufactureds
    self.table_3.add_row(1, 'Biologics')
    self.table_3.add_row(2, 'Mechanicals')
    self.table_3.add_row(3, 'Textiles')
    self.table_3.add_row(4, 'Weapons')
    self.table_3.add_row(5, 'Armor')
    self.table_3.add_row(6, 'Robots')

    self.table_4 = DescriptionTable()        # pharma
    self.table_4.add_row(1, 'Nostrums')
    self.table_4.add_row(2, 'Restoratives')
    self.table_4.add_row(3, 'Palliatives')
    self.table_4.add_row(4, 'Chelates')
    self.table_4.add_row(5, 'Antidotes')
    self.table_4.add_row(6, 'Antitoxins')

    self.table_5 = DescriptionTable()     # data
    self.table_5.add_row(1, 'Software')
    self.table_5.add_row(2, 'Databases')
    self.table_5.add_row(3, 'Expert Systems')
    self.table_5.add_row(4, 'Upgrades')
    self.table_5.add_row(5, 'Backups')
    self.table_5.add_row(6, 'Raw Sensings')

    self.table_6 = DescriptionTable()      # consumables
    self.table_6.add_row(1, 'Disposables')
    self.table_6.add_row(2, 'Respirators')
    self.table_6.add_row(3, 'Filter Masks')
    self.table_6.add_row(4, 'Combination')
    self.table_6.add_row(5, 'Parts')
    self.table_6.add_row(6, 'Improvements')


class Po(TradeGood):
    '''Po cargo description tables'''
    self.table_1 = DescriptionTable()        # raws
    self.table_1.add_row(1, 'Bulk Nutrients')
    self.table_1.add_row(2, 'Bulk Fibers')
    self.table_1.add_row(3, 'Bulk Organics')
    self.table_1.add_row(4, 'Bulk Minerals')
    self.table_1.add_row(5, 'Bulk Textiles')
    self.table_1.add_row(6, 'Exotic Flora')

    self.table_2 = DescriptionTable()       # entertainments
    self.table_2.add_row(1, 'Art')
    self.table_2.add_row(2, 'Recordings')
    self.table_2.add_row(3, 'Writings')
    self.table_2.add_row(4, 'Tactiles')
    self.table_2.add_row(5, 'Osmancies')
    self.table_2.add_row(6, 'Wafers')

    self.table_3 = DescriptionTable()        # novelties
    self.table_3.add_row(1, 'Strange Crystals')
    self.table_3.add_row(2, 'Strange Seeds')
    self.table_3.add_row(3, 'Pigments')
    self.table_3.add_row(4, 'Emotion Lighting')
    self.table_3.add_row(5, 'Silanes')
    self.table_3.add_row(6, 'Flora')

    self.table_4 = DescriptionTable()        # raws
    self.table_4.add_row(1, 'Gemstones')
    self.table_4.add_row(2, 'Antiques')
    self.table_4.add_row(3, 'Collectibles')
    self.table_4.add_row(4, 'Allotropes')
    self.table_4.add_row(5, 'Spices')
    self.table_4.add_row(6, 'Seedstock')

    self.table_5 = DescriptionTable()      # uniques
    self.table_5.add_row(1, 'Masterpieces')
    self.table_5.add_row(2, 'Exotic Flora')
    self.table_5.add_row(3, 'Antiques')
    self.table_5.add_row(4, 'Incomprehensibles')
    self.table_5.add_row(5, 'fossils')
    self.table_5.add_row(6, 'VHDUS Emitter')

    self.table_6 = DescriptionTable()        # imbalances
    self.table_6.add_row(1, 'In')
    self.table_6.add_row(2, 'Ri')
    self.table_6.add_row(3, 'Fl')
    self.table_6.add_row(4, 'Ic')
    self.table_6.add_row(5, 'Ag')
    self.table_6.add_row(6, 'Va')


class Ri(TradeGood):
    '''Ri cargo description tables'''
    self.table_1 = DescriptionTable()        # raws
    self.table_1.add_row(1, 'Bulk Foodstuffs')
    self.table_1.add_row(2, 'Bulk Protein')
    self.table_1.add_row(3, 'Carbs')
    self.table_1.add_row(4, 'Fats')
    self.table_1.add_row(5, 'Exotic Flora')
    self.table_1.add_row(6, 'Exotic Fauna')

    self.table_2 = DescriptionTable()        # novelties
    self.table_2.add_row(1, 'Echostones')
    self.table_2.add_row(2, 'Self-Defenders')
    self.table_2.add_row(3, 'Attractants')
    self.table_2.add_row(4, 'Sophont Cuisine')
    self.table_2.add_row(5, 'Sophont Hats')
    self.table_2.add_row(6, 'Variable Tattoos')

    self.table_3 = DescriptionTable()      # consumables
    self.table_3.add_row(1, 'Branded Foods')
    self.table_3.add_row(2, 'Branded Drinks')
    self.table_3.add_row(3, 'Branded Clothes')
    self.table_3.add_row(4, 'Flavored Drinks')
    self.table_3.add_row(5, 'Flowers')
    self.table_3.add_row(6, 'Music')

    self.table_4 = DescriptionTable()        # rares
    self.table_4.add_row(1, 'Delicacies')
    self.table_4.add_row(2, 'Spices')
    self.table_4.add_row(3, 'Tisanes')
    self.table_4.add_row(4, 'Nectars')
    self.table_4.add_row(5, 'Pelts')
    self.table_4.add_row(6, 'Variable Tattoos')

    self.table_5 = DescriptionTable()      # uniques
    self.table_5.add_row(1, 'Antique Art')
    self.table_5.add_row(2, 'Masterpieces')
    self.table_5.add_row(3, 'Artifacts')
    self.table_5.add_row(4, 'Fine Art')
    self.table_5.add_row(5, 'Meson Barriers')
    self.table_5.add_row(6, 'Famous Wafers')

    self.table_6 = DescriptionTable()       # entertainments
    self.table_6.add_row(1, 'Edutainments')
    self.table_6.add_row(2, 'Recordings')
    self.table_6.add_row(3, 'Writings')
    self.table_6.add_row(4, 'Tactiles')
    self.table_6.add_row(5, 'Osmancies')
    self.table_6.add_row(6, 'Wafers')


class Va(TradeGood):
    '''Va cargo description tables'''
    self.table_1 = DescriptionTable()        # raws
    self.table_1.add_row(1, 'Bulk Dusts')
    self.table_1.add_row(2, 'Bulk Minerals')
    self.table_1.add_row(3, 'Bulk Metals')
    self.table_1.add_row(4, 'Radioactive Ores')
    self.table_1.add_row(5, 'Bulk Particulates')
    self.table_1.add_row(6, 'Ephemerals')

    self.table_2 = DescriptionTable()        # novelties
    self.table_2.add_row(1, 'Branded Vacc Suits')
    self.table_2.add_row(2, 'Awareness Pinger')
    self.table_2.add_row(3, 'Strange Seeds')
    self.table_2.add_row(4, 'Pigments')
    self.table_2.add_row(5, 'Unusual Minerals')
    self.table_2.add_row(6, 'Exotic Crystals')

    self.table_3 = DescriptionTable()      # consumables
    self.table_3.add_row(1, 'Branded Oxygen')
    self.table_3.add_row(2, 'Vacc Suit Scents')
    self.table_3.add_row(3, 'Vacc Suit Patches')
    self.table_3.add_row(4, 'Branded Tools')
    self.table_3.add_row(5, 'Holo-Companions')
    self.table_3.add_row(6, 'Flavored Air')

    self.table_4 = DescriptionTable()        # rares
    self.table_4.add_row(1, 'Vacc Gems')
    self.table_4.add_row(2, 'Unusual Dusts')
    self.table_4.add_row(3, 'Insulants')
    self.table_4.add_row(4, 'Crafted Devices')
    self.table_4.add_row(5, 'Rare Minerals')
    self.table_4.add_row(6, 'Catalysts')

    self.table_5 = DescriptionTable()        # samples
    self.table_5.add_row(1, 'Archeologicals')
    self.table_5.add_row(2, 'Fauna')
    self.table_5.add_row(3, 'Flora')
    self.table_5.add_row(4, 'Minerals')
    self.table_5.add_row(5, 'Ephemerals')
    self.table_5.add_row(6, 'Polymers')

    self.table_6 = DescriptionTable()      # scrap/waste
    self.table_6.add_row(1, 'Obsoletes')
    self.table_6.add_row(2, 'Used Goods')
    self.table_6.add_row(3, 'Reparables')
    self.table_6.add_row(4, 'Plutonium')
    self.table_6.add_row(5, 'Metals')
    self.table_6.add_row(6, 'Sludges')


class Cp(TradeGood):
    '''Cp cargo description tables'''
    self.table_1 = DescriptionTable()     # data
    self.table_1.add_row(1, 'Software')
    self.table_1.add_row(2, 'Expert Systems')
    self.table_1.add_row(3, 'Databases')
    self.table_1.add_row(4, 'Upgrades')
    self.table_1.add_row(5, 'Backups')
    self.table_1.add_row(6, 'Raw Sensings')

    self.table_2 = DescriptionTable()        # novelties
    self.table_2.add_row(1, 'Incenses')
    self.table_2.add_row(2, 'Contemplatives')
    self.table_2.add_row(3, 'Cold Welders')
    self.table_2.add_row(4, 'Polymer Sheets')
    self.table_2.add_row(5, 'Hats')
    self.table_2.add_row(6, 'Skin Tones')

    self.table_3 = DescriptionTable()      # consumables
    self.table_3.add_row(1, 'Branded Clothing')
    self.table_3.add_row(2, 'Branded Devices')
    self.table_3.add_row(3, 'Flavored Drinks')
    self.table_3.add_row(4, 'Flavorings')
    self.table_3.add_row(5, 'Decorations')
    self.table_3.add_row(6, 'Group Symbols')

    self.table_4 = DescriptionTable()
    self.table_4.add_row(1, 'Monumental Art')
    self.table_4.add_row(2, 'Holo Sculpture')
    self.table_4.add_row(3, 'Collectible Books')
    self.table_4.add_row(4, 'Jewelry')
    self.table_4.add_row(5, 'Museum Items')
    self.table_4.add_row(6, 'Monumental Art')

    self.table_5 = DescriptionTable()
    self.table_5.add_row(1, 'Coinage')
    self.table_5.add_row(2, 'Currency')
    self.table_5.add_row(3, 'Money Cards')
    self.table_5.add_row(4, 'Gold')
    self.table_5.add_row(5, 'Silver')
    self.table_5.add_row(6, 'Platinum')

    self.table_6 = DescriptionTable()
    self.table_6.add_row(1, 'Regulations')
    self.table_6.add_row(2, 'Synchronizations')
    self.table_6.add_row(3, 'Expert Systems')
    self.table_6.add_row(4, 'Educationals')
    self.table_6.add_row(5, 'Mandates')
    self.table_6.add_row(6, 'Accountings')
