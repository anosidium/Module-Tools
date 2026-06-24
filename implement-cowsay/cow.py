import argparse
import cowsay

parser = argparse.ArgumentParser(prog="cow.py",
                                 description="Print a message using a cowsay animal")
                                 
parser.add_argument("message",
                    nargs="+")

parser.add_argument("-a",
                    "--animal",
                    default="cow",
                    help="Animal to use for the speech bubble.")

args = parser.parse_args()

animal_names = cowsay.char_names

if args.animal not in animal_names:
    parser.error("The specified animal is not found in the cowsay animal list.")

animal_function = getattr(cowsay, args.animal)
user_input = " ".join(args.message)
animal_function(user_input)
