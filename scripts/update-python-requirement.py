'''
Helper that identifies the current python version being used in the dev environment setup, and updates the `requires-python` field in the `pyproject.toml` file accordingly.

If a `requires-python` field already exists in the `pyproject.toml` file, it will be updated to match the current Python version. Otherwise, the field will be added after the `readme` field.
'''

from pathlib import Path
import re
import sys


pyproject_path = Path("pyproject.toml")
pyproject = pyproject_path.read_text()
python_version = ".".join(map(str, sys.version_info[:3]))
requires_python = f'requires-python = ">={python_version}"'

# Replace the existing requirement so repeated setup runs remain idempotent.
if re.search(r"^requires-python\s*=", pyproject, flags=re.MULTILINE):
    pyproject = re.sub(
        r"^requires-python\s*=.*$",
        requires_python,
        pyproject,
        flags=re.MULTILINE,
    )

# Keep project metadata together by inserting the new field after `readme`.
else:
    pyproject = re.sub(
        r"^(readme\s*=.*\n)",
        rf"\1{requires_python}\n",
        pyproject,
        count=1,
        flags=re.MULTILINE,
    )

pyproject_path.write_text(pyproject)
