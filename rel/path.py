# rel/path.py
from pathlib import Path

def get_root_path():
    """Return the root path of the project."""
    return Path(__file__).resolve().parent

def get_data_path():
    """Return the data path of the project."""
    root_path = get_root_path()
    return root_path / "data"

def create_data_dir():
    """Create the data directory if it does not exist."""
    data_path = get_data_path()
    data_path.mkdir(exist_ok=True)