import os

def filter_lines(file_path, keyword):
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            if keyword in line:
                yield line.strip()

def write_filtered_lines(input_file, output_file, keyword):
    with open(output_file, 'w', encoding='utf-8') as output:
        for line in filter_lines(input_file, keyword):
            output.write(line + '\n')  

input_directory = 'logs'
output_directory = 'filtered_logs'

input_file_path = os.path.join(input_directory, 'лог_файл.txt')
output_file_path = os.path.join(output_directory, 'відфільтрований_файл.txt')
keyword = 'Ошибка'

os.makedirs(output_directory, exist_ok=True)

write_filtered_lines(input_file_path, output_file_path, keyword)
print(f"Рядки, що містять '{keyword}', записані у '{output_file_path}'.")
