import unittest

from rdkit.Chem.rdmolfiles import MolToSmiles

from reinvent_chemistry import Conversions
from reinvent_chemistry.library_design import AttachmentPoints
from reinvent_chemistry.library_design.bond_maker import BondMaker
from reinvent_chemistry.library_design.fragment_reactions import FragmentReactions
from unittest_reinvent.fixtures.test_data import METAMIZOLE_SCAFFOLD_LABELED, METAMIZOLE_DECORATIONS, \
    METAMIZOLE_LABELED_COMPONENTS
from unittest_reinvent.library_design.fixtures import ANILINE_DERIVATIVE, SLICED_ANILINE_DERIVATIVE, \
    ANILINE_DERIVATIVE_DECORATIONS


class TestBondMaker(unittest.TestCase):

    def setUp(self):
        self._bond_maker = BondMaker()
        self._attachments = AttachmentPoints()
        self._conversions = Conversions()
        self.reactions = FragmentReactions()
        self.expected_results = ANILINE_DERIVATIVE
        self.unlabeled_scaffold_A = SLICED_ANILINE_DERIVATIVE
        self.decorations_A = ANILINE_DERIVATIVE_DECORATIONS
        self.scaffold_labeled_B = METAMIZOLE_SCAFFOLD_LABELED
        self.decorations_B = METAMIZOLE_DECORATIONS
        self.expected_results_B = METAMIZOLE_LABELED_COMPONENTS

    def test_join_randomized_scaffold_and_decorations(self):
        scaffold = self._attachments.add_attachment_point_numbers(self.unlabeled_scaffold_A, canonicalize=False)
        scaffold_mol = self._conversions.smile_to_mol(scaffold)
        scaffold = self._conversions.mol_to_random_smiles(scaffold_mol)

        molecule = self._bond_maker.join_scaffolds_and_decorations(scaffold, self.decorations_A)
        complete_smile = MolToSmiles(molecule, isomericSmiles=False, canonical=True)

        self.assertEqual(self.expected_results, complete_smile)

    def test_join_scaffolds_and_decorations_keep_labels(self):
        molecule = self._bond_maker.join_scaffolds_and_decorations(self.scaffold_labeled_B, self.decorations_B,
                                                                   keep_labels_on_atoms=True)
        complete_smile = MolToSmiles(molecule, isomericSmiles=False, canonical=True)
        self.assertEqual(self.expected_results_B, complete_smile)

