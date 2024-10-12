class ReverseFileIterator:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = open(file_path, 'rb')
        self.file.seek(0, 2)  # Перейти до кінця файлу
        self.position = self.file.tell()

    def __iter__(self):
        return self

    def __next__(self):
        if self.position == 0:
            self.file.close()
            raise StopIteration


with open('/homework4_1.py') as file:
    lines = file.readlines()  # Зчитує всі рядки
    for line in reversed(lines):  # Проходить по рядках у зворотному порядку
        print(line.strip())  # Виводить рядок без пробілів на початку і в кінці



