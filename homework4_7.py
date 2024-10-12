import os

def error_log_generator(log_file_path):
    with open(log_file_path, 'r') as log_file:
        for line in log_file:
            yield line

def filter_and_save_errors(log_file_path, error_file_path):
    with open(error_file_path, 'w') as error_file:
        for line in error_log_generator(log_file_path):
            if ' 4' in line:
                error_file.write(line)

input_directory = 'logs2'
output_directory = 'filtered_logs4xx'

input_file_path = os.path.join(input_directory, 'logfile4xx.txt')
output_file_path = os.path.join(output_directory, 'відфільтрований_файл.txt')

os.makedirs(output_directory, exist_ok=True)

filter_and_save_errors(input_file_path, output_file_path)

print(f"Помилки записані у файл '{output_file_path}'.")
