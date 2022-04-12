
from rdkit import Chem

from reinvent_chemistry.library_design.reaction_filters import ReactionFiltersEnum
from unittest_reinvent.fixtures.test_data import REACTION_SUZUKI, SCAFFOLD_SUZUKI, DECORATION_SUZUKI, \
    SCAFFOLD_NO_SUZUKI, DECORATION_NO_SUZUKI
from unittest_reinvent.library_design.reaction_filters.base_reaction_filter import BaseTestReactionFilter


class TestNonSelectiveReactionFilter(BaseTestReactionFilter):

    def setUp(self):
        self.type = ReactionFiltersEnum().NON_SELECTIVE
        self.reactions = [[REACTION_SUZUKI]]
        super().setUp()

    def test_with_suzuki_reagents(self):
        scaffold = SCAFFOLD_SUZUKI
        decoration = DECORATION_SUZUKI
        scaffold = self._attachment_points.add_attachment_point_numbers(scaffold, canonicalize=False)
        molecule: Chem.Mol = self._bond_maker.join_scaffolds_and_decorations(scaffold, decoration)
        score = self.reaction_filter.evaluate(molecule)
        self.assertEqual(1.0, score)

    def test_with_non_suzuki_reagents(self):
        scaffold = SCAFFOLD_NO_SUZUKI
        decoration = DECORATION_NO_SUZUKI
        scaffold = self._attachment_points.add_attachment_point_numbers(scaffold, canonicalize=False)
        molecule: Chem.Mol = self._bond_maker.join_scaffolds_and_decorations(scaffold, decoration)
        score = self.reaction_filter.evaluate(molecule)
        self.assertEqual(0.0, score)
