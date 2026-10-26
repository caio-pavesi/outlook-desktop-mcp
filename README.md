# Desktop Outlook App MCP server

When workiq is blocked by your organization, this mcp server can act on your outlook e-mail without using blocked microsoft graph connections

# Table of Contents

- [Desktop Outlook App MCP server](#desktop-outlook-app-mcp-server)
- [Table of Contents](#table-of-contents)
- [Install](#install)
- [Usage](#usage)
- [Docs](#docs)
- [Contributing](#contributing)
- [License](#license)

# Install

> This requires the latest version of Python and UV installed, check the [Python Downloads page] and the [UV Installation page] to the understand the installation process

Clone this repository to your computer using the following code, and that's it!

```powershell
git clone https://github.com/caio-pavesi/outlook-desktop-mcp.git
```

This server automates the local Outlook desktop app via `pywin32`/COM, so it only runs on Windows with Outlook installed, signed in, and open.

# Usage

After cloning this you can just hit `ctrl+b` and vscode will run the nescessary [scripts](/scripts) to prepare the repository with a virtual environment based on the python version being run, the required libraries, and a non-controlled `.env` variables file.

The server is registered in [.vscode/mcp.json](/.vscode/mcp.json) under the name `outlook` and starts with `uv run main.py`. This requires Python and [UV] to be installed (see [Install](#install)). If you need to add it to your own VS Code `mcp.json`, use the snippet below, replacing `--directory`'s value with the absolute path to **your** local clone's `src` folder:

```jsonc
{
  "servers": {
    "outlook": {
      "command": "uv",
      "args": [
        "--directory",
        "<<YOUR PATH TO SRC FOLDER>>",
        "run",
        "main.py"
      ]
    }
  }
}
```

Once running, it exposes the following tools:

| Tool | Description |
| --- | --- |
| `get_emails(start_date, end_date)` | List inbox emails received within a date range, including each email's `EntryID`. |
| `reply_to_email(entry_id, body)` | Reply to the sender of an email identified by its `EntryID`. |
| `reply_all_to_email(entry_id, body)` | Reply to everyone on an email identified by its `EntryID`. |
| `forward_email(entry_id, to, body)` | Forward an email identified by its `EntryID` to one or more recipients. |
| `send_email(to, subject, body, cc)` | Compose and send a brand-new email. |

Uses the `EntryID` returned by `get_emails` as the `entry_id` argument for the reply/forward tools.

# Docs

I'm still working on them, but you'll find them in the [docs folder](/docs/) and in the [github wiki](https://github.com/caio-pavesi/python-software-template/wiki).

# Contributing

If you're using this template and you find any bugs, please do insert them into the [GitHub issues](https://github.com/caio-pavesi/python-software-template/issues). And if you want to contribute to the code speak to me directly via [e-mail](mailto:ocaiopavesi@gmail.com) and adhere to the following standards:
* https://agents.md/
* https://semver.org/
* https://keepachangelog.com/en/1.1.0/
* https://github.com/RichardLitt/standard-readme
* https://www.conventionalcommits.org/en/v1.0.0/
* https://nvie.com/posts/a-successful-git-branching-model/

# License

[MIT © Caio Pavesi](/LICENSE).

<!-- Links -->
[Python Downloads page]: https://www.python.org/downloads/
[UV Installation page]: https://docs.astral.sh/uv/getting-started/installation/
[UV]: https://docs.astral.sh/uv/getting-started/installation/