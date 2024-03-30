import openpyxl as op

def add_password():
    # path = r"C:\Users\User\Documents\password-handler\file"
    path = "/Users/yoosunu/Desktop/password-handler/새 폴더"
    wb = op.load_workbook(path+"/password.xlsx")
    # wb = op.load_workbook(path+"/password.csv")
    ws = wb.active

    data = []

    print("사이트의 이름을 입력해주세요: ")
    SITE = str(input())
    print("아이디를 입력해주세요: ")
    ID = str(input())
    print("비밀번호를 입력해주세요: ")
    PASSWORD = str(input())

    """data define"""

    # SITE = "google"
    # ID = "id"
    # PASSWORD = "password"

    data.append(SITE)
    data.append(ID)
    data.append(PASSWORD)

    """data input"""

    cell_length = []
    i = 1
    j = True
    while j == False:
        cell_first = ws.cell(row=1, columns=i)
        cell_length.append(cell_first)
        i += 1
        if cell_first == None:
            j == False

    for columns in range(1, len(cell_length) + 1):
        cell_site = ws.cell(row=1, column=columns)
        if cell_site.value == None:
            for i, value in enumerate(data):
                ws.cell(row=1+i, column=columns, value=value)
            break

    """saving"""

    wb.save(path + "/password.xlsx")
    # wb.save(path + "/password.csv")
    wb.close()

