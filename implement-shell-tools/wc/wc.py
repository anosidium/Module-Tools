import argparse

parser = argparse.ArgumentParser(prog="wc",
                                 description="simple wc clone")

parser.add_argument("-w",
                    "--words",
                    dest="words_count",
                    action="store_true",
                    help="print word count")

parser.add_argument("-l",
                    "--lines",
                    dest="lines_count",
                    action="store_true",
                    help="print line count")

parser.add_argument("-c",
                    "--bytes",
                    dest="byte_count",
                    action="store_true",
                    help="print byte count")

parser.add_argument("path")

args = parser.parse_args()
