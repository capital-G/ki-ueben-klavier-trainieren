.PHONY: book
book:
	PYTHONPATH="./book/chapters" jupyter-book build book/

.PHONY: clean
clean:
	rm -rf book/_build
