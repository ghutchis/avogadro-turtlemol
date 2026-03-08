"""Fill a sphere with copies of the current molecule."""

import TurtleMol

from ._common import base_structure, format_xyz, make_params, parse_xyz


def run(avo_input):
    options = avo_input.get('options', {})
    xyz_input = avo_input.get('xyz', '')

    iparams = make_params({
        'shape': 'sphere',
        'tol': options.get('tolerance', 1.0),
        'radius': options.get('radius', 1.0),
        'numMolecules': 'fill',
        'randomizeOrient': options.get('randomize', False),
        'structureFile': xyz_input,
        'baseStrucFile': options.get('og_struc', ''),
    })

    struc = parse_xyz(xyz_input)
    baseStruc = base_structure(iparams['baseStrucFile'])
    outStruc, strucType = TurtleMol.drawMolSphere(struc, baseStruc, iparams)

    return {
        'append': False,
        'moleculeFormat': 'xyz',
        'xyz': format_xyz(outStruc, strucType, xyz_input),
    }
