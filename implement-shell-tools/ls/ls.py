import argparse
import os

parser = argparse.ArgumentParser(prog="ls",
                                 description="simple ls clone")

parser.add_argument("-1",
                    dest="one_per_line",
                    action="store_true",
                    help="list one file per line")

parser.add_argument("-a",
                    action="store_true",
                    help="show hidden files")

parser.add_argument("filepath",
                    nargs="?",
                    default=".")

args = parser.parse_args()
