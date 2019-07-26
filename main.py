import unittest

from app import blueprint
from app.main import create_app

app = create_app()
app.register_blueprint(blueprint)

app.app_context().push()

@app.cli.command('test')
def test():
     tests = unittest.TestLoader().discover('app/main/test', pattern='*_test.py')
     result = unittest.TextTestRunner(verbosity=2).run(tests)
     if result.wasSuccessful():
          return 0
     return 1
     
if __name__ == '__main__':
     app.run()