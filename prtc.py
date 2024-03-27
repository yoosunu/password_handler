import openpyxl as op

wb = op.load_workbook(r"C:\Users\User\Documents\password-handler\file\test.xlsx")
ws = wb.active

data = [1,2,3,4,5,6]

# for i, value in enumerate(data):
#     ws.cell(row=1, column=1+i, value=value)

wb.save(r"C:\Users\User\Documents\password-handler\file\test.xlsx")
wb.close()