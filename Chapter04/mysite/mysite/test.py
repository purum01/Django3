from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
print(BASE_DIR)
print(Path(__file__))
print(Path(__file__).resolve())
print(Path(__file__).resolve().parent)
print(Path(__file__).resolve().parent.parent)
