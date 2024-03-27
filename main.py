from utils.create import workbook_create
from utils.modify import add_password
from pathlib import Path

folder_path = Path(r"C:\Users\User\Documents\password-handler\file")
file_name = "password.xlsx"
file_path = folder_path / file_name

if file_path.exists():
    add_password()
else:
    workbook_create()