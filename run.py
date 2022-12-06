from Libraries.Config.packages import *
import importlib
import argparse
import glob


def main():
    args = parse()
    run(args.phases)


################################################################################


def parse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--phase",
        metavar="phase_id",
        help="list of modules to run, in format 0, 1, ..., 99",
        action="extend",
        nargs="+",
        type=int,
        dest="phases",
    )
    args = parser.parse_args()
    return args


################################################################################


def run(phases):
    for phase in phases:
        filenames = glob.glob(f"Phases/{phase:02d}*")
        assert len(filenames) == 1, filenames
        filename = filenames[0]
        ##
        modulename = re.sub(r"/", ".", filename)
        modulename = re.sub(r"\.py", "", modulename)
        print("\n" * 4)
        print("=" * 100)
        print(f"Phase: {phase}, module: {modulename}")
        print("\n" * 2)
        ##
        new_module = importlib.import_module(modulename)
        function = new_module.main
        function()


################################################################################

main()
