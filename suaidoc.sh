#! bin/bash
mkdir $(dirname $0)/tmp
tmp=$(dirname $0)/tmp
python3 scripts/update_md.py $1 $tmp/
python3 scripts/replace.py $1 $tmp/_intro.pdf
pandoc $tmp/_updated_md.md -o $2 \
	--template=template.tex --pdf-engine=xelatex \
	--listings --pdf-engine-opt=-shell-escape
rm -r $tmp