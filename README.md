# Wolt Python Package Cookiecutter
Cookiecutter for rapidly developing new open source Python packages.

Features:
* CI (GHA)
* Publishing to PyPI on GitHub releases (GHA)
* Poetry
* Pre-commit with all the good stuff
* Proper configs for linters
* src project structure (makes sure the tests are ran against installed package)
* Testing against multiple Python versions


## Usage
Make sure you have [`cruft`](https://github.com/cruft/cruft#installation) installed. Alternatively, you can use
 [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/installation.html) if you are not interested in
  getting updates to the project "boilerplate" in the future.

Create a new project:
```
cruft create https://github.com/creditornot/wolt-python-package-cookiecutter
```
The CLI interface will ask some basic questions, such the name of the project, and then generate all the goodies
 automatically.

After that you can make it a proper git repo:
```
cd <your-project-slug>
git init
git add .
git commit -m "Initial project structure from Wolt Python Package cookiecutter"
```

We update this cookiecutter template regularly to keep it up-to-date with the best practices of the Python world. You
 can get the updates into your project with:
```
cruft update
```

# TODOs:
* CI will require setting some secrets (e.g. PyPI token)
