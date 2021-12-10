import yaml
from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_DIR = str(Path(__file__).parent.parent)
CONTEXT_FILE = Path(__file__).parent / "context.yaml"

with open(CONTEXT_FILE) as file_handler:
    content = yaml.safe_load(file_handler)

EXAMPLE_CONTEXT = content['default_context']
PROJECT_NAME = EXAMPLE_CONTEXT["project_name"]


def test_generate_new_project(tmp_path):
    path_to_new_project = cookiecutter(
        TEMPLATE_DIR, no_input=True, extra_context=EXAMPLE_CONTEXT, output_dir=tmp_path
    )
    assert path_to_new_project == str(tmp_path / PROJECT_NAME)
