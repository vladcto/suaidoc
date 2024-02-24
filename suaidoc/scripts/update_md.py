from importlib.resources import files
import re

import suaidoc.templates


def setup_images_size(md_content):
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


def latex_equation(content, numerate=True):
    equation = 'equation' if numerate else "equation*"
    return (f"\\begin{{{equation}}}\\begin{{gathered}}"
            f"{content}\n"
            f"\\end{{gathered}}\\end{{{equation}}}")


def wrap_equation_with_label(md_content):
    pattern = r"Equation: ([^\n]*?)\n\n\$\$([\s\S]*?)\$\$"

    def replacement(match):
        label = match.group(1)
        equation = match.group(2)
        return latex_equation(content=equation+f"\\label{{eq:{label}}}")

    return re.sub(pattern, replacement, md_content)


def wrap_simplify_equation(md_content):
    pattern = r"Simplify\n\n\$\$([\s\S]*?)\$\$"

    def replacement(match):
        return latex_equation(content=match.group(1), numerate=False)

    return re.sub(pattern, replacement, md_content)


def wrap_remain_equations(md_content):
    pattern = r'\$\$(.*?)\$\$'

    def replacement(match):
        return latex_equation(content=match.group(1))

    return re.sub(pattern, replacement, md_content, flags=re.DOTALL)


def add_intro_page_path(md_content, pdf_template_path):
    return md_content.replace('---', f'---\nsuaidocintropath: \detokenize{{{pdf_template_path}}}', 1)

def add_csl_metadata(md_content):
    gost_csl = files(suaidoc.templates).joinpath('gost2008.csl');
    return md_content.replace('---', f'---\ncsl: {gost_csl}', 1)


def update_markdown_file(markdown_path, output_file_path, pdf_template_path):
    with open(markdown_path, 'r', encoding='utf-8') as file:
        md = file.read()
    md = setup_images_size(md)
    md = replace_center_titles(md)

    # math
    md = wrap_cyrillic_in_mathit(md)
    md = wrap_equation_with_label(md)
    md = wrap_simplify_equation(md)
    md = wrap_remain_equations(md)

    md = add_intro_page_path(md, pdf_template_path)
    md = add_csl_metadata(md)
    
    with open(output_file_path, mode='w+', encoding='utf-8') as output_file:
        output_file.write(md)
