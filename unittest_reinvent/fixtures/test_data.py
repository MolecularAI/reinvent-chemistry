import numpy as np

INVALID = 'INVALID'
NONSENSE = 'C1CC(Br)CCC1[ClH]'
ASPIRIN = 'O=C(C)Oc1ccccc1C(=O)O'
ASPIRIN2 = 'CC(=O)Oc1ccccc1C(=O)O'  # alternate style
CELECOXIB = 'O=S(=O)(c3ccc(n1nc(cc1c2ccc(cc2)C)C(F)(F)F)cc3)N'
CELECOXIB2 = "Cc1ccc(-c2cc(C(F)(F)F)nn2-c2ccc(S(N)(=O)=O)cc2)cc1"  # alternate style
CELECOXIB_C = "O=S(=O)(c3ccc(n1nc(cc1c2ccc(cc2)C)C(F)(F)F)cc3)NC"
IBUPROFEN = 'CC(C)Cc1ccc(cc1)[C@@H](C)C(=O)O'
ETHANE = 'CC'
PROPANE = 'CCC'
BUTANE = 'CCCC'
PENTANE = 'CCCCC'
HEXANE = 'CCCCCC'
METAMIZOLE = 'CC1=C(C(=O)N(N1C)C2=CC=CC=C2)N(C)CS(=O)(=O)O'
CAFFEINE = 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'
COCAINE = 'CN1C2CCC1C(C(C2)OC(=O)C3=CC=CC=C3)C(=O)OC'
BENZENE = 'c1ccccc1'
TOLUENE = 'c1ccccc1C'
ANILINE = 'c1ccccc1N'
AMOXAPINE = 'C1CN(CCN1)C2=NC3=CC=CC=C3OC4=C2C=C(C=C4)Cl'
GENTAMICIN = 'CC(C1CCC(C(O1)OC2C(CC(C(C2O)OC3C(C(C(CO3)(C)O)NC)O)N)N)N)NC'
METHOXYHYDRAZINE = 'CONN'
HYDROPEROXYMETHANE = 'COO'
PARACETAMOL = "CC(=O)NC1=CC=C(C=C1)O"
ETHANOL = "CCO"
BUTAN_1_AMINE = "CCCCN"
CYCLODECANE = "C1CCCCCCCCC1"
CYCLOUNDERCANE = "C1CCCCCCCCCC1"
PACLITAXEL = "CC1=C2C(C(=O)C3(C(CC4C(C3C(C(C2(C)C)(CC1OC(=O)C(C(C5=CC=CC=C5)NC(=O)C6=CC=CC=C6)O)O)OC(=O)C7=CC=CC=C7)(CO4)OC(=O)C)O)C)OC(=O)C"
DECALIN = "C1CCC2CCCCC2C1"
BENZO_A_PYRENE = "c1ccc2c(c1)cc3ccc4cccc5c4c3c2cc5"
ISOHEPTANE = "CCC(C)C(C)C"
METHYL_3_O_TOLYL_PROPYL_AMINE = "CN[CH]CCc1ccccc1C"  # non-stereo
METHYL_3_O_TOLYL_PROPYL_AMINE2 = "Cc1ccccc1CC[C@H]NC"  # alternate style
PENTYLBENZENE = "CCCCCC1=CC=CC=C1"
COCAINE_FRAGMENT = "CN1C2CCC1C(C(C2)OC(=O)c3ccccc3)C(=O)O[*:0]"
CELECOXIB_FRAGMENT = "*c1cc(C(F)(F)F)nn1-c1ccc(S(N)(=O)=O)cc1"
METHYLPHEMYL_FRAGMENT = "*c1ccc(C)cc1"
DOPAMINE = "C1=CC(=C(C=C1CCN)O)O"
SCAFFOLD_SUZUKI = 'Cc1ccc(cc1)c2cc(nn2c3ccc(cc3)S(=O)(=O)N)[*]'
REACTION_SUZUKI = "[*;$(c2aaaaa2),$(c2aaaa2):1]-!@[*;$(c2aaaaa2),$(c2aaaa2):2]>>[*:1][*].[*:2][*]"
DECORATION_SUZUKI = '[*]c1ncncc1'
TWO_DECORATIONS_SUZUKI = '[*]c1ncncc1|[*]c1ncncc1'
TWO_DECORATIONS_ONE_SUZUKI = '[*]c1ncncc1|[*]C'
SCAFFOLD_NO_SUZUKI = '[*:0]Cc1ccc(cc1)c2cc(nn2c3ccc(cc3)S(=O)(=O)N)'
DECORATION_NO_SUZUKI = '[*]C'
SCAFFOLD_TO_DECORATE = "[*]c1ccc(cc1)c2cc(nn2c3ccc(cc3)S(=O)(=O)N)[*]"
SCAFFOLD_TO_DECORATE_NUMBERED = "[*:0]c1c([*:1])cc2c(n1)c(c(cn2)c3cnn(c3)C4CCC(CC4)N(C)C(=O)C)OC"
CELECOXIB_SCAFFOLD = 'Cc1ccc(cc1)c2cc(nn2c3ccc(cc3)S(=O)(=O)N)[*:0]'
REACTION_SUZUKI_NAME = 'Suzuki'


SIMPLE_TOKENS = {t: i for i, t in
                 enumerate(['$', '^', '(', ')', '1', '2', '3', '=', 'C', 'F', 'N', 'O', 'S', 'c', 'n'])}

REP_LIKELIHOOD = np.array(
    [15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 15.0, 10.0, 10.0, 10.0,
     10.0, 10.0, 10.0, 10.0, 10.0, 10.0, 10.0], dtype=np.float32)

LIKELIHOODLIST = np.array(
    [20.0, 20.0, 19.0, 19.0, 18.0, 18.0, 20.0, 21.0, 21.0, 20.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 20.0, 21.0,
     22.0, 23.0, 24.0, 25.0, 26.0, 27.0, 20.0, 17.0, 16.0, 15.0, 14.0, 13.0, 12.0, 20.0, 21.0, 22.0, 23.0, 24.0,
     25.0, 26.0, 27.0, 20.0], dtype=np.float32)

INVALID_SMILES_LIST = [INVALID] * 25
REP_SMILES_LIST = [ASPIRIN] * 15 + [CELECOXIB] * 10
