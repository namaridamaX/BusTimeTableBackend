import datetime
import os.path

import pytz
import tabula
import pandas as pd
import PyPDF2
from datetime import datetime, timedelta, timezone

PDF_Path = "PDF/bus.pdf"

def ReadPdf():
    # PDFファイルの読み取り（dfsの形式はList）
    dfs = tabula.read_pdf(PDF_Path, lattice=True, pages=1)
    return dfs

def ListDfs(dfs):
    df_list = [df.dropna(axis=1) for df in dfs]
    df_list = [df_list.pop(0), df_list.pop(0)]
    return df_list

def SerchPdf():
    FullWidthDigits = "０１２３４５６７８９"
    HalfWidthDigits = "0123456789"
    conv_map = str.maketrans(FullWidthDigits,HalfWidthDigits)
    # dt_now = datetime.now(pytz.timezone('Asia/Tokyo')) #現在の時間


    if (os.path.getsize("PDF") == 0): return True

    with open("PDF/bus.pdf","rb") as f:
        reader = PyPDF2.PdfReader(f)
        page = reader.pages[0] #PyPDF2がversion3.0に変更によりこっちを使うようになりました
        pdf_text = page.extract_text() #PyPDF2がversion3.0に変更によりこっちを使うようになりました

        # 運行期間が書かれている日付を抽出
        target = '～'
        idx = pdf_text.find(target)
        s = pdf_text[idx+1:idx+7]

        dayword = '日'
        ldx = s.find(dayword)
        chenged_text = s[:ldx + 1]

        #textの全角数字を半角に変換
        chenged_text = chenged_text.translate(conv_map)
        str_year = str(dt_now.year)
        chenged_text = str_year + "年" + chenged_text

        #日付をdatetime型に変換
        dummy_date = "2022年12月12日"
        #bus_pdf_date = datetime.strptime(chenged_text,'%Y年%m月%d日')
        bus_pdf_date = datetime.strptime(dummy_date, '%Y年%m月%d日')

        #タイムゾーンを付与してイギリス時間から日本時間へ
        jst_timedelta = timedelta(hours=+9)
        jst = timezone(jst_timedelta, 'JST')
        bus_pdf_date = bus_pdf_date.astimezone(jst)

        if (bus_pdf_date < dt_now):
            return True

        return False




