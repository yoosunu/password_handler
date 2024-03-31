from utils.create import workbook_create
from utils.modify import add_password
import os
from pathlib import Path

# from os import path

folder_path = Path(r"C:\Users\User\Documents\password-handler\file")
# folder_path = Path("/Users/yoosunu/Desktop/password-handler/files")
file_name = "password.xlsx"
# file_name = "password.csv"
file_path = folder_path / file_name

if os.path.exists(file_path):
    add_password()
else:
    workbook_create()
    add_password()
