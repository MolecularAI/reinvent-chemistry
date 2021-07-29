import unittest

from reinvent_chemistry import Conversions
from reinvent_chemistry.standardization.rdkit_standardizer import RDKitStandardizer
from unittest_reinvent.fixtures.test_data import CELECOXIB2
from unittest_reinvent.standardization.fixtures import MockLogger


class TestRDKitStandardizerNoConfig(unittest.TestCase):

    def setUp(self):
        self.chemistry = Conversions()
        logger = MockLogger()
        filter_configs = []
        self.standardizer = RDKitStandardizer(filter_configs, logger)

        self.compound_1 = CELECOXIB2

    def test_standardizer_1(self):
        result = self.standardizer.apply_filter(self.compound_1)
        self.assertEqual(self.compound_1, result)
