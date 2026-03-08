"""Fill a mesh shape with the current molecule at a target density."""

import TurtleMol

from ._common import base_structure, format_xyz, make_params, parse_xyz


def run(avo_input):
    options = avo_input.get('options', {})
    xyz_input = avo_input.get('xyz', '')

    iparams = make_params({
        'shape': 'mesh',
        'tol': options.get('tolerance', 1.0),
        'randomizeOrient': options.get('randomize', False),
        'structureFile': xyz_input,
        'baseStrucFile': options.get('og_struc', ''),
        'randFill': options.get('placement', False),
        'mesh': options.get('mesh', ''),
        'meshScale': options.get('mesh_scale', 1.0),
        'density': options.get('density', 1.0),
    })

    struc = parse_xyz(xyz_input)
    baseStruc = base_structure(iparams['baseStrucFile'])
    outStruc, strucType = TurtleMol.drawMolMesh(struc, baseStruc, iparams)

    return {
        'append': False,
        'moleculeFormat': 'xyz',
        'xyz': format_xyz(outStruc, strucType, xyz_input),
    }
