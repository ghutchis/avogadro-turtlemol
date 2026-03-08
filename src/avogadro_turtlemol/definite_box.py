"""Place a definite number of molecules in a box."""

import TurtleMol

from ._common import base_structure, format_xyz, make_params, parse_xyz


def run(avo_input):
    options = avo_input.get('options', {})
    xyz_input = avo_input.get('xyz', '')

    iparams = make_params({
        'shape': 'box',
        'tol': options.get('tolerance', 1.0),
        'Xlen': options.get('length', 1.0),
        'Ylen': options.get('width', 1.0),
        'Zlen': options.get('height', 1.0),
        'numMolecules': options.get('num_mol', 1),
        'randomizeOrient': options.get('randomize', False),
        'structureFile': xyz_input,
        'baseStrucFile': options.get('og_struc', ''),
        'randFill': options.get('placement', False),
    })

    struc = parse_xyz(xyz_input)
    baseStruc = base_structure(iparams['baseStrucFile'])
    outStruc, strucType = TurtleMol.drawMolBox(struc, baseStruc, iparams)

    return {
        'append': False,
        'moleculeFormat': 'xyz',
        'xyz': format_xyz(outStruc, strucType, xyz_input),
    }
