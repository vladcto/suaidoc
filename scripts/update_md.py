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


def update_markdown_file(markdown_path, output_file_path):
    markdown_directory = os.path.dirname(os.path.abspath(markdown_path))
    with open(markdown_path, 'r', encoding='utf-8') as file:
        md = file.read()
    md = replace_relative_image_paths(md, markdown_directory)
    md = replace_center_titles(md)
    with open(output_file_path, mode='w+', encoding='utf-8') as output_file:
        output_file.write(md)
