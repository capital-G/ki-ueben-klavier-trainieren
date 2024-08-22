.PHONY: book
book:
	PYTHONPATH="./book/chapters" jupyter-book build book/

pdf:
	PYTHONPATH="./book/chapters" jupyter-book build --builder pdflatex book/

.PHONY: clean
clean:
	rm -rf book/_build
