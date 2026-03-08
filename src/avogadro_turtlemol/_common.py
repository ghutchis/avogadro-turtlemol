"""Shared helpers for TurtleMol Avogadro plugin."""

import io
import warnings

warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd
import TurtleMol


def make_params(iparams):
    """Merge TurtleMol default params into iparams, keeping provided values."""
    dparams = TurtleMol.defaultParams()
    for name in dparams:
        if name not in iparams:
            iparams[name] = dparams[name]
    return iparams


def parse_xyz(xyz_str):
    """Parse an XYZ string into a DataFrame with columns Atom, X, Y, Z."""
    return pd.read_csv(
        io.StringIO(xyz_str),
        sep=r'\s+',
        skiprows=2,
        names=["Atom", "X", "Y", "Z"],
    )


def base_structure(path):
    """Load optional base structure file; return None if path is empty."""
    if path:
        return TurtleMol.readStrucFile(path)
    return None


def format_xyz(outStruc, strucType, fallback_xyz):
    """Convert TurtleMol output to an XYZ string."""
    columns = ['Atom', 'X', 'Y', 'Z']
    df = pd.DataFrame(columns=columns)

    if strucType == "molecule":
        for mol in outStruc:
            for atom in mol:
                df = pd.concat(
                    [df, pd.DataFrame([atom], columns=columns)],
                    ignore_index=True,
                )
    else:
        df = pd.DataFrame(outStruc, columns=columns)

    if len(df) == 0:
        return fallback_xyz

    lines = f'{len(df)}\n\n'
    for _, row in df.iterrows():
        lines += f"{row['Atom']:<2}  {row['X']:> 10.5f}   {row['Y']:> 8.5f}   {row['Z']:> 8.5f}\n"
    return lines
