import argparse

parser = argparse.ArgumentParser(prog="wc",
                                 description="simple wc clone")

parser.add_argument("-w",
                    "--words",
                    dest="show_words",
                    action="store_true",
                    help="print word count")

parser.add_argument("-l",
                    "--lines",
                    dest="show_lines",
                    action="store_true",
                    help="print line count")

parser.add_argument("-c",
                    "--bytes",
                    dest="show_bytes",
                    action="store_true",
                    help="print byte count")

parser.add_argument("path")

args = parser.parse_args()

if not args.show_lines and not args.show_words and not args.show_bytes:
    args.show_lines = True
    args.show_words = True
    args.show_bytes = True

with open(args.path, "rb") as file:
    content = file.read()

word_count = str(len(content.split()))
line_count = str(content.count(b"\n"))
byte_count = str(len(content))

outputs = []

if args.show_lines:
    outputs.append(line_count)

if args.show_words:
    outputs.append(word_count)

if args.show_bytes:
    outputs.append(byte_count)

outputs.append(args.path)

output = "\t".join(outputs)
print(output)
