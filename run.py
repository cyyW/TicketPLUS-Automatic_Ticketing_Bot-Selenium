from mycode import ticket_plus

'''  會員登入  '''
# 帳號 :
phone = "988221609"
# 密碼 :
possword = "wygHiq-0xacfu-mojjaq"
''''''

'''  關鍵字(頁1)  '''
# 搜尋字眼 :
keyword_1s = ["雙日","三日"]
# 排除字眼 :
keywordNo_1s = ["兒童","身障","愛心","Restricted View"]
''''''

'''  關鍵字(頁2)  '''
# 搜尋字眼 :
keyword_2s = ["預售票"]
# 排除字眼 :
keywordNo_2s = ["兒童","身障","愛心","Restricted View"]
''''''

'''  選擇票數  '''
press = 2 
''''''


ticket_plus(phone,possword,keyword_1s,keywordNo_1s,keyword_2s,keywordNo_2s,press)