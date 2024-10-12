import os
import shutil

class BackupManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.backup_path = f"{file_path}.bak"

    def __enter__(self):
        if os.path.exists(self.file_path):
            shutil.copy2(self.file_path, self.backup_path)
        return self.file_path

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type is None:
            if os.path.exists(self.backup_path):
                os.remove(self.backup_path)
        else:
            if os.path.exists(self.backup_path):
                shutil.copy2(self.backup_path, self.file_path)
            print(f"Сталася помилка: {exc_value}. Файл відновлено з резервної копії.")
        return False

file_path = 'important_file.txt'

try:
    with BackupManager(file_path) as file:
        with open(file, 'w') as f:
            f.write("Нова важлива інформація")

    print(f"Файл '{file_path}' успішно оброблений.")
except Exception as e:
    print(f"Обробка файлу завершилася з помилкою: {e}")
