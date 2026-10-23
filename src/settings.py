"""
Global settings for the project.

All global variables should be defined here, as well as environment
variables (in the .env file) should be imported and defined in this file.
"""

from pathlib import Path

from decouple import config

# Project directory
BASE_DIR = Path(__file__).parent.parent.resolve()

# Environment / .env variables
VAR_1 = config("VAR_1", default = "EXAMPLE_1", cast = str)
VAR_2 = config("VAR_2", default = "EXAMPLE_2", cast = str)
