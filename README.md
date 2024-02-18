# SUAIDOC - docs for SUAI

СLI утилита для генерации отчетов из Markdown по ГОСТ-7.32.

Просто вызовите в терминале `suaidoc create <md_file_path>` и получите отчет в PDF. Магия!

## Установка

Утилита является **Python** пакетом, поэтому для установки утилиты достаточно в терминале написать:

```bash
pip install suaidoc --upgrade
```

или

```bash
pip3 install suaidoc --upgrade
```

Теперь нужно установить утилиты, требуемые для работы:

### macOS

Можно установить с помощью [brew](https://brew.sh). Для установки вставьте в терминал:

```zsh
brew install pandoc
brew install --cask wkhtmltopdf
brew install --cask mactex-no-gui
```

Установка `mactex-no-gui` может занять много времени. Если хочется побыстрее, то можно установить [MacTeX](https://tug.org/mactex/) вручную. GUI приложения затем можно спокойно удалить.

### Windows

Можно установить с помощью [chocolatey](https://chocolatey.org). Для установки вставьте в терминал от имени администратора:

```powershell
choco install pandoc
choco install wkhtmltopdf
choco install miktex.install
```

### Установка вручную

Если установка с помощью пакет-менеджеров выше не удалась, то требуется установить отсутствующие утилиты вручную.

Если вы не пробовали установку с помощью пакет-менеджеров, то сначала попробуйте ее. Она легче, быстрее и менее муторная.

#### Pandoc

Pandoc используется для генерации Markdown в PDF.

1) Перейдите на [сайт Pandoc](https://pandoc.org/installing.html) и выберите нужный установщик.
2) **Убедитесь**, что выбрана настройка для добавления pandoc в `PATH`!
3) После установки проверьте, что *pandoc* можно вызвать из терминала.

#### wkhtmltopdf

Для генерации титульной страницы из HTML в PDF.

1) Перейдите на [сайт wkhtmltopdf](https://wkhtmltopdf.org) и выберите нужный установщик.
2) Запомните расположение, куда был установлен *wkhtmltopdf*.
3) Скорее всего, после установки *wkhtmltopdf* не будет добавлен в `PATH`. Поэтому добавьте путь из предыдущего шага к `PATH`.
4) Проверьте, что *wkhtmltopdf* можно вызвать из терминала.

#### LaTeX

*MiKTeX* используется из-за удобства и нужных встроенных пакетов.

1) Перейдите на [сайт MikTex](https://miktex.org/download) и выберите нужный установщик.
2) Следуйте шагам установки, **обязательно** выбрав опцию для автоматического обновления.
3) Запустите приложение *MikTex console* от администратора и на главной странице проверьте автоматические обновления. Установите обновление, если это возможно.

## Примеры

Примеры представлены в папке [example](/example/).

Также есть и особенные примеры:
- [Пример форматирования](/example/main/).
- [Расширение Markdown WIP](/example/main/).

## ГОСТ 7.32

Это утилита не стремится строго следовать ГОСТ 7.32. Прежде всего утилита предназначена для **облегчения** написания отчетов *студентов*. Поэтому часть стандартов, которая усложнит написание, использование или структурирование - незначительно изменены. Для более комплексных научных работ, стоит выбрать другие решения, например [latex-g7-32](https://github.com/latex-g7-32/latex-g7-32).

Для простых лабораторных, практических работ suaidoc является идеальным решением.

### Список нарушений ГОСТ

WIP

## Команды

WIP

### --help

WIP

### create

WIP

### template

WIP