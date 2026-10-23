# One-time setup: point the docs wiki submodule at this repository's wiki.

$originUrl = git remote get-url origin
$wikiUrl = ($originUrl -replace '\.git$', '') + '.wiki.git'

git config --file .gitmodules submodule.docs.url $wikiUrl
git config --file .gitmodules submodule.docs.ignore all

git submodule sync --recursive
git submodule update --init --remote --recursive

git add .gitmodules docs
git commit -m "chore: point docs submodule at repository wiki"
