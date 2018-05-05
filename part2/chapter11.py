import win32com.client
import pythoncom


class XASessionEventHandler:
    login_state = 0

    def OnLogin(self, code, msg):
        if code == "0000":
            print("로그인 성공")
            XASessionEventHandler.login_state = 1
        else:
            print("로그인 실패")


class XAQueryEventHandlerT1102:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT1102.query_state = 1


class XAQueryEventHandlerT8430:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8430.query_state = 1


class XAQueryEventHandlerT8413:
    query_state = 0

    def OnReceiveData(self, code):
        XAQueryEventHandlerT8413.query_state = 1

# -------------------------------
# Log in
# -------------------------------
id = "id"
passwd = "passwd"
cert_passwd = "cert_passwd"

instXASession = win32com.client.DispatchWithEvents("XA_Session.XASession", XASessionEventHandler)
instXASession.ConnectServer("hts.ebestsec.co.kr", 20001)
instXASession.Login(id, passwd, cert_passwd, 0, 0)

while XASessionEventHandler.login_state == 0:
    pythoncom.PumpWaitingMessages()

'''
num_account = instXASession.GetAccountListCount()
for i in range(num_account):
    account = instXASession.GetAccountList(i)
    print(account)
'''

'''
# -------------------------------
# t1102
# -------------------------------
instXAQueryT1102 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT1102)
instXAQueryT1102.ResFileName = "C:\\eBest\\xingAPI\\Res\\t1102.res"
instXAQueryT1102.SetFieldData("t1102InBlock", "shcode", 0, "078020")
instXAQueryT1102.Request(0)

while XAQueryEventHandlerT1102.query_state == 0:
    pythoncom.PumpWaitingMessages()

name = instXAQueryT1102.GetFieldData("t1102OutBlock", "hname", 0)
price = instXAQueryT1102.GetFieldData("t1102OutBlock", "price", 0)

print(name)
print(price)
'''

'''
# -------------------------------
# T8430
# -------------------------------
instXAQueryT8430 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8430)
instXAQueryT8430.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8430.res"

instXAQueryT8430.SetFieldData("t8430InBlock", "gubun", 0, 1)
instXAQueryT8430.Request(0)

while XAQueryEventHandlerT8430.query_state == 0:
    pythoncom.PumpWaitingMessages()

count = instXAQueryT8430.GetBlockCount("t8430OutBlock")
for i in range(5):
    hname = instXAQueryT8430.GetFieldData("t8430OutBlock", "hname", i)
    shcode = instXAQueryT8430.GetFieldData("t8430OutBlock", "shcode", i)
    expcode = instXAQueryT8430.GetFieldData("t8430OutBlock", "expcode", i)
    etfgubun = instXAQueryT8430.GetFieldData("t8430OutBlock", "etfgubun", i)
    print(i, hname, shcode, expcode, etfgubun)
'''

# -------------------------------
# T8413
# -------------------------------
instXAQueryT8413 = win32com.client.DispatchWithEvents("XA_DataSet.XAQuery", XAQueryEventHandlerT8413)
instXAQueryT8413.ResFileName = "C:\\eBEST\\xingAPI\\Res\\t8413.res"

instXAQueryT8413.SetFieldData("t8413InBlock", "shcode", 0, "078020")
instXAQueryT8413.SetFieldData("t8413InBlock", "gubun", 0, "2")
instXAQueryT8413.SetFieldData("t8413InBlock", "sdate", 0, "20180111")
instXAQueryT8413.SetFieldData("t8413InBlock", "edate", 0, "20180122")
instXAQueryT8413.SetFieldData("t8413InBlock", "comp_yn", 0, "N")

instXAQueryT8413.Request(0)

while XAQueryEventHandlerT8413.query_state == 0:
    pythoncom.PumpWaitingMessages()

count = instXAQueryT8413.GetBlockCount("t8413OutBlock1")
for i in range(count):
    date = instXAQueryT8413.GetFieldData("t8413OutBlock1", "date", i)
    open = instXAQueryT8413.GetFieldData("t8413OutBlock1", "open", i)
    high = instXAQueryT8413.GetFieldData("t8413OutBlock1", "high", i)
    low = instXAQueryT8413.GetFieldData("t8413OutBlock1", "low", i)
    close = instXAQueryT8413.GetFieldData("t8413OutBlock1", "close", i)
    print(date, open, high, low, close)
