import unittest

from app.main import create_app
from flask_script import Manager


app = create_app()

@manager.command
def run():
     app.run()

@manager.command
def test():
     tests = unittest.TestLoader().discover('app/main/test', pattern='*_test.py')
     result = unittest.TextTestRunner(verbosity=2).run(tests)
     if result.wasSuccessful():
          return 0
     return 1
     
if __name__ == '__main__':
     app.run()