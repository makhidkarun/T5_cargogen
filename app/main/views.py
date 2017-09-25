'''T5_cargogen views.py'''

import logging
from flask import render_template
from . import main
from .forms import SourceWorldForm

from .simple import TradeCargo
from .trade_codes import TradeCodes, Uwp

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)


class World(object):
    '''World class'''
    def __init__(self, uwp):
        self.uwp = Uwp(uwp)
        LOGGER.debug('uwp = %s', uwp)
        LOGGER.debug('self.uwp = %s', self.uwp)
        self.trade_codes = TradeCodes(self.uwp)
        LOGGER.debug('self.trade_codes = %s', self.trade_codes)


@main.route('/', methods=['GET', 'POST'])
def index():
    '''Generate cargo'''
    cargo = TradeCargo()
    form = SourceWorldForm()
    source_world_uwp = ''
    source_world_tcs = ''
    results = list()
    if form.validate_on_submit():
        LOGGER.debug('form.source_uwp.data = %s', form.source_uwp.data)
        # form.uwp.data is unicode, convert
        if form.source_uwp.data:
            source_world = World(str(form.source_uwp.data))
            cargo.generate_cargo(
                str(source_world.uwp),
                source_world.trade_codes.list())
            source_world_uwp = str(source_world.uwp)
            source_world_tcs = str(source_world.trade_codes)
        if form.market_uwp.data:
            LOGGER.debug('form.market_uwp.data = %s', form.market_uwp.data)
            for uwp in form.market_uwp.data.split(' '):
                LOGGER.debug('uwp = %s', uwp)
                market_world = World(str(uwp))
                cargo.generate_sale(
                    str(market_world.uwp),
                    market_world.trade_codes.list())
                results.append([
                    str(market_world.uwp),
                    str(market_world.trade_codes), cargo.str_price()])

    LOGGER.debug('results = %s', results)
    return render_template(
        'index.html',
        cargo=cargo,
        source_world_uwp=source_world_uwp,
        source_world_tcs=source_world_tcs,
        results=results,
        form=form)
