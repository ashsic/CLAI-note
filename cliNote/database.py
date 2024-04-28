"""This module provides basic local flatfile JSON storage."""

import configparser
from pathlib import Path

from cliNote import DB_WRITE_ERROR, SUCCESS

DEFAULT_DB_FILE_PATH = Path.home().joinpath(
    "." + Path.home().stem + "_todo.json"
)

def get_database_path(config_file: Path) -> Path:
    config_parser = configparser.ConfigParser()
    config_parser.read(config_file)
    return Path(config_parser["General"]["database"])

def init_database(db_path: Path) -> int:
    # Creates db
    try:
        db_path.write_text("[]") # Create empty db
        return SUCCESS
    except OSError:
        return DB_WRITE_ERROR