import os


class FileIterator:
    def __init__(self, directory):
        self.directory = directory
        self.files = os.listdir(directory)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # Поки є файли для обробки
        while self.index < len(self.files):
            filename = self.files[self.index]
            self.index += 1

            file_path = os.path.join(self.directory, filename)

            if os.path.isfile(file_path):
                return filename, os.path.getsize(file_path)

        raise StopIteration



directory_path = '/home/pasha/PycharmProjects/pythonProject4/directory_path'
file_iterator = FileIterator(directory_path)

for filename, file_size in file_iterator:
    print(f"{filename}: {file_size} байт")
