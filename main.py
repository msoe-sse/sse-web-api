import unittest

from app import app

@app.cli.command('test')
def test():
     tests = unittest.TestLoader().discover('app/test', pattern='*_test.py')
     result = unittest.TextTestRunner(verbosity=2).run(tests)
     if result.wasSuccessful():
          return 0
     return 1
     
if __name__ == '__main__':
     app.run()