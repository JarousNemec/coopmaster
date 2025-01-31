# Installation 

## Ide 
InteliJ Ide

## TeX Live
https://community.chocolatey.org/packages/texlive
choco install texlive


tlmgr update --self --all

pdflatex -file-line-error -interaction=nonstopmode -synctex=1 -output-format=pdf -output-directory=C:/Users/admin/PycharmProjects/coopmaster/out thesis.tex
