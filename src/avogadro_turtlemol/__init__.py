"""Avogadro plugin for filling/packing molecular structures using TurtleMol."""

import argparse
import json
import sys


def main():
    # Avogadro calls the plugin as:
    #   avogadro-turtlemol <identifier> [--lang <locale>] [--debug]
    # with the user options JSON on stdin.
    parser = argparse.ArgumentParser()
    parser.add_argument("feature")
    parser.add_argument("--lang", nargs="?", default="en")
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()

    avo_input = json.load(sys.stdin)
    output = None

    match args.feature:
        case "fill-box":
            from .fill_box import run
            output = run(avo_input)
        case "fill-sphere":
            from .fill_sphere import run
            output = run(avo_input)
        case "fill-mesh":
            from .fill_mesh import run
            output = run(avo_input)
        case "density-box":
            from .density_box import run
            output = run(avo_input)
        case "density-sphere":
            from .density_sphere import run
            output = run(avo_input)
        case "density-mesh":
            from .density_mesh import run
            output = run(avo_input)
        case "definite-box":
            from .definite_box import run
            output = run(avo_input)
        case "definite-sphere":
            from .definite_sphere import run
            output = run(avo_input)
        case "definite-mesh":
            from .definite_mesh import run
            output = run(avo_input)

    if output is not None:
        print(json.dumps(output))
