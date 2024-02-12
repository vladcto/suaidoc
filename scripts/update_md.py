import argparse
import os
import re


def replace_relative_image_paths(md_content, markdown_directory):
    # re !["<image_name>"](<relative_path>)<size>
    matches = re.finditer(r'!\[(.*?)\]\((.*?)\)(?:<(.*?)>)?', md_content)

    for match in matches:
        image_name = match.group(1)
        relative_path = match.group(2)

        original_image_path = os.path.join(markdown_directory, relative_path)

        size_map = {
            None: 0.95,
            "t": 0.25,
            "s": 0.35,
            "m": 0.55,
            "l": 0.85
        }
        size = str(size_map[match.group(3)])
        md_content = md_content.replace(match.group(0),
                                        '\\image{' + original_image_path + '}{' + image_name + '}{'+size+'}')

    return md_content


def replace_center_titles(md_content):
    # re # <name> <suaidoc-center>
    matches = re.finditer(r'# ([^\n]+) <suaidoc-center>', md_content)

    for match in matches:
        full_match = match.group(0)
        title_name = match.group(1)
        md_content = md_content.replace(
            full_match, f'\centertitle{{{title_name}}}')

    return md_content


parser = argparse.ArgumentParser()
parser.add_argument('markdown_path', type=str,
                    help='Path to the markdown file')
parser.add_argument('updated_directory', type=str,
                    help='Path to the markdown file')

args = parser.parse_args()

file_path = args.markdown_path

markdown_directory = os.path.dirname(os.path.abspath(file_path))

with open(file_path, 'r', encoding='utf-8') as file:
    md = file.read()

md = replace_relative_image_paths(md, markdown_directory)
md = replace_center_titles(md)

output_file_path = os.path.join(args.updated_directory, '_updated_md.md')

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(md)
