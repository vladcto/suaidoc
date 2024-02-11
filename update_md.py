import argparse
import os
import re

parser = argparse.ArgumentParser()
parser.add_argument('markdown_path', type=str,
                    help='Path to the markdown file')

args = parser.parse_args()

file_path = args.markdown_path

markdown_directory = os.path.dirname(os.path.abspath(file_path))

with open(file_path, 'r', encoding='utf-8') as file:
    md = file.read()

def replace_relative_image_paths(md_content, markdown_directory):
    matches = re.finditer(r'!\["([^"]+)"\]\(([^)]+)\)', md_content)
    
    for match in matches:
        image_name = match.group(1)
        relative_path = match.group(2)
        
        # Полный путь к оригинальному изображению
        original_image_path = os.path.join(markdown_directory, relative_path)
        
        # Заменить путь в Markdown файле
        md_content = md_content.replace('!["' + image_name + '"](' + relative_path + ')',
                                        '\\image{' + original_image_path + '}{' + image_name + '}')
    
    return md_content

md = replace_relative_image_paths(md, markdown_directory)

output_file_path = os.path.join(markdown_directory, '_suaidoc_tmp.md')

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(md)
