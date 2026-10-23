# environment setup
python scripts/update-python-requirement.py

uv self update
uv sync --group dev
uv pip install --upgrade pip

# Create variables file
cat > .env << 'EOF'
VAR_1="foo"
VAR_2="bar"
EOF

# Initialize docs submodule
git submodule sync --recursive
git submodule update --init --remote --recursive
