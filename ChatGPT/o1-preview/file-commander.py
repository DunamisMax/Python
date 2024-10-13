#!/usr/bin/env python3

import sys
import shutil
import zipfile
from pathlib import Path
import threading
import hashlib
import logging
from datetime import datetime
from tqdm import tqdm
from cryptography.fernet import Fernet

# Initialize logging
logging.basicConfig(
    filename='file_manager.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class FileManager:
    def __init__(self, root_dir):
        self.root_dir = Path(root_dir)
        if not self.root_dir.exists():
            print(f"Root directory '{self.root_dir}' does not exist.")
            sys.exit(1)
        self.matching_files = []
        self.key = None  # For encryption/decryption

    @staticmethod
    def clean_file_types(file_types):
        if not file_types:
            return None
        cleaned_types = [f".{ft.strip().lower().lstrip('.')}" for ft in file_types.split(",")]
        return cleaned_types

    def get_matching_files(self, file_types=None):
        if file_types:
            self.matching_files = [p for p in self.root_dir.rglob('*') if p.suffix.lower() in file_types and p.is_file()]
        else:
            self.matching_files = [p for p in self.root_dir.rglob('*') if p.is_file()]
        return self.matching_files

    def copy_files(self, destination):
        destination = Path(destination)
        for file in tqdm(self.matching_files, desc="Copying files"):
            dest_path = destination / file.relative_to(self.root_dir)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(file, dest_path)
        logging.info(f"Copied {len(self.matching_files)} files to '{destination}'")
        print(f"Copied {len(self.matching_files)} files to '{destination}'.")

    def smart_rename(self):
        for file in self.matching_files:
            basename = file.name
            print(f"Current File: {basename}")
            new_name = input(f"Enter new name for '{basename}' (or leave blank to skip): ").strip()
            if new_name:
                new_name_with_ext = f"{new_name}{file.suffix}"
                new_path = file.with_name(new_name_with_ext)
                try:
                    file.rename(new_path)
                    logging.info(f"Renamed '{basename}' to '{new_name_with_ext}'")
                    print(f"Renamed '{basename}' to '{new_name_with_ext}'.")
                except Exception as e:
                    logging.error(f"Failed to rename '{basename}': {e}")
                    print(f"Error renaming '{basename}': {e}")

    def delete_files(self):
        confirm = input(f"Are you sure you want to delete {len(self.matching_files)} files? (y/n): ").lower()
        if confirm == 'y':
            for file in tqdm(self.matching_files, desc="Deleting files"):
                try:
                    file.unlink()
                    logging.info(f"Deleted '{file}'")
                except Exception as e:
                    logging.error(f"Failed to delete '{file}': {e}")
                    print(f"Error deleting '{file}': {e}")
            print(f"Deleted {len(self.matching_files)} files.")
        else:
            print("Deletion aborted.")

    def move_files(self, destination):
        destination = Path(destination)
        for file in tqdm(self.matching_files, desc="Moving files"):
            dest_path = destination / file.relative_to(self.root_dir)
            dest_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.move(str(file), str(dest_path))
                logging.info(f"Moved '{file}' to '{dest_path}'")
            except Exception as e:
                logging.error(f"Failed to move '{file}': {e}")
                print(f"Error moving '{file}': {e}")
        print(f"Moved {len(self.matching_files)} files to '{destination}'.")

    def list_files(self):
        for file in self.matching_files:
            print(file)
        print(f"Total files: {len(self.matching_files)}")

    def change_file_extension(self, new_extension):
        if not new_extension.startswith('.'):
            new_extension = f'.{new_extension}'
        for file in tqdm(self.matching_files, desc="Changing file extensions"):
            new_file_name = file.with_suffix(new_extension)
            try:
                file.rename(new_file_name)
                logging.info(f"Changed extension of '{file.name}' to '{new_file_name.name}'")
            except Exception as e:
                logging.error(f"Failed to change extension for '{file}': {e}")
                print(f"Error changing extension for '{file}': {e}")
        print(f"Changed extension of {len(self.matching_files)} files to '{new_extension}'.")

    def compress_files(self, zip_name):
        zip_path = Path(zip_name)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file in tqdm(self.matching_files, desc="Compressing files"):
                try:
                    zipf.write(file, file.relative_to(self.root_dir))
                    logging.info(f"Added '{file}' to '{zip_name}'")
                except Exception as e:
                    logging.error(f"Failed to add '{file}' to '{zip_name}': {e}")
                    print(f"Error compressing '{file}': {e}")
        print(f"Compressed {len(self.matching_files)} files into '{zip_name}'.")

    def encrypt_files(self):
        if not self.key:
            self.key = Fernet.generate_key()
            with open('filekey.key', 'wb') as keyfile:
                keyfile.write(self.key)
        else:
            with open('filekey.key', 'rb') as keyfile:
                self.key = keyfile.read()
        fernet = Fernet(self.key)
        for file in tqdm(self.matching_files, desc="Encrypting files"):
            try:
                with file.open('rb') as original_file:
                    original = original_file.read()
                encrypted = fernet.encrypt(original)
                with file.open('wb') as encrypted_file:
                    encrypted_file.write(encrypted)
                logging.info(f"Encrypted '{file}'")
            except Exception as e:
                logging.error(f"Failed to encrypt '{file}': {e}")
                print(f"Error encrypting '{file}': {e}")
        print(f"Encrypted {len(self.matching_files)} files.")

    def decrypt_files(self):
        if not self.key:
            if Path('filekey.key').exists():
                with open('filekey.key', 'rb') as keyfile:
                    self.key = keyfile.read()
            else:
                print("Encryption key not found. Cannot decrypt files.")
                return
        fernet = Fernet(self.key)
        for file in tqdm(self.matching_files, desc="Decrypting files"):
            try:
                with file.open('rb') as encrypted_file:
                    encrypted = encrypted_file.read()
                decrypted = fernet.decrypt(encrypted)
                with file.open('wb') as decrypted_file:
                    decrypted_file.write(decrypted)
                logging.info(f"Decrypted '{file}'")
            except Exception as e:
                logging.error(f"Failed to decrypt '{file}': {e}")
                print(f"Error decrypting '{file}': {e}")
        print(f"Decrypted {len(self.matching_files)} files.")

    def checksum_files(self):
        checksums = {}
        for file in tqdm(self.matching_files, desc="Calculating checksums"):
            try:
                hasher = hashlib.sha256()
                with file.open('rb') as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hasher.update(chunk)
                checksum = hasher.hexdigest()
                checksums[str(file)] = checksum
                logging.info(f"Calculated checksum for '{file}': {checksum}")
            except Exception as e:
                logging.error(f"Failed to calculate checksum for '{file}': {e}")
                print(f"Error calculating checksum for '{file}': {e}")
        print("Checksums calculated for files:")
        for filepath, checksum in checksums.items():
            print(f"{filepath}: {checksum}")

    def run(self):
        # Step 2: Input the file types to search for (optional)
        file_types_input = input("Enter file types to search for (comma-separated, or press Enter for all file types): ").strip()
        file_types = self.clean_file_types(file_types_input)

        # Step 3: Get the matching files
        self.get_matching_files(file_types)

        if not self.matching_files:
            print("No matching files found.")
            return

        # Step 4: Display options to the user
        while True:
            print("\nWhat do you want to do with these files?")
            print("1. Copy from one folder to another")
            print("2. Smart rename")
            print("3. Delete files")
            print("4. Move files to another folder")
            print("5. List all files")
            print("6. Change file extension")
            print("7. Compress files into a ZIP")
            print("8. Encrypt files")
            print("9. Decrypt files")
            print("10. Calculate checksums")
            print("11. Exit")

            choice = input("\nEnter your choice (1-11): ").strip()

            if choice == '1':
                dest_dir = input("Enter the destination folder path: ").strip()
                self.copy_files(dest_dir)
            elif choice == '2':
                self.smart_rename()
            elif choice == '3':
                self.delete_files()
            elif choice == '4':
                dest_dir = input("Enter the destination folder path: ").strip()
                self.move_files(dest_dir)
            elif choice == '5':
                self.list_files()
            elif choice == '6':
                new_extension = input("Enter the new extension (e.g., .txt): ").strip()
                if not new_extension.startswith('.'):
                    new_extension = '.' + new_extension
                self.change_file_extension(new_extension)
            elif choice == '7':
                zip_name = input("Enter the name of the ZIP file (e.g., archive.zip): ").strip()
                if not zip_name.endswith('.zip'):
                    zip_name += '.zip'
                self.compress_files(zip_name)
            elif choice == '8':
                self.encrypt_files()
            elif choice == '9':
                self.decrypt_files()
            elif choice == '10':
                self.checksum_files()
            elif choice == '11':
                print("Exiting the program.")
                break
            else:
                print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    # Step 1: Input the root directory
    root_dir_input = input("Enter root directory to search: ").strip()
    file_manager = FileManager(root_dir_input)
    file_manager.run()