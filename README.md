# Wolt Python Package Cookiecutter

Cookiecutter for rapidly developing new open source Python packages. Best practices with all the modern bells
and whistles included.

## Features:

**Automatic updates to the projects generated from this cookiecutter**
* Powered by [cruft](https://cruft.github.io/cruft/)
* Keep your project up-to-date with best practices

**Continuous integration**
* Powered by [Github Actions](https://github.com/features/actions)
* Testing against multiple different versions

**Documentation**
* Automatically published as [GitHub Pages](https://pages.github.com/)
* Powered by [mkdocs-material](https://github.com/squidfunk/mkdocs-material)
* Auto-generated API documentation from docstrings via [mkdocstrings](https://github.com/mkdocstrings/mkdocstrings)
* See the extensive list of [MkDocs plugins](https://github.com/mkdocs/mkdocs/wiki/MkDocs-Plugins) which can help you
 to tune the documentation to fit your project's needs

**Automated releases**
* Publishing to [PyPI](https://pypi.org/) when a release is made in GitHub

**Changelog management**
* TODO

**Bells and whistles**
* [Poetry](https://python-poetry.org/docs/) for managing dependencies and packaging
* [pre-commit](https://pre-commit.com/) for running all the goodies listed below
* [mypy](https://flake8.pycqa.org/en/latest/) for static type checking
* [flake8](https://flake8.pycqa.org/en/latest/) (with multiple plugins) for linting (e.g. style and complexity checks)
* [black](https://black.readthedocs.io/en/stable/) for auto-formatting the code
* [isort](https://pycqa.github.io/isort/) for auto-sorting imports
* [autoflake](https://github.com/myint/autoflake) for auto-removing unused imports

**Automation**
* Updates to the best practices (via GHA workflow which runs `cruft update` and creates a PR)
* Dependency updates (via GHA workflow which creates a PR)

## Usage

Make sure you have [`cruft`](https://github.com/cruft/cruft#installation) installed. Alternatively, you can use
 [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you are not interested in
  getting updates to the project "boilerplate" in the future.

Create a new project:

```sh
cruft create https://github.com/creditornot/wolt-python-package-cookiecutter
```

The CLI interface will ask some basic questions, such the name of the project, and then generate all the goodies
 automatically.

After that you can make it a proper git repo:

```sh
cd <your-project-slug>
git init
git add .
git commit -m "Initial project structure from Wolt Python Package cookiecutter"
```

We update this cookiecutter template regularly to keep it up-to-date with the best practices of the Python world. You
 can get the updates into your project with:

```sh
cruft update
```

### Configure secrets
`PYPI_TOKEN`

Required for publishing the package to [PyPI](https://pypi.org/). You can generate a token by logging into PyPI and
 navigating to _Add API token_ in your [account settings](https://pypi.org/manage/account/).


`AUTO_UPDATE_GITHUB_TOKEN`

This cookiecutter template comes with an auto update feature if the project was created using cruft.
A GitHub action automatically checks for updates and creates a pull request.

Generate [personal access token](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
and use it as the value for `AUTO_UPDATE_GITHUB_TOKEN` secret. When creating the access token, the following
 permissions have to be granted

* repo
* workflow


### After the first release
The first release will create `gh-pages` branch which will contain the static files for the documentation. Enable GitHub
 Pages in the _Pages_ section of the repository settings.
