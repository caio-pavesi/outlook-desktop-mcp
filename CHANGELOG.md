# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Outlook desktop MCP server (`outlook`) replacing the weather sample server, using `pywin32` to drive the local Outlook application.
- `get_emails` tool to list inbox emails received within a given date range.
- `reply_to_email` and `reply_all_to_email` tools to reply to an email identified by its `EntryID`.
- `forward_email` tool to forward an email identified by its `EntryID` to one or more recipients.
- `send_email` tool to compose and send a new email.

### Changed

- `pyproject.toml` has a dependency group for production

[Unreleased]: https://github.com/caio-pavesi/outlook-desktop-mcp/tree/develop

