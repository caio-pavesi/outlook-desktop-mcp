# One-time setup: point the docs wiki submodule at this repository's wiki.

origin_url=$(git remote get-url origin)
wiki_url="${origin_url%.git}.wiki.git"

git config --file .gitmodules submodule.docs.url "$wiki_url"
git config --file .gitmodules submodule.docs.ignore all

git submodule sync --recursive
git submodule update --init --remote --recursive

git add .gitmodules docs
git commit -m "chore: point docs submodule at repository wiki"
