from pathlib import Path

from cookiecutter.main import cookiecutter

TEMPLATE_DIR = str(Path(__file__).parent.parent)

PROJECT_NAME = "example-project"

EXAMPLE_CONTEXT = {
    "author_name": "John Doe",
    "author_email": "john.doe@mail.com",
    "github_username": "johndoe",
    "project_name": PROJECT_NAME,
    "project_short_description": "A short description of the project",
}


def test_generate_new_project(tmp_path):
    path_to_new_project = cookiecutter(
        TEMPLATE_DIR, no_input=True, extra_context=EXAMPLE_CONTEXT, output_dir=tmp_path
    )
    assert path_to_new_project == str(tmp_path / PROJECT_NAME)
