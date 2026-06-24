import argparse
import cowsay

animal_names = cowsay.char_names

parser = argparse.ArgumentParser(prog="cowsay",
                                 description="Make animals say things")
                                 
parser.add_argument("message",
                    nargs="+",
                    help="The message to say.")

parser.add_argument("--animal",
                    "-a",
                    default="cow",
                    choices=animal_names,
                    help="Animal to use for the speech bubble.")

args = parser.parse_args()

if args.animal not in animal_names:
    parser.error("The specified animal is not found in the cowsay animal list.")

animal_function = getattr(cowsay, args.animal)
user_input = " ".join(args.message)
animal_function(user_input)
