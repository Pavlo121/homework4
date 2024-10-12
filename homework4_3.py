import os
import csv
from PIL import Image


class ImageMetadata:
    def __init__(self, directory):
        self.directory = directory
        self.images = [f for f in os.listdir(directory) if
                       f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    def get_metadata(self):
        for image in self.images:
            image_path = os.path.join(self.directory, image)
            with Image.open(image_path) as img:
                yield {
                    'filename': image,
                    'format': img.format,
                    'size': img.size,
                    'mode': img.mode
                }


def save_metadata_to_csv(directory, output_csv):
    metadata_extractor = ImageMetadata(directory)

    with open(output_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['filename', 'format', 'size', 'mode'])
        writer.writeheader()

        for metadata in metadata_extractor.get_metadata():
            writer.writerow(metadata)


# Використання
image_directory = '/home/pasha/PycharmProjects/pythonProject4/images'
output_csv_file = '/home/pasha/PycharmProjects/pythonProject4/image_metadata.csv'
save_metadata_to_csv(image_directory, output_csv_file)
