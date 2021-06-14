# 抓取資料進資料庫
import os, twstock, sqlite3
import pandas as pd
from tqdm import tqdm

# 利用os的path.join()將本檔案(__file__)與db.sqlite3做連結
# path.dirname()回傳db.sqlite3的路徑並透過sqlite3,connect()連接資料庫
conn = sqlite3.connect(os.path.join(os.path.dirname(os.path.dirname(__file__)),"db.sqlite3"))

# 選定十支股票，台積電、鴻海、聯發科、台塑化、中華電、台達電、富邦金、國泰金、南亞、聯電
tenStock = ["2330","2317","2454","6505","2412","2308","2881","2882","1303","2303"]

# 利用tqdm()顯示出進度條的效果
for i in tqdm(tenStock,ncols=100):

    # 利用twstock的Stock()來抓取十支股票之資訊
    # 將initial_fetch設為False，才可抓出超過一個月以上的資料
    everyStock = twstock.Stock(i,initial_fetch=False) 

    # 利用pandas的DataFrame()來結構化股票資料
    # 並透過twstock的fetch_from()抓取股票的歷史紀錄
    StockHistory = pd.DataFrame(everyStock.fetch_from(2010,1))

    # 利用pandas的to_sql()將儲存在DataFrame的資料存進資料庫中
    # if_exists="append"表示如果資料已存在將會將新的數值插入現有的資料
    # index=False將索引值刪除
    StockHistory.to_sql(i,conn,if_exists="append",index=False)

conn.commit()
conn.close()