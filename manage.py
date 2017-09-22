#!/usr/bin/env python
'''T5_cargogen manage.py'''

import os
from app import create_app
from flask_script import Manager, Shell

APP = create_app(os.getenv('FLASK_CONFIG') or 'default')
MANAGER = Manager(APP)


def make_shell_context():
    '''Shell context'''
    return dict(app=APP)


MANAGER.add_command("shell", Shell(make_context=make_shell_context))


@MANAGER.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    MANAGER.run()
