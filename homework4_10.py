import zipfile
import os

class ZipManager:
    def __init__(self, zip_file_path):
        self.zip_file_path = zip_file_path
        self.zip_file = None

    def __enter__(self):
        self.zip_file = zipfile.ZipFile(self.zip_file_path, 'w', zipfile.ZIP_DEFLATED)
        return self

    def add_file(self, file_path, arcname=None):
        if arcname is None:
            arcname = os.path.basename(file_path)
        self.zip_file.write(file_path, arcname)

    def __exit__(self, exc_type, exc_value, traceback):
        self.zip_file.close()

zip_file_path = 'example_archive.zip'

with ZipManager(zip_file_path) as zip_manager:
    zip_manager.add_file('file1.txt')
    zip_manager.add_file('file2.txt', 'folder_in_zip/file2.txt')

print(f"Файли успішно додано до архіву '{zip_file_path}'.")
