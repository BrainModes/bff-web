import unittest
from tests.prepare_test import SetUpTest, PrepareTest
from tests.logger import Logger


def setUpModule():
    pass


def tearDownModule():
    pass


class TestAPI(unittest.TestCase):
    log = Logger(name='test_api.log')
    test = SetUpTest(log)
    app = PrepareTest().app


    @classmethod
    def setUpClass(cls) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_01_api(self):
        self.log.info("test case 1")
        app = self.app
