from utils.create import workbook_create
from utils.modify import add_password
from pathlib import Path

# folder_path = Path(r"C:\Users\User\Documents\password-handler\file")
folder_path = Path("/Users/yoosunu/Desktop/password-handler/새 폴더")
file_name = "password.xlsx" 
# file_name = "password.csv"
file_path = folder_path / file_name

if file_path.exists():
    add_password()
else:
    workbook_create()
    add_password()
    