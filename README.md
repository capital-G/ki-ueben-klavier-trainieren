# KI üben, Klavier traineren

This repository contains the source code for the course.
The website with the actual course is located at <https://ki-ueben.musikinformatik.net/>.

## Development

Assuming Python is installed on the system, it is advised to create a virtual environment via [venv](https://docs.python.org/3/library/venv.html) (e.g. `virtualenv venv`) to install all necessary dependencies via `pip install -r requirements-dev.txt`.

Afterwards, the notebooks can be worked in the browser via

```shell
venv/bin/jupyter lab
```

The book is written in a mix of [*myst*](https://myst-parser.readthedocs.io/en/latest/intro.html) and [*rst*](https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html).

To build the actual website use

```shell
make book
```

This repository uses [`pre-commit`](https://pre-commit.com/) to align commits.

## License

Code is licensed under AGPL-3.0.

Text and documentation is licensed under CC BY-NC-SA 4.0.
