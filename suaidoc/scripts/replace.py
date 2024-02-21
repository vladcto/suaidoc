import pdfkit
import frontmatter
from datetime import datetime

def convert_markdown_to_pdf(markdown_file_path, output_pdf_path, template_path):
    with open(markdown_file_path, mode='r', encoding='utf-8') as md_file:
        md = md_file.read()
    meta_data = frontmatter.loads(md).metadata
    
    if (meta_data.get('year')):
        year = str(meta_data.get('year', ''))
    else:
        year = str(datetime.now().year)
    data = {
        'department': str(meta_data.get('department', '')),
        'teacher': str(meta_data.get('teacher', '')),
        'teacher_title': str(meta_data.get('teacher_title', '')),
        'theme': str(meta_data.get('theme', '')),
        'variant': str(meta_data.get('variant', '')),
        'discipline': str(meta_data.get('discipline', '')),
        'group': str(meta_data.get('group', '')),
        'student': str(meta_data.get('student', '')),
        'number': str(meta_data.get('number', '')),
        'year': year
    }

    with open(template_path, 'r', encoding='utf-8') as file:
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

    pdfkit.from_string(html_content, output_pdf_path, options=options)