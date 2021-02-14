from rdkit import Chem
from rdkit.Chem import Draw


def draw_molecule(smile):
    molecule = [Chem.MolFromSmiles(smile)]
    return Draw.MolsToGridImage(
        molecule,
        useSVG=True,
    )


def draw_molecules(smiles, names, per_row=2, size=(200, 250)):
    molecules = [Chem.MolFromSmiles(s) for s in smiles]
    return Draw.MolsToGridImage(
        molecules,
        legends=names,
        molsPerRow=per_row,
        useSVG=True,
        subImgSize=size,
    )
