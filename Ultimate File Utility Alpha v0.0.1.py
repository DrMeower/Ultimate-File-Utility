# The Ultimate File Manager

import os
import os.path
import shutil
import glob
import datetime
import getpass

print("""Welcome to the Ultimate File Manager Utility!
Please select the action you want to perform:

1: Basic Backup
2: Automatic Downloads directory sort
3: Custom patern
4: Duplicate File Scanner""")

selection = input()
user = getpass.getuser()

# Backup
if selection == "1":

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    folder_to_backup = input(r"Which directory do you want to backup? ")
    where_to_backup = input(r"Where do you want to store the current backup? ")
    backed_up_folder = os.path.join(where_to_backup, timestamp)
    backup = shutil.copytree(
        folder_to_backup, backed_up_folder)


# Downloads Folder Sort
if selection == "2":

    folder = input("What folder to sort? ")
    if folder == "":
        folder = rf"C:\Users\{user}\Downloads"

# Pattern
    pdf = os.path.join(folder, "*.pdf")
    txt = os.path.join(folder, "*.txt")
    zip = os.path.join(folder, "*.zip")
    jpg = os.path.join(folder, "*.jpg")
    png = os.path.join(folder, "*.png")

# Move to each sorted folder
    pdf_folder = shutil.move(
        pdf, rf"C:\Users\{user}\Desktop\Downloads Sorted\pdfs")
    if not os.path.exists(pdf_folder):
        os.mkdir(pdf_folder)
    txt_folder = shutil.move(
        txt, rf"C:\Users\{user}\Desktop\Downloads Sorted\txt")
    if not os.path.exists(txt_folder):
        os.mkdir(txt_folder)
    zip_folder = shutil.move(
        zip, rf"C:\Users\{user}\Desktop\Downloads Sorted\zips")
    if not os.path.exists(zip_folder):
        os.mkdir(zip_folder)
    jpg_folder = shutil.move(
        jpg, rf"C:\Users\{user}\Desktop\Downloads Sorted\jpgs")
    if not os.path.exists(jpg_folder):
        os.mkdir(jpg_folder)
    png_folder = shutil.move(
        png, rf"C:\Users\{user}\Desktop\Downloads Sorted\png")
    if not os.path.exists(png_folder):
        os.mkdir(png_folder)


# Custom Pattern
if selection == "3":

    unsorted_folder = input(r"Enter the full directory path: ")
    sorted_folder = input(r"Enter the full destination path: ")

    # Default directories
    if unsorted_folder == "":
        unsorted_folder = r"C:\Users\arisd\Desktop\Python\File Organizer - Unsorted Files"
    if sorted_folder == "":
        sorted_folder = r"C:\Users\arisd\Desktop\Python\File Organizer - Sorted Files"

    pattern = input("Please provide a filetype pattern: (e.g. *.txt) ")
    search_path = os.path.join(unsorted_folder, pattern)

    # Find and move each file
    for file_path in glob.glob(search_path):
        print(f"Moving {file_path} -> {sorted_folder}")
        shutil.move(file_path, sorted_folder)
        print(f"Moved: {file_path}")


# Duplicate File Scanner
if selection == "4":
    first_folder = input("Please select the first directory to scan: ")
    second_folder = input("Please select the second directory to scan: ")

    files_one = os.listdir(first_folder)
    files_two = os.listdir(second_folder)

    view = input("Do you want to view each directory's contents?: (Yes/No) ")

    if view == "Yes":
        print("Folder One Files: ", files_one)
        print("Folder Two Files: ", files_two)

    set_one = set(files_one)
    set_two = set(files_two)

    duplicates = set_one.intersection(set_two)

    if duplicates:
        print("Duplicate files found: ")
        for file in duplicates:
            print(f"- {file}")
    else:
        print("No duplicates found.")
