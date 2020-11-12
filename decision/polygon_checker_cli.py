from argparse import ArgumentParser
from .helpers import read_from_file, process_polygons

# init parser for CLI
parser = ArgumentParser(description="Define are polygons equal")

# add arguments for CLI
parser.add_argument("-s", action="store", dest="polygons", type=str, help="get polygon`s coordinates separated by \\n")
parser.add_argument("-f", action="store", dest="file", type=str, help="get name of the text source file name")

# parse got arguments
args = parser.parse_args()

if args.polygons:
    input_text = args.polygons.split('\n')
    result = process_polygons(input_text)
elif args.file:
    input_text = read_from_file(args.file)
    result = process_polygons(input_text)
else:
    result = "No arguments in CLI"

# print finish result
print(result)
