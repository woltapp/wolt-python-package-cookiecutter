import pytest
import yaml
from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_DIR = str(Path(__file__).parent.parent)
CONTEXT_FILE = Path(__file__).parent / "context.yaml"

with open(CONTEXT_FILE) as file_handler:
    content = yaml.safe_load(file_handler)

EXAMPLE_CONTEXT = content['default_context']
PROJECT_NAME = EXAMPLE_CONTEXT["project_name"]


@pytest.fixture
def generated_project_path(tmp_path) -> Path:
    """
    :return: path to newly generated project
    """
    return Path(cookiecutter(
        TEMPLATE_DIR, no_input=True, extra_context=EXAMPLE_CONTEXT, output_dir=tmp_path
    ))


def test_generate_new_project(tmp_path, generated_project_path):

    assert generated_project_path == tmp_path / PROJECT_NAME


def test_poetry_uses_dev_group(generated_project_path):

    pyproject_toml_content = generated_project_path.joinpath("pyproject.toml").read_text()

    assert "dev-dependencies" not in pyproject_toml_content
    assert "[tool.poetry.group.dev.dependencies]" in pyproject_toml_content.splitlines()
