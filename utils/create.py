import openpyxl as op


def workbook_create():
    wb = op.Workbook()
    ws = wb.active

    # window os
    path = r"C:\Users\User\Documents\password-handler\file"
    # mac os
    # path = "/Users/yoosunu/Desktop/password-handler/새 폴더"

    BASES = ["SITE", "ID", "PW"]
    for i, BASE in enumerate(BASES, start=1):
        ws.cell(row=i, column=1, value=BASE)

    wb.save(path + "\password.xlsx")
    wb.close()
