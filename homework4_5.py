import os
class EvenNumberGenerator:
    def __init__(self):
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        even_number = self.current
        self.current += 1
        return even_number

class LimitEvenNumberGenerator:
    def __init__(self,generator, limit):
        self.generator = generator
        self.limit = limit

    def __enter__(self):
        return self.generator

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


output_file_path = 'even_numbers_output.txt'

with open(output_file_path, 'w') as file:
    for i in range(100):
        even_number = i * 2
        file.write(f"{even_number}\n")

print(f"Парні числа записані у файл '{output_file_path}'.")
