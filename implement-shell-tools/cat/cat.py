import argparse

parser = argparse.ArgumentParser(prog="cat",
                                 description="simple cat clone")

parser.add_argument("-n",
                    "--number",
                    dest="number_all",
                    action="store_true",
                    help="number all output lines")

parser.add_argument("-b",
                    "--number-nonblank",
                    dest="number_nonblank",
                    action="store_true",
                    help="number non-empty output lines")

parser.add_argument("paths", nargs="+", help="file(s) to process")

args = parser.parse_args()
