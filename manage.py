#!/usr/bin/env python
'''T5_cargogen manage.py'''

from __future__ import print_function
import os
from app import create_app
from flask_script import Manager, Shell

APP = create_app(os.getenv('FLASK_CONFIG') or 'default')
MANAGER = Manager(APP)


COV = None
if os.environ.get('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='app/*')
    COV.start()


def make_shell_context():
    '''Shell context'''
    return dict(app=APP)


MANAGER.add_command("shell", Shell(make_context=make_shell_context))


@MANAGER.command
def test(coverage=False):
    """Run the unit tests."""
    if coverage and not os.environ.get('FLASK_COVERAGE'):
        import sys
        os.environ['FLASK_COVERAGE'] = '1'
        os.execvp(sys.executable, [sys.executable] + sys.argv)
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://{}/index.html'.format(covdir))
        COV.erase()


if __name__ == '__main__':
    MANAGER.run()
