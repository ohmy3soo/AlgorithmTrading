import win32com.client

'''
explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True
'''

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
'''
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")
ws.Cells(1,1).Value = "hello world"
wb.SaveAs('c:\\Users\\kihunahn\\Desktop\\test.xlsx')
excel.Quit()
'''
wb = excel.Workbooks.Open('c:\\Users\\kihunahn\\Desktop\\test.xlsx')
ws = wb.ActiveSheet
'''
print(ws.Cells(1,1).Value)
excel.Quit()
'''

ws.Cells(1,2).Value = "is"
ws.Range("C1").Value = "good"
ws.Range("C1").Interior.ColorIndex = 10     # 0 ~ 56
ws.Range("A2:C2").Interior.ColorIndex = 27


