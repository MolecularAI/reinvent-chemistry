import unittest

from reinvent_chemistry.library_design.reaction_definitions.standard_definitions import StandardDefinitions
from unittest_reinvent.fixtures.paths import REACTION_DEFINITIONS_PATH


class TestStandardDefinitions(unittest.TestCase):

    def setUp(self):
        self._definitions = StandardDefinitions(REACTION_DEFINITIONS_PATH)
        self.valid_definition = '[#6;$(C[C;$(C([#6]))]):4]-!@[N;$([NH1;D2](C)C);!$(N-[#6]=[*]);$(N([C])):3]>>[#6:4][*].[N:3][*]'

    def test_get_reaction_definition(self):
        definition = self._definitions.get_reaction_definition('reductiveamination')
        self.assertIsNotNone(definition)
        self.assertEqual(self.valid_definition, definition)

    def test_get_leaving_group_pairs(self):
        leaving_groups = self._definitions.get_leaving_group_pairs('reductiveamination')
        self.assertIsNotNone(leaving_groups)
        self.assertEqual(leaving_groups[0].leaving_group_scaffold, '*=[O]')
        self.assertEqual(leaving_groups[0].leaving_group_decoration, '')

    def test_get_leaving_group_pairs_missing(self):
        with self.assertRaises(IOError) as context:
            leaving_groups = self._definitions.get_leaving_group_pairs('reductiveamination_1')
        self.assertTrue("there are no definitions for reaction name: reductiveamination_1" in str(context.exception))
