.PHONY: clean

TARGET := main.pdf

FIGURES := $(filter-out $(TARGET),$(wildcard *.pdf))

$(TARGET): main.tex imcreport.sty $(FIGURES)
	sed -i.bak -e 's/、/，/g' -e 's/。/．/g' $<
	lualatex -halt-on-error -interaction=nonstopmode $<
	lualatex -halt-on-error -interaction=nonstopmode $<
	lualatex -halt-on-error -interaction=nonstopmode $<

clean:
	rm -f main.pdf main.log main.aux *.tex.bak
