import unittest
from src import create_app


class TestBaseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.app = create_app(config="testing")
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self) -> None:
        self.app_context.pop()
        self.app = None
        self.app_context = None
