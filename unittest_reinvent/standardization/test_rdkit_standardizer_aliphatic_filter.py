from reinvent_chemistry.enums import FilterTypesEnum
from unittest_reinvent.fixtures.test_data import BENZENE, PENTYLBENZENE
from unittest_reinvent.standardization.base_rdkit_standardizer import BaseRDKitStandardizer


class TestRDKitStandardizerAliphaticFilter(BaseRDKitStandardizer):

    def setUp(self):
        filter_types = FilterTypesEnum()
        self.raw_config = {"name": filter_types.ALIPHATIC_CHAIN_FILTER, "parameters": {}}
        super().setUp()

        self.compound_1 = BENZENE

    def test_standardizer_positive(self):
        result = self.standardizer.apply_filter(self.compound_1)
        self.assertEqual(self.compound_1, result)

    def test_standardizer_negative(self):
        result = self.standardizer.apply_filter(PENTYLBENZENE)
        self.assertIsNone(result)
