
all: data PenguinData Readit_all Process PenguinScatter

.PHONY: data
data:

	mkdir -p data

PenguinData: data/

	curl -O data/penguins.csv "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"

Readit_all: 

	python -B readit_all.py

Process:

	python -B process.py

PenguinScatter:

	python -B PenguinScatter.py
