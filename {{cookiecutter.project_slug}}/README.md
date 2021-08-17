# {{ cookiecutter.project_name }}
![PyPI](https://img.shields.io/pypi/v/{{ cookiecutter.project_slug }}?style=flat-square)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/{{ cookiecutter.project_slug}}?style=flat-square)
![PyPI - License](https://img.shields.io/pypi/l/{{ cookiecutter.project_slug }}?style=flat-square)
---

**Documentation**: [https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug
 }}](https://{{ cookiecutter.github_username }}.github.io/{{ cookiecutter.project_slug
 }})

**Source Code**: [https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}](https
://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }})

**PyPI**: [https://pypi.org/project/{{ cookiecutter.project_slug }}/](https://pypi.org/project/{{ cookiecutter
.project_slug }}/)

---

{{ cookiecutter.project_short_description }}

## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```

## Development
* Clone this repository
* Create a virtual environment and install the dependencies

```sh
poetry install
```

* Activate the virtual environment

```sh
poetry shell
```

### Testing

```sh
pytest
```

### Documentation
The documentation is automatically generated from the content of the [docs directory](./docs) and from the docstrings
 of the public signatures of the source code. The documentation is updated and published as a [Github project page
 ](https://pages.github.com/) automatically as part each release.

### Releasing
A PyPI release and documentation update is initiated by creating a [release in GitHub](https://docs.github.com/en/github/administering-a-repository/releasing-projects-on-github/about-releases).

The project uses [semantic versioning](https://semver.org/). Use `v` in front of the major version number, for
 example: `v2.1.3`.


### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before a commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```

Or if you want e.g. want to run all checks manually for all files:
```sh
pre-commit run --all-files
```
