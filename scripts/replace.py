import argparse
import pdfkit
import markdown_it
import frontmatter
from datetime import datetime

parser = argparse.ArgumentParser(description='Process some files.')
parser.add_argument('markdown_path', type=str,
                    help='Path to the markdown file')
parser.add_argument('output_pdf_path', type=str,
                    help='Path to the output PDF file')

args = parser.parse_args()

file_path = args.markdown_path

with open(file_path, 'r', encoding='utf-8') as file:
    md = file.read()

md_parser = markdown_it.MarkdownIt()
parsed_md = md_parser.parse(md)

meta_data = frontmatter.loads(md).metadata

if (meta_data.get('year')):
    year = str(meta_data.get('year', ''))
else:
    year = str(datetime.now().year)
data = {
    'department': str(meta_data.get('departament', '')),
    'teacher': str(meta_data.get('teacher', '')),
    'teacher_title': str(meta_data.get('teacher_title', '')),
    'discipline': str(meta_data.get('discipline', '')),
    'variant': str(meta_data.get('variant', '')),
    'subject': str(meta_data.get('subject', '')),
    'group': str(meta_data.get('group', '')),
    'student': str(meta_data.get('student', '')),
    'number': str(meta_data.get('number', '')),
    'year': year
}

with open('template/template.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

for placeholder, value in data.items():
    html_content = html_content.replace(f'$${placeholder}$$', str(value))

options = {
    'page-size': 'A4',
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'zoom': 1.3,
}

pdfkit.from_string(html_content, args.output_pdf_path, options=options)
