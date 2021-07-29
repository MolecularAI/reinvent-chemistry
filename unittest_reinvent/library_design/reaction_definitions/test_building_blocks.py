import unittest

import pandas as pd

from reinvent_chemistry.library_design.reaction_definitions.building_blocks import BuildingBlocks
from unittest_reinvent.fixtures.paths import REACTION_DEFINITIONS_PATH
from unittest_reinvent.library_design.reaction_filters.fixtures import REACTION_SUZUKI_NAME, TWO_DECORATIONS_SUZUKI, \
    TWO_DECORATIONS_AFTER_SUZUKI
from unittest_reinvent.fixtures.test_data import REACTION_SUZUKI_NAME


class TestBuildingBlocks(unittest.TestCase):

    def setUp(self):
        self._building_blocks = BuildingBlocks(REACTION_DEFINITIONS_PATH)
        df_dict = {"Step": [1],
                   "Scaffold": [TWO_DECORATIONS_SUZUKI],
                   "SMILES": [TWO_DECORATIONS_AFTER_SUZUKI]
                   }

        self._dataframe = pd.DataFrame(df_dict)

    def test_create_building_blocks(self):
        blocks = self._building_blocks.create(REACTION_SUZUKI_NAME, 0, self._dataframe)
        first_compound = blocks[0]
        self.assertEqual(len(blocks), 1)
        self.assertEqual(len(first_compound.building_block_pairs), 32)
        self.assertEqual(first_compound.reaction_name, REACTION_SUZUKI_NAME)
        self.assertEqual(first_compound.compound, TWO_DECORATIONS_AFTER_SUZUKI)
        self.assertEqual(first_compound.attachment_position, 0)
