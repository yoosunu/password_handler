import openpyxl as op

def add_password():
    path = r"C:\Users\User\Documents\password-handler\file"
    wb = op.load_workbook(path+"\password.xlsx")
    ws = wb.active

    data = []

    print("사이트의 이름을 입력해주세요: ")
    SITE = input()
    print("아이디를 입력해주세요: ")
    ID = input()
    print("비밀번호를 입력해주세요: ")
    PASSWORD = input()

    """data define"""

    # SITE = 1
    # ID = 2
    # PASSWORD = 3

    data.append(SITE)
    data.append(ID)
    data.append(PASSWORD)

    """data input"""

    for columns in range(1, len(data) + 1):
        cell_site = ws.cell(row=1, column=columns)
        if cell_site.value == None:
            for i, value in enumerate(data):
                ws.cell(row=1+i, column=columns, value=value)
            break



    """saving"""

    wb.save(path + "\password.xlsx")
    wb.close()

