# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

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
│   └── unit # Unit tests
│       └── test_mypackage.py
└── uv.lock
```

## API reference

::: mypackage
