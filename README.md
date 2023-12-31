# 遠大-自動購票機器人-Selenium
會製作這個起因是 112年10月28日 (六) 上午 11：00 的 YOASOBI ASIA TOUR 2023-2024 LIVE IN TAIPEI，

讓我們明白了人的速度終究是有極限的，

而做出此 Selenium 自動購票也並非真認為就能搶到票，

只是一時心血來潮，因此想用其搶票還請三思。

## 環境
* Python `3.8.18`
* Chrome Driver : [請依據自身瀏覽器下載相應版本並替換](https://googlechromelabs.github.io/chrome-for-testing/#stable)
* ddddocr : 請參考 **自動識別驗證碼** 部分

## 執行影片
[![IMAGE ALT TEXT](http://img.youtube.com/vi/xHZOzDat1ZQ/0.jpg)](https://www.youtube.com/watch?v=xHZOzDat1ZQ" "遠大-自動購票機器人-Selenium") 

## 使用說明 
### 操作步驟:
1. 目前僅能夠抓取[遠大購票網站](https://ticketplus.com.tw/)中的 **部分購票類型(如下圖所示)**。
2. 需自行於 [run.py](https://github.com/cyyW/TicketPLUS-Automatic_Ticketing_Bot-Selenium/blob/main/run.py) 輸入資料 : 帳號、密碼、**關鍵字設置(參考以下)**、購票張數
3. 執行程式後，將會進入遠大的首頁，等待其自動輸入會員後會進行等待
4. **請於遠大首頁自行點選你想要的活動即開始搶票**，而後就會根據你的關鍵字自動點選。
5. 直至填寫資料的頁面就算完成了。

<img src="https://github.com/cyyW/TicketPLUS-Automatic_Ticketing_Bot-Selenium/blob/main/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%202023-11-14%20033545.png" height="416px" width="861px" />
* <sup>目前僅能抓取如上圖的 選擇票種 頁面</sup>



### 關鍵字設置
* 頁面 : 頁面0(遠大首頁), **頁面1(購買門票)**, **頁面2(選擇票種)**；頁面1及頁面2須依據不同頁面分別設置關鍵字

* 關鍵字 : 於 [ ] 內輸入，文字需用 " " 包裹，以下分別講解 keyword(關鍵字) 及 keywordNo(排除字)。
1. keyword(關鍵字) : 以 逗號(,) 由左而右區隔關鍵字搜尋順序，並且 " " 內的關鍵字以 空格 間隔則表示 or(任一出現皆TRUE)。

   例1 : ["雙日","三日"] -> 先搜尋 雙日 ，再搜尋 單日。

   例2 : ["雙日 預售","三日"] -> 先搜尋(雙日 或 預售)，再搜尋單日。
   
2. keywordNo(排除字) : 透過 逗號(,) 間隔但不分順序，包含到任一排除字皆不取。
   
   例1 : ["兒童","身障","愛心","Restricted View"] -> 排除包含 (兒童 或 身障 或 愛心 或 Restricted View) 的項目。

## 程式設計
可參閱 [selenium_ticket_手稿](https://github.com/cyyW/TicketPLUS-Automatic_Ticketing_Bot-Selenium/blob/main/selenium_ticket_%E6%89%8B%E7%A8%BF.pdf)

其中包含大致的設計流程圖及功能設計的手寫草稿，雖然蠻亂的:joy:

## 自動識別驗證碼
### 使用元件 : 
带带弟弟OCR : [sml2h3/ddddocr](https://github.com/sml2h3/ddddocr)
### 安裝 :
```
pip install ddddocr
```
### 備註 :

安裝並執行後可能會發生以下問題。

` AttributeError: module 'PIL.Image' has no attribute 'ANTIALIAS' `

參考自 [此StackoverFlow](https://stackoverflow.com/questions/76616042/attributeerror-module-pil-image-has-no-attribute-antialias)，並用以下方法解決。
```
pip uninstall Pillow
pip install Pillow==9.5.0 
```

