from . import TestBaseCase 

class TestAppConfig(TestBaseCase):
    def setUp(self) -> None:
        super().setUp()
        self.client = self.app.test_client()
        
    def test_app_config(self) -> None:
        self.assertTrue(self.app.config["TESTING"])