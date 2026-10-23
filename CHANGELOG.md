# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.1]

### Fixed

- `init-template` and `dev-setup` scripts now use `git submodule update --remote` for the `docs` submodule, so they check out the wiki's actual current commit instead of failing on the template's stale pinned commit SHA (#22)
- `docs` submodule marked `ignore = all` in `.gitmodules` so its commit, which tracks the wiki's moving `HEAD` rather than a fixed pin, no longer shows as a perpetual dirty change in `git status`
- `init-template` scripts now commit the resolved `docs` submodule pointer and `.gitmodules` URL after setup

## [0.4.0]

### Added

- `init-template` scripts to repoint the docs wiki submodule at this repository's
  wiki when starting a new repository from this template
- `[tool.python-software-template]` version field in `pyproject.toml` to track which template version a repo was scaffolded from (#18)

## [0.3.0]

### Added

- `dev-setup` updated to sync only dev dependencies

## [0.2.0]

### Added

- RUFF linter support
- TOML language support
- CHANGELOG.md file
- Documentation added on submodule
- Added example variables in settings.py file from .env file
- Added example code in main.py

### Changed

- `source` folder renamed to `src` to meet a more broad industry standard

## [0.1.1] - 2026-02-06

### Added

- Development setup scripts for Windowns
- Development setup scripts for MacOs
- Development setup scripts for Linux
- Python version management via `.python-version` file

### Removed

- uv.lock file

## [0.1.0] - 2025-07-06

### Added

- UV package manager support

## [0.0.1] - 2025-06-08

### Fixed

- Configuration of development environment failure from a hardcoded path

## [0.0.0] - 2024-11-11



[0.4.1]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.4.1
[0.4.0]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.4.0
[0.3.0]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.3.0
[0.2.0]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.2.0
[0.1.1]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.1.1
[0.1.0]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.1.0
[0.0.1]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.0.1
[0.0.0]: https://github.com/caio-pavesi/python-software-template/releases/tag/0.0.0
