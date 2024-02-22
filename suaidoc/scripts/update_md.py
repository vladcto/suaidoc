from os import path
import re
import sys


def replace_relative_image_paths(md_content, markdown_directory):
    # re !["<image_name>"](<relative_path>)<size>
    matches = re.finditer(r'!\[(.*?)\]\((.*?)\)(?:<(.*?)>)?', md_content)

    for match in matches:
        image_name = match.group(1)
        relative_path = match.group(2)

        size_map = {
            None: 0.95,
            "t": 0.25,
            "sm": 0.35,
            "m": 0.55,
            "l": 0.85
        }
        size = str(size_map[match.group(3)])
        md_content = md_content.replace(match.group(0),
                                        f'\\image{{{relative_path}}}{{{image_name}}}{{{size}}}')

    return md_content


def replace_center_titles(md_content):
    # re #<name><suaidoc-center>
    matches = re.finditer(r'# ([^\n]+) <suaidoc-center>', md_content)

    for match in matches:
        full_match = match.group(0)
        title_name = match.group(1)
        md_content = md_content.replace(
            full_match, f'\centertitle{{{title_name}}}')

    return md_content


def wrap_cyrillic_in_mathit(md_content):
    # re $$<cyrillic>$$ or $<cyrillic>$
    latex_formula_pattern = r"\$\$.*?\$\$|\$.*?\$"
    cyrillic_pattern = re.compile(r"([а-яА-ЯёЁ]+)")

    def replace_cyrillic_in_formula(formula):
        return cyrillic_pattern.sub(r"\\mathit{\1}", formula.group())

    return re.sub(latex_formula_pattern, replace_cyrillic_in_formula, md_content, flags=re.DOTALL)


def wrap_equation_with_label(md_content):
    # re
    # Equation: text
    # 
    # $$<equation>$$
    pattern = r"Equation: ([^\n]*?)\n\n\$\$([\s\S]*?)\$\$"

    def replacement(match):
        print(match)
        label = match.group(1)
        equation = match.group(2)
        return f"\\begin{{equation}}\\begin{{gathered}}{equation}\\label{{eq:{label}}}\n\\end{{gathered}}\\end{{equation}}"

    return re.sub(pattern, replacement, md_content)



def wrap_remain_equations(md_content):
    pattern = r'\$\$(.*?)\$\$'
    replacement = r'\\begin{equation}\n\\begin{gathered}\1\\end{gathered}\n\\end{equation}'
    return re.sub(pattern, replacement, md_content, flags=re.DOTALL)


def add_intro_page_path(md_content, pdf_template_path):
    return md_content.replace('---', f'---\nsuaidocintropath: \detokenize{{{pdf_template_path}}}', 1)


def update_markdown_file(markdown_path, output_file_path, pdf_template_path):
    markdown_directory = path.dirname(path.abspath(markdown_path))
    with open(markdown_path, 'r', encoding='utf-8') as file:
        md = file.read()
    md = replace_relative_image_paths(md, markdown_directory)
    md = replace_center_titles(md)
    md = wrap_cyrillic_in_mathit(md)
    md = wrap_equation_with_label(md)
    md = wrap_remain_equations(md)
    md = add_intro_page_path(md, pdf_template_path)
    with open(output_file_path, mode='w+', encoding='utf-8') as output_file:
        output_file.write(md)
