all: 

data:

	mkdir -p data


PenguinData: data/

	!curl -O "https://raw.githubusercontent.com/allisonhorst/palmerpenguins/master/inst/extdata/penguins.csv"

Readit_all: 

	python -B readit_all.py

Process:

	python -B process.py

PenguinScatter:

	python _B PenguinScatter.py
