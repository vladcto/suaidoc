#!/usr/bin/python
import os
import shutil
import sys
import click as click
import subprocess
from scripts.update_md import update_markdown_file
from scripts.replace import convert_markdown_to_pdf


@click.group()
def suaidoc():
    """
    Утилита для создания отчетов по работам в ГУАП.
    """
    pass


@suaidoc.command()
@click.option('-o', '--output', default=None, help="Имя выходного файла")
@click.argument('md_file', type=click.Path(exists=True))
def create(md_file, output):
    if (output is None):
        output = os.path.splitext(md_file)[0] + '.pdf'
    # Next we change the working directory so we need absolute path
    output = os.path.abspath(output)

    script_dir = os.path.dirname(os.path.realpath(sys.argv[0]))
    tmp_dir = os.path.join(script_dir, 'tmp')
    os.makedirs(tmp_dir, exist_ok=True)

    try:
        tmp_md_path = os.path.join(tmp_dir, 'tmp.md')
        tmp_pdf_path = os.path.join(tmp_dir, 'intro.pdf')

        with open(tmp_md_path, "w+", encoding='utf-8') as tmp_md_file:
            update_markdown_file(md_file, tmp_md_file)
            html_template = os.path.join(
                script_dir, 'templates', 'template.html')
            convert_markdown_to_pdf(
                tmp_md_path, tmp_pdf_path, html_template)

            # Change working directory so LaTeX can find the pdf page
            os.chdir(script_dir)
            tex_template = os.path.join('templates', 'template.tex')
            pandoc_convert = ['pandoc', tmp_md_path, '-o', output]
            pandoc_template = ['--template=' +
                               tex_template, '--pdf-engine=xelatex']
            pandoc_listings = ['--listings',
                               '--pdf-engine-opt=-shell-escape']
            subprocess.run(
                [*pandoc_convert, *pandoc_template, *pandoc_listings])
            click.echo('PDF created in ' + output)
    finally:
        shutil.rmtree(tmp_dir)


@suaidoc.command()
@click.option('-t',
              '--template',
              default='lab',
              help="Создать md-шаблон в текущей директории",
              type=click.Choice(['lab']),
              show_default=True)
def template():
    click.echo('Dropped the database')


def check_suaidoc_updates() -> bool:
    try:
        subprocess.check_output(
            ['git', 'diff', '--exit-code', 'origin/main'])
        return False
    except subprocess.CalledProcessError:
        return True


@suaidoc.command()
def update():
    os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
    if not shutil.which('git'):
        click.echo('Git не установлен.')
        return

    try:
        subprocess.check_output(['git', 'status'])
    except subprocess.CalledProcessError:
        click.echo(
            'Это не Git-репозиторий. Для обновления нужно скачать новый архив.')
        return


    try:
        subprocess.check_output(['git', 'diff', '--exit-code'])
    except subprocess.CalledProcessError:
        click.echo(
            'В репозиторий внесены изменения. Если вы их не делали, то сделайте то-то')
        return

    if (check_suaidoc_updates()):
        click.echo(
            'Нет доступных обновлений suaidoc.')
        return

    try:
        subprocess.check_output(['git', 'fetch'])

        try:
            subprocess.check_output(
                ['git', 'diff', '--exit-code', 'origin'])
        except subprocess.CalledProcessError:
            print('Нет доступных обновлений suaidoc.')
            return

        print('Обновление suaidoc...')
        subprocess.check_output(['git', 'pull'])
        click.echo('suaidoc обновлен.')
    except subprocess.CalledProcessError:
        click.echo('Ошибка при обновлении suaidoc.')
        return

    last_update = subprocess.check_output(
        ['git', 'log', '-1', '--format=%cd']).decode('utf-8').strip()
    click.echo(f'Последнее обновление: {last_update}')


if __name__ == '__main__':
    suaidoc()
