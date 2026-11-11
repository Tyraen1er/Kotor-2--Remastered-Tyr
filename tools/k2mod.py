"""KotOR 2 Modding CLI Helper for workspace automation."""
import argparse
import sys
from pathlib import Path
from pykotor.common.misc import Game
from pykotor.extract.installation import Installation
from pykotor.resource.type import ResourceType
from pykotor.resource.formats.ncs import compile_nss, write_ncs, decompile_ncs, read_ncs
from pykotor.resource.formats.twoda import read_2da, write_2da
from k2balance import register_balance_subparsers

GAME_PATH = Path(r"C:\Program Files (x86)\Steam\steamapps\common\Knights of the Old Republic II")
ROOT_DIR = Path(__file__).resolve().parent.parent
REF_SCRIPTS = ROOT_DIR / "_reference" / "scripts"
REF_2DA = ROOT_DIR / "_reference" / "2da"


def cmd_compile(args):
    src = Path(args.source)
    out = Path(args.output) if args.output else src.with_suffix(".ncs")
    lookup = [src.parent, REF_SCRIPTS]
    ncs = compile_nss(src.read_text(encoding="latin1"), Game.K2, library_lookup=lookup)
    write_ncs(ncs, out)
    print(f"[OK] Compiled {src.name} -> {out} ({len(ncs.instructions)} instructions)")


def cmd_extract(args):
    inst = Installation(GAME_PATH)
    restype = ResourceType.from_extension(args.ext)
    res = inst.resource(args.resname, restype)
    if not res:
        print(f"[ERR] Resource {args.resname}.{args.ext} not found in installation.")
        sys.exit(1)
    out = Path(args.output) if args.output else Path(f"{args.resname}.{args.ext}")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(res.data)
    print(f"[OK] Extracted {args.resname}.{args.ext} -> {out} ({len(res.data)} bytes)")


def main():
    parser = argparse.ArgumentParser(description="KotOR 2 Modding Helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_comp = sub.add_parser("compile", help="Compile an NSS script to NCS for KotOR 2")
    p_comp.add_argument("source", help="Path to .nss file")
    p_comp.add_argument("-o", "--output", help="Output .ncs path")
    p_comp.set_defaults(func=cmd_compile)

    p_ext = sub.add_parser("extract", help="Extract a resource from KotOR 2 installation")
    p_ext.add_argument("resname", help="Resource name without extension")
    p_ext.add_argument("ext", help="Resource extension (e.g. uti, 2da, nss, ncs)")
    p_ext.add_argument("-o", "--output", help="Output file path")
    p_ext.set_defaults(func=cmd_extract)

    register_balance_subparsers(sub)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
