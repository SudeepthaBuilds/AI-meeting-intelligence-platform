import os

path = r"media\meetings\Screen_Recording_2026-07-08_185323.mp4"

print("Exists:", os.path.exists(path))
print("Absolute Path:", os.path.abspath(path))
print("Current Directory:", os.getcwd())
