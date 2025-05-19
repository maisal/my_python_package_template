# My Python package template

## Features

- src layout for clean module packaging and import management
- Uses [mise](https://github.com/jdx/mise) to manage development environment and run tasks
- Uses [uv](https://github.com/astral-sh/uv) to manage Python packages
- Uses [ruff](https://github.com/astral-sh/ruff) as a linter and formatter
- Uses [mypy](https://github.com/python/mypy) for static type checking
- Uses [mkdocs](https://github.com/mkdocs/mkdocs) to build project documentation
- Uses [pytest](https://github.com/pytest-dev/pytest) to test Python code
- Uses [tox-uv](https://github.com/tox-dev/tox-uv) to run tests across multiple Python versions
- Dynamically derives the package version from Git tags and commit hashes
- Installs `ruff`, `mypy`, `mkdocs`, `pytest`, and `tox-uv` as Python packages using uv

## Project layout

```
.
├── .github
│   └── workflows
│       └── pytest.yml  # CI for tests
├── .gitignore
├── .mise.toml  # Environment and task runner configuration
├── .pre-commit-config.yaml  # Linter/formatter hooks
├── docs
│   └── index.md  # Project documentation
├── LICENSE
├── mkdocs.yml  # mkdocs configuration
├── pyproject.toml
├── README.md
├── src
│   └── mypackage
│       ├── __init__.py
│       └── core.py
├── tests
│   ├── integration  # Integration tests
│   │   └── test_integration.py
│   └── unit  # Unit tests
│       └── test_mypackage.py
└── uv.lock
```

## Usage
[mise](https://github.com/jdx/mise) is required for this template.
Please install and configure mise by following the [mise installation guide](https://mise.jdx.dev/getting-started/installation.html).
To set up the development environment, simply run:
```shell
mise init
```
This will:
  - Install the required Python version and tools
  - Create a virtual environment
  - Install Python packages and pre-commit hooks

The package version is dynamically generated using Git metadata.
A version file will be written to the path specified in pyproject.toml:
```pyproject.toml
[tool.setuptools_scm]
write_to = "src/mypackage/_version.py"
```

You can then run predefined tasks using mise:
```shell
$ mise task
Name                Description
ci                  Run tests on multiple Python versions using tox
doc                 Build and serve package documentation
init                Set up the development environment
pytest              Run unit tests using pytest with coverage report
pytest-integration  Run integration tests using pytest
```
