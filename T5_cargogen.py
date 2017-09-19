#! /usr/bin/env python2
'''SWN tags'''

import logging
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Regexp, Optional

from T5_cargogen.simple import TradeCargo
from T5_cargogen.trade_codes import TradeCodes, Uwp

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.DEBUG)

APP = Flask(__name__)
APP.config['SECRET_KEY'] = 'baiNgeeB2ciNai7naeyaich0u'
BOOTSTRAP = Bootstrap(APP)
MANAGER = Manager(APP)


class World(object):
    '''World class'''
    def __init__(self, uwp):
        self.uwp = Uwp(uwp)
        LOGGER.debug('uwp = %s', uwp)
        LOGGER.debug('self.uwp = %s', self.uwp)
        self.trade_codes = TradeCodes(self.uwp)
        LOGGER.debug('self.trade_codes = %s', self.trade_codes)


class SourceWorldForm(Form):
    '''Source world'''
    source_uwp = StringField(
        'Source world UWP',
        validators=[Regexp(r'^[A-HYX][0-9A-HJ-NP-Z]{6}\-[0-9A-HJ-NP-Z]$')])
    market_uwp = StringField(
        'Market world UWP',
        validators=[
            Optional(),
            Regexp(r'^[A-HYX][0-9A-HJ-NP-Z]{6}\-[0-9A-HJ-NP-Z]$')])
    submit = SubmitField('Submit')


@APP.route('/', methods=['GET', 'POST'])
def index():
    '''Generate cargo'''
    cargo = TradeCargo()
    form = SourceWorldForm()
    if form.validate_on_submit():
        LOGGER.debug('form.source_uwp.data = %s', form.source_uwp.data)
        # form.uwp.data is unicode, convert
        source_world = World(str(form.source_uwp.data))
        cargo.generate_cargo(
            str(source_world.uwp),
            source_world.trade_codes.list())
        if form.market_uwp.data:
            market_world = World(str(form.market_uwp.data))
            cargo.generate_sale(
                str(market_world.uwp),
                market_world.trade_codes.list())
            market_world_uwp = str(market_world.uwp)
            market_world_tcs = str(market_world.trade_codes)
        else:
            market_world_uwp = ''
            market_world_tcs = ''

    return render_template(
        'index.html',
        cargo=cargo,
        source_world_uwp=str(source_world.uwp),
        source_world_tcs=str(source_world.trade_codes),
        market_world_uwp=market_world_uwp,
        market_world_tcs=market_world_tcs,
        form=form)


if __name__ == '__main__':
    MANAGER.run()
