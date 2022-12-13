
all: data  Readit_all Process Penguins

.PHONY: data
data:

	mkdir -p data

Readit_all: 
	
	curl -o data/penguins.csv "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"
	python -B readit_all.py

Process:

	python -B process.py

Penguins:

	python -B penguins.py
