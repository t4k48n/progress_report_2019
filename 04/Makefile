main.pdf: main.tex imcreport.sty $(filter-out main.pdf,$(wildcard *.pdf))
	lualatex -halt-on-error -interaction=nonstopmode main.tex
	lualatex -halt-on-error -interaction=nonstopmode main.tex
	lualatex -halt-on-error -interaction=nonstopmode main.tex

clean:
	rm -f main.pdf main.log main.aux

.PHONY: clean
