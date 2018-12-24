import CaboCha
import pydotplus
import subprocess

def make_analyzed_file(input_file_name: str, output_file_name: str) -> None:

    cabo = CaboCha.Parser()
    with open(input_file_name, encoding='utf-8') as input_file:
        with open(output_file_name, mode='w', encoding='utf-8') as output_file:
            for line in input_file:
                tree = cabo.parse(line.lstrip())
                output_file.write(tree.toString(CaboCha.FORMAT_LATTICE))

make_analyzed_file('neko.txt', 'noko.txt.cabocha')