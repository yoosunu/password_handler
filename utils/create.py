import openpyxl as op

def workbook_create():
    wb = op.Workbook()
    wb.active

    # path = r"C:\Users\User\Documents\password-handler\file"
    path = "/Users/yoosunu/Desktop/password-handler/새 폴더"
    wb.save(path + "/password.xlsx")
    # wb.save(path + "/password.csv")
    wb.close()
