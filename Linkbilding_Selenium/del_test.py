import os

current_dir = os.getcwd()
next_folder = os.path.basename(os.path.dirname(__file__))

print("Текущий раздел:", current_dir)
print("Следующая папка текущего файла:", next_folder)