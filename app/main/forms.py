'''T5_cargogen forms.py'''

import re
import logging
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import Regexp, Optional

LOGGER = logging.getLogger(__name__)
LOGGER.setLevel(logging.ERROR)

UWP_REGEXP = r'^[A-HYX][0-9A-HJ-NP-Z]{6}\-[0-9A-HJ-NP-Z]$'
UWPS_REGEXP = r'\b[A-HYX][0-9A-HJ-NP-Z]{6}\-[0-9A-HJ-NP-Z]\b'


class SourceWorldForm(FlaskForm):
    '''Source world'''
    source_uwp = StringField(
        'Source world UWP',
        validators=[Regexp(UWP_REGEXP)])
    market_uwp = StringField(
        'Market world UWP',
        validators=[
            Optional()])
    submit = SubmitField('Submit')

    @staticmethod
    def validate_market_uwp(form, field):
        '''Custom validator to match multiple UWPs'''
        uwps = re.findall(UWPS_REGEXP, field.data)
        LOGGER.debug('uwps = %s', uwps)
        if len(uwps) == 0:
            msg = 'Invalid UWP or UWPs in {}'.format(
                field.data)
            raise ValidationError(msg)
        else:
            field.data = ' '.join(uwps)
            LOGGER.debug('%s.data = %s', field.name, field.data)
