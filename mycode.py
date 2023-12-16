from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import sys

def ticket_plus (phone,possword,keyword_1s,keywordNo_1s,keyword_2s,keywordNo_2s,press):
    options = Options()
    options.chrome_executable_path ="C:/Users/USER/Desktop/selenium_ticket/TicketPLUS-Automatic_Ticketing_Bot-Selenium/chromedriver.exe"

    # 1. 事前準備 (頁面0)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://ticketplus.com.tw/")


    wait = WebDriverWait(driver, 5)
    element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"v-btn__content")))

    actions = ActionChains(driver)

    # 點擊會員登入
    member_button = driver.find_element(By.CLASS_NAME,"v-btn__content")
    actions.move_to_element(member_button).click().perform()



    # 輸入帳密並登入
    for i in range(2):
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "input-tel__input")))

        number = driver.find_element(By.CLASS_NAME, "input-tel__input")  
        actions.move_to_element(number).click().send_keys(phone).perform()

        possword_button = driver.find_element(By.CLASS_NAME,"v-text-field__slot")
        actions.move_to_element(possword_button).click().send_keys(possword).perform()

        wait = WebDriverWait(driver, 3)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"nextBtn.mt-2.v-btn.v-btn--block.v-btn--has-bg.theme--light.v-size--x-large.white")))

        login = driver.find_element(By.CLASS_NAME, "nextBtn.mt-2.v-btn.v-btn--block.v-btn--has-bg.theme--light.v-size--x-large.white")
        actions.move_to_element(login).click().perform()




    # 2. 選擇場次 (頁面一)
    while True :
        
        try:  # 等待進入頁面
            wait = WebDriverWait(driver, 3600)
            element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v-tab.v-tab--active")))
        except WebDriverException as e:  # 捕获WebDriverException异常，这包括了各种Selenium异常，如超时、元素找不到等
            print(f"页面加载时发生错误: {e}")
            driver.refresh()
            continue
        
        #識別並關閉廣告
        try:
            ads = driver.find_element(By.CLASS_NAME, "text-center.pa-5.v-card.v-sheet.theme--light")
            actions.send_keys(Keys.ESCAPE).perform()
            print("關閉廣告")
        except:
            print("無廣告")

        # 點擊購票-根據關鍵字取得點擊優先順序
        sesstions = driver.find_elements(By.CLASS_NAME, "sesstion-item")
        events = driver.find_elements(By.CLASS_NAME, "d-flex.text-left.font-weight-bold.text-regular.py-2.is-word-break.col-sm-12.col-md-4.col-12.align-self-center")
        k = 0
        for keyword in keyword_1s: # 依關鍵字
            break_all = False
            continue_get = False
            keywords_list = keyword.split()
            orders = []
            k = k + 1
            e = 0
            for event in events:  # 搜尋場次排序
                e = e + 1
                even_name = event.get_attribute('textContent')
                if any(keyword_str in even_name for keyword_str in keywords_list) and any(keywordNo not in even_name for keywordNo in keywordNo_1s): # 場次滿足關鍵字搜尋條件
                    print(even_name)
                    print(e)
                    orders.append(e)
                elif len(events) == e and len(orders) == 0 and len(keyword_1s) == k : # 關鍵字及場次皆已循完，皆未找到
                    print("場次皆未找到，停止程序 1 小時")
                    sys.exit()
                    # time.sleep(3600)
                elif len(events) == e and len(orders) == 0 : # 活動循完表單沒東西，跳回繼續下一個關鍵字
                    print("此關鍵字搜尋無果")
                    continue_get =True
            if continue_get : 
                continue


            sesstions = driver.find_elements(By.CLASS_NAME, "sesstion-item")
            o = 0
            for order in orders :
                o = o + 1
                s = 0
                for sesstion in sesstions :
                    s = s + 1
                    if s == order :
                        try :
                            BookTicket = sesstion.find_element(By.CLASS_NAME, "v-btn__content")
                            print("點擊按鈕 :", BookTicket.get_attribute('textContent'))
                            actions.move_to_element(BookTicket).click().perform()
                            break_all = True
                            break
                        except:
                            print("此票賣完")

                        if len(keyword_1s) == k and len(orders) == o and len(sesstions) == s :
                            print("所選票卷皆已賣完 : 重整頁面")
                            driver.refresh()              
                if break_all:
                    break_all = True
                    break
            if break_all:
                break_all = True
                break
        if break_all:
            break_all = True
            break





# 3. 選擇票型 (頁面二)
    while True :
        
        # 等待進入頁面二
        try:  
            wait = WebDriverWait(driver, 3600)
            element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "font-weight-medium.py-3.col-sm-6.col-9.align-self-center.pl-6.d-flex.align-center")))
        except WebDriverException as e:  # 捕获WebDriverException异常，这包括了各种Selenium异常，如超时、元素找不到等
            print(f"页面加载时发生错误: {e}")
            driver.refresh()
            continue

        # 點擊購票-根據關鍵字取得點擊優先順序
        tickets = driver.find_elements(By.CLASS_NAME, "font-weight-medium.py-3.col-sm-6.col-9.align-self-center.pl-6.d-flex.align-center")
        k = 0
        for keyword in keyword_2s: # 依關鍵字
            break_all = False
            continue_get = False
            keywords_list = keyword.split()
            order2s = []
            k = k + 1
            t = 0
            for ticket in tickets:  # 搜尋場次排序
                t = t + 1
                ticket_name = ticket.get_attribute('textContent')
                if any(keyword_str in ticket_name for keyword_str in keywords_list) and any(keywordNo not in ticket_name for keywordNo in keywordNo_2s): # 場次滿足關鍵字搜尋條件
                    print(ticket_name)
                    print(t)
                    order2s.append(t)
                elif len(tickets) == t and len(order2s) == 0 and len(keyword_2s) == k : # 關鍵字及場次皆已循完，皆未找到
                    print("場次皆未找到，停止程序 1 小時")
                    sys.exit()
                    # time.sleep(3600)
                elif len(tickets) == t and len(order2s) == 0 : # 活動循完表單沒東西，跳回繼續下一個關鍵字
                    print("此關鍵字搜尋無果")
                    continue_get =True

            if continue_get : 
                continue


            types = driver.find_elements(By.CLASS_NAME, "row.py-1.py-md-4.rwd-margin.no-gutters.text-title")
            o = 0
            for order2 in order2s :
                o = o + 1
                s = 0
                for type  in types :
                    s = s + 1
                    if s == order2 :
                        try :
                            print("開始點擊")
                            plus_btn = type.find_element(By.CLASS_NAME, "v-btn.v-btn--fab.v-btn--has-bg.v-btn--round.theme--light.v-size--x-small.light-primary-2")
                            for i in range (press) :             
                                actions.click(plus_btn).perform()
                            break_all = True
                            break
                        except:
                            print("此票賣完")

                        if len(keyword_2s) == k and len(order2s) == o and len(types) == s :
                            print("所選票卷皆已賣完 : 重整頁面")
                            driver.refresh()              
                if break_all:
                    break_all = True
                    break
            if break_all:
                break_all = True
                break
        if break_all:
            break_all = True
            break

    # 驗證碼 -> 點擊下一步 
    while True :
        # 抓取驗證碼圖
        import cairosvg

        svg_element = driver.find_element(By.CLASS_NAME, "captcha-img")
        svg_content = svg_element.get_attribute("outerHTML")

        # 在SVG内容前添加一个有效的<svg>根元素
        svg_with_root = f'<svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" height="75" width="213" viewBox="0 0 213 75">{svg_content}</svg>'

        svg_save_path = "C:/Users/USER/Desktop/selenium_ticket/TicketPLUS-Automatic_Ticketing_Bot-Selenium/png/photo.svg"
        png_save_path = "C:/Users/USER/Desktop/selenium_ticket/TicketPLUS-Automatic_Ticketing_Bot-Selenium/png/photo.png"

        with open(svg_save_path, "w", encoding="utf-8") as f:
            f.write(svg_with_root)

        cairosvg.svg2png(url=svg_save_path, write_to=png_save_path, output_width=213, output_height=75) # png_save_path (圖檔名)

        # 圖片上白背景
        from PIL import Image
        input_image = Image.open(png_save_path)

        # 創建白色背景圖象，大小與圖相同
        width, height = input_image.size
        output_image = Image.new("RGB", (width, height), "white")

        # 兩圖合併
        output_image.paste(input_image, (0, 0), input_image)
        output_image.save(png_save_path)


        # 識別驗證碼 (帶帶弟弟OCR)
        import ddddocr
        ocr = ddddocr.DdddOcr(beta=True)

        with open(png_save_path, 'rb') as f:
            image = f.read()

        res = ocr.classification(image)

        print("驗證碼 :")
        print(res)


        # 輸入驗證碼
        captcha_code = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/div/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/input")
        captcha_code.send_keys(res)
        
        # 點擊 下一步
        next_btn = driver.find_element(By.CLASS_NAME, "nextBtn.v-btn.v-btn--block.v-btn--has-bg.theme--light.elevation-0.v-size--x-large")
        driver.execute_script("arguments[0].click();", next_btn)

        # 等待進入頁面
        try:  
            wait = WebDriverWait(driver, 300)
            element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "v-messages__message")))
        except WebDriverException as e:  # 捕获WebDriverException异常，这包括了各种Selenium异常，如超时、元素找不到等
            print(f"頁面發生錯誤: {e}")
            driver.refresh()
            continue

        # 驗證碼輸入錯誤
        code_wrong = driver.find_element(By.CLASS_NAME, "v-messages__message")
        print("錯誤訊息 :", code_wrong.get_attribute('textContent'))






# text-center bg-tranparent-yellow pa-3 text-title font-weight-bold rwd-margin is-word-break

# row py-1 py-md-4 rwd-margin no-gutters text-title
    # 票名 :
    # font-weight-medium py-3 col-sm-6 col-9 align-self-center pl-6 d-flex align-center
    # font-weight-medium py-3 col-sm-6 col-9 align-self-center pl-6 d-flex align-center

    # 票價 :
    # text-center col-sm-3 col-md-3 col-3 align-self-center px-4 font-weight-bold

    # +號 按鈕 :
    # v-btn v-btn--fab v-btn--has-bg v-btn--round theme--light v-size--x-small light-primary-2
    # v-btn v-btn--fab v-btn--has-bg v-btn--round theme--light v-size--x-small light-primary-2


# <svg xmlns:xlink="http://www.w3.org/1999/xlink" xmlns="http://www.w3.org/2000/svg" height="75" width="213" viewBox="0,0,213,75"></svg>

# input-52

# v-input v-input--hide-details v-input--is-label-active v-input--is-dirty theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined v-text-field--placeholder
# v-input v-input--has-state theme--light v-text-field v-text-field--is-booted v-text-field--enclosed v-text-field--outlined v-text-field--placeholder error--text
# v-input.v-input--has-state.theme--light.v-text-field.v-text-field--is-booted.v-text-field--enclosed.v-text-field--outlined.v-text-field--placeholder.error--text
# 下一步 :
# nextBtn v-btn v-btn--block v-btn--has-bg theme--light elevation-0 v-size--x-large

# /html/body/div/div[1]/div/div/main/div/div/div[2]/div[3]/div/div[2]/div[3]/div/div[1]/div[2]/div/div[1]/div/input

# 此欄位為必填

# v-text-field__details
# v-messages theme--light error--text
# v-messages__wrapper
# v-messages__message

# /html/body/div/div[1]/div/div/main/div/div/div[4]/div[1]/div[2]/div[1]
# /html/body/div/div[1]/div/div/main/div/div/div[4]/div[1]/div[3]/div