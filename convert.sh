#! bin/bash
python3 replace.py $1 intro.pdf
pandoc $1 -o $2 \
	--template=template.tex --pdf-engine=xelatex \
	--listings --pdf-engine-opt=-shell-escape
