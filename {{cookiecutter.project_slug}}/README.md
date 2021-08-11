# {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

## Installation

```sh
pip install {{ cookiecutter.project_slug }}
```

## Development
1. Clone this repository
2. Create a virtual environment and install the dependencies

   ```sh
   poetry install
   ```

3. Activate the virtual environment

   ```sh
   poetry shell
   ```

### Testing

```sh
pytest
```

### Pre-commit

Pre-commit hooks run all the auto-formatters (e.g. `black`, `isort`), linters (e.g. `mypy`, `flake8`), and other quality
 checks to make sure the changeset is in good shape before the commit/push happens.

You can install the hooks with (runs for each commit):

```sh
pre-commit install
```

Or if you want them to run only for each push:

```sh
pre-commit install -t pre-push
```
