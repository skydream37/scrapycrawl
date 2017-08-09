crapy為爬取商品資訊的爬蟲，裡面有三隻，分別可以爬取大創，美華泰，以及寶雅商品資料，包括商店名稱，商品名稱，商品價格，商品銷售數，運費、商品連結、爬取時間等資訊

另外做了一些防反爬蟲處理
1.	關閉robot.txt
2.	關閉cookie
3.	使用user agent
4.	使用proxy(專題製作時使用西刺代理爬取做成IP POOL，後來使用crawlera代理服務，這邊DEMO上暫時關閉改成本地ip)

daiso大創百貨
mht美華泰
poya寶雅
安裝完 scrapy後(pip install scrapy)
在scrapy.cfg同層目錄開啟terminal，依照需求輸入以下指令，
scrapy crawl daiso
開啟爬蟲，同步將資料寫入資料庫，這邊暫時使用sqlite
scrapy crawl daiso -o daiso.json -t json 
將爬蟲資料寫出成json檔
scrapy crawl daiso -o daiso.csv -t csv
將爬蟲資料寫出成csv檔


104R是剛開始學python對104人力銀行以thread進行爬取的code
google_trends是爬取js動態生成網頁，採用selenium爬取頁面的code
可依照需求納入scrapy中進行爬蟲程式自動化整合

# scrapycrawl
# scrapycrawl
