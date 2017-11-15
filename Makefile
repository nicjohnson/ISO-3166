clean:
	rm -rf data

build: clean
	mkdir -p data/subdivisions/by_country data/countries
	python fmt.py
