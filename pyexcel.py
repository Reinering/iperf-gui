# -*- coding: utf-8 -*-

import win32com.client as wc
import os
import pythoncom
import datetime



# excel 数值转文本
def converText(data):
    if data:
        return '\'' + data
    return data

# datetime to string
def datetime_toString(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def writeExcel(filename, sheet, args):
    """
    :param args: 数据类型：[[row, data],[row1, data1]]

    :return:
    """
    # subprocess.run("taskkill -f -im EXCEL*", shell=True)
    myExcel = None
    mySheet = None
    try:
        # os.system("taskkill -f -im EXCEL*")
        pythoncom.CoInitialize()  # win32com初始化
        excel = wc.Dispatch("Excel.Application")
        print(type(excel))
        # excel.DisplayAlerts = 0
        excel.Visible = False
        if os.path.exists(filename):
            myExcel = excel.Workbooks.Open(filename.replace(u'/', u'\\'), False)
        else:
            myExcel = excel.Workbooks.Add()
            myExcel.SaveAs(filename)
        try:
            mySheet = myExcel.Sheets(sheet)
        except Exception as e:
            print(e)
        if mySheet == None:
            mySheet = myExcel.Worksheets.Add()
            mySheet.Name = sheet
        # else:
        #     mySheet.Rows(row).Delete()
        for arg in args:
            if arg:
                row = arg[0]
                i = 1
                for ar in arg[1:]:

                    if type(ar) == datetime.datetime:
                        mySheet.Cells(row, i).Value = datetime_toString(ar)
                    elif type(ar) == str:
                        mySheet.Cells(row, i).Value = ar
                    else:
                        mySheet.Cells(row, i).Value = str(ar)
                    i += 1
        myExcel.Save()
    except Exception as e:
        # print("ExcelError", e)
        raise Exception
    finally:
        try:
            myExcel.Close(SaveChanges=0)
            excel.Quit()
            del(excel)
        except Exception as e:
            raise Exception

