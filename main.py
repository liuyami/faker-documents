from faker import Faker
import xlrd
import xlwt
from xlutils.copy import copy

fake = Faker('zh_CN')



def write_excel_xls(path, sheet_name, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlwt.Workbook()  # 新建一个工作簿
    sheet = workbook.add_sheet(sheet_name)  # 在工作簿中新建一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            sheet.write(i, j, value[i][j])  # 像表格中写入数据（对应的行和列）
    workbook.save(path)  # 保存工作簿
    #print("xls格式表格写入数据成功！")
 
 
def write_excel_xls_append(path, value):
    index = len(value)  # 获取需要写入数据的行数
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    rows_old = worksheet.nrows  # 获取表格中已存在的数据的行数
    new_workbook = copy(workbook)  # 将xlrd对象拷贝转化为xlwt对象
    new_worksheet = new_workbook.get_sheet(0)  # 获取转化后工作簿中的第一个表格
    for i in range(0, index):
        for j in range(0, len(value[i])):
            new_worksheet.write(i+rows_old, j, value[i][j])  # 追加写入数据，注意是从i+rows_old行开始写入
    new_workbook.save(path)  # 保存工作簿
    #print("xls格式表格【追加】写入数据成功！")
 
 
def read_excel_xls(path):
    workbook = xlrd.open_workbook(path)  # 打开工作簿
    sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
    worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
    for i in range(0, worksheet.nrows):
        for j in range(0, worksheet.ncols):
            print(worksheet.cell_value(i, j), "\t", end="")  # 逐行逐列读取数据



def main():
    

    book_name_xls = 'users.xls'    
    sheet_name_xls = 'sheet1'    
    field_title = [['OpenID', '姓名', '性别', '生日', '电话', '地址', '邮件']]

    
    write_excel_xls(book_name_xls, sheet_name_xls, field_title)

    datas = []
    i = 1

    while True:
        profile = fake.profile(fields=None, sex=None)
        row = [fake.md5(), fake.name(), profile['sex'], fake.date(pattern="%Y-%m-%d"), fake.phone_number(), profile['address'], profile['mail']]
        datas.append(row)
        #write_excel_xls_append(book_name_xls, [row])
        i += 1

        if i >= 7001:
            break

    
    write_excel_xls_append(book_name_xls, datas)

    print('done')

if __name__ == "__main__":
    main()