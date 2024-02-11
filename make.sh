#! bin/bash
pandoc example2.md -o example2.pdf \
	--template=template.tex --pdf-engine=xelatex \
	--listings --pdf-engine-opt=-shell-escape
