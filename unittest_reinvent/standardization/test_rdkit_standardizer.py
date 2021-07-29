from reinvent_chemistry.enums import FilterTypesEnum
from unittest_reinvent.fixtures.test_data import CELECOXIB, BENZENE
from unittest_reinvent.standardization.base_rdkit_standardizer import BaseRDKitStandardizer


class TestRDKitStandardizer(BaseRDKitStandardizer):

    def setUp(self):
        filter_types = FilterTypesEnum()
        self.raw_config = {"name": filter_types.DEFAULT, "parameters": {"max_heavy_atoms": 10}}
        super().setUp()

        self.compound_1 = BENZENE

    def test_standardizer_positive_outcome(self):
        result = self.standardizer.apply_filter(self.compound_1)
        self.assertEqual(self.compound_1, result)

    def test_standardizer_negative_outcome(self):
        result = self.standardizer.apply_filter(CELECOXIB)
        self.assertIsNone(result)
