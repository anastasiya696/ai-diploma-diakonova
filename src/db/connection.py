import sqlite3
from pathlib import Path


def get_connection(db_name="my_exam_kids_world.db"):
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    db_path = data_dir / db_name
    connection = sqlite3.connect(db_path)

    return connection