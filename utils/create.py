import openpyxl as op

def workbook_create():
    wb = op.Workbook()
    ws = wb.active

    path = r"C:\Users\User\Documents\password-handler\file"
    wb.save(path + "\password.xlsx")
    wb.close()
