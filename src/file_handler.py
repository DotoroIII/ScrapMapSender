import os
import zipfile


def compress_map(map_path):
    with zipfile.ZipFile(f"{os.path.splitext(os.path.basename(map_path))[0]}.zip", "w") as zip_archive:
        zip_archive.write(map_path, os.path.basename(map_path), zipfile.ZIP_DEFLATED)
        zip_archive.close()

def decompress_map(zip_map_path, output_folder):
    zip = zipfile.ZipFile(f"{zip_map_path}")
    zip.extract(f"{os.path.splitext(os.path.basename(zip_map_path))[0]}.db", output_folder)
    zip.close()