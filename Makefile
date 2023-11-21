.PHONY: book
book:
	jupyter-book build book/

.PHONY: clean
clean:
	rm -rf book/_build
