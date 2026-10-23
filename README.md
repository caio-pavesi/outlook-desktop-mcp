# Python Software Template

Easily start-up a repository for your python software projects. Note that this won't be the best of for libraries or packaged apps.

# Table of Contents

- [Python Software Template](#python-software-template)
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
git clone https://github.com/caio-pavesi/python-software-template.git
```

# Usage

If you're starting a new repository from this template, first run the matching `scripts/init-template.*` for your OS (e.g. `powershell scripts/init-template.ps1` on Windows) to repoint the `docs` wiki submodule at your repository's wiki.

After cloning this you can just hit `ctrl+b` and vscode will run the nescessary [scripts](/scripts) to prepare the repository with a virtual environment based on the python version being run, the required libraries, and a non-controlled `.env` variables file.

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