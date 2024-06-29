import os
import sys
import unittest
from flask.cli import FlaskGroup
from src import create_app

config = os.environ.get("CONFIG")
app = create_app(config)
cli = FlaskGroup(app)


@cli.command("tests")
def run_tests():
    tests = unittest.TestLoader().discover("./src")
    results = unittest.TextTestRunner(verbosity=2).run(tests)
    if not results.wasSuccessful():
        sys.exit()


if __name__ == "__main__":
    cli()
