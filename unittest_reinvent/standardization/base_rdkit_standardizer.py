import unittest

from dacite import from_dict

from reinvent_chemistry import Conversions
from reinvent_chemistry.standardization.filter_configuration import FilterConfiguration
from reinvent_chemistry.standardization.rdkit_standardizer import RDKitStandardizer
from unittest_reinvent.standardization.fixtures import MockLogger


class BaseRDKitStandardizer(unittest.TestCase):

    def setUp(self):
        self.chemistry = Conversions()
        logger = MockLogger()
        self.raw_config = None if None else self.raw_config
        if not self.raw_config:
            raise NotImplemented('Please, assign value to self.raw_config in the derived test class')
        config = from_dict(data_class=FilterConfiguration, data=self.raw_config)
        filter_configs = [config]
        self.standardizer = RDKitStandardizer(filter_configs, logger)
