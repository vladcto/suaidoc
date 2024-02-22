#!/usr/bin/python
import os
import shutil
import click as click
import subprocess
from suaidoc.scripts.update_md import update_markdown_file
from suaidoc.scripts.replace import convert_markdown_to_pdf
from importlib.resources import files
import tempfile

import suaidoc.templates


@click.group()
def cli():
    """
    Утилита для создания отчетов по работам в ГУАП.
    """
    pass


@cli.command()
@click.argument('md_file', type=click.Path(exists=True))
@click.option('-o', '--output', default=None, help="Имя выходного файла")
@click.option('-d', '--debug', is_flag=True, help="Включить конвертирование .md в .tex")
def create(md_file, output, debug):
    """
    Создать PDF-отчет из MD_FILE.
    """
    if (debug):
        if (output is not None):
            click.echo("--output are ignored with the --debug flag.")
        output = os.path.splitext(md_file)[0] + '_debug.tex'

    if (output is None):
        output = os.path.splitext(md_file)[0] + '.pdf'

    tmp_dir = os.path.normpath(tempfile.mkdtemp()).replace("\\", "/")
    html_template = files(suaidoc.templates).joinpath('template.html')
    tex_template = files(suaidoc.templates).joinpath('template.tex')
    os.makedirs(tmp_dir, exist_ok=True)

    try:
        tmp_md_path = f'{tmp_dir}/tmp.md'
        tmp_pdf_path = f'{tmp_dir}/intro.pdf'
        click.echo(tmp_pdf_path)

        update_markdown_file(md_file, tmp_md_path, tmp_pdf_path)
        convert_markdown_to_pdf(
            tmp_md_path, tmp_pdf_path, html_template)

        pandoc_convert = ["pandoc", tmp_md_path, "--citeproc", "-so", output]
        pandoc_template = [
            f'--template={tex_template}', '--pdf-engine=xelatex']
        pandoc_listings = ['--listings',
                           '--pdf-engine-opt=-shell-escape']

        subprocess.run([*pandoc_convert, *pandoc_template, *pandoc_listings])
        click.echo('File created in ' + os.path.abspath(output))
    finally:
        shutil.rmtree(tmp_dir)


@cli.command()
def template():
    """
    Создать Markdown-шаблон отчета в текущей директории.
    """
    file = open(os.getcwd() + '/report.md', "x", encoding='utf-8')
    file.write(
        '''
---
departament: 12
teacher: Амог У. С.
teacher_title: Гений науки, к.г.н.
discipline: Изучение влияния мандаринов
variant: 3
number: 12
subject: Изучение влияния мандаринов на человека
group: 4128
student: Анонимный Н. Н.
---
        '''
    )
    file.close()


if __name__ == '__main__':
    cli()
