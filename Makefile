main: main.py crawler.py
	python $<
.PHONY: clean
clean:
	rm *.pyc
