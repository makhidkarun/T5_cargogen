#! /usr/bin/env python2
'''SWN tags'''

import logging
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_script import Manager
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import Regexp

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
    uwp = StringField(
        'Source world UWP',
        validators=[Regexp(r'^[A-HYX][0-9A-HJ-NP-Z]{6}\-[0-9A-HJ-NP-Z]$')])
    submit = SubmitField('Submit')


@APP.route('/', methods=['GET', 'POST'])
def index():
    '''Generate cargo'''
    cargo = TradeCargo()
    form=SourceWorldForm()
    if form.validate_on_submit():
        LOGGER.debug('form validated')
        LOGGER.debug('form.uwp.data type is %s', type(form.uwp.data))
        LOGGER.debug('form.uwp.data = %s', form.uwp.data)
        # form.uwp.data is unicode, convert
        world = World(str(form.uwp.data))
        cargo.generate_cargo(str(world.uwp), world.trade_codes.list())

    return render_template('index.html', cargo=cargo, form=form)


if __name__ == '__main__':
    MANAGER.run()
