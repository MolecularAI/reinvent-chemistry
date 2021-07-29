from rdkit.Chem import GetDistanceMatrix
from rdkit.Chem.Crippen import MolLogP
from rdkit.Chem.Descriptors import MolWt
from rdkit.Chem.Lipinski import NumHAcceptors, NumHDonors, NumRotatableBonds

import numpy as np
from rdkit.Chem.MolSurf import TPSA
from rdkit.Chem.rdMolDescriptors import CalcNumRings, CalcNumAtomStereoCenters


class PhysChemDescriptors:
    """Molecular descriptors.
    The descriptors in this class are mostly calculated RDKit phys-chem properties.
    """

    def maximum_graph_length(self, mol):
        return int(np.max(GetDistanceMatrix(mol)))

    def hba_libinski(self, mol):
        return NumHAcceptors(mol)

    def hbd_libinski(self, mol):
        return NumHDonors(mol)

    def mol_weight(self, mol):
        return MolWt(mol)

    def number_of_rings(self, mol):
        return CalcNumRings(mol)

    def number_of_rotatable_bonds(self, mol):
        return NumRotatableBonds(mol)

    def slog_p(self, mol):
        return MolLogP(mol)

    def tpsa(self, mol):
        return TPSA(mol)

    def number_of_stereo_centers(self, mol):
        return CalcNumAtomStereoCenters(mol)
