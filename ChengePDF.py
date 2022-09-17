import tabula
import pandas as pd

PDF_Path = "PDF/2022年度シャトルバス時刻表（8.29～9.pdf"

def ReadPdf():
    # PDFファイルの読み取り（dfsの形式はList）
    dfs = tabula.read_pdf("PDF/2022年度シャトルバス時刻表（8.29～9.pdf", lattice=True, pages=1)
    return dfs

def ListDfs(dfs):
    df_list = [df.dropna(axis=1) for df in dfs]
    df_list = [df_list.pop(0), df_list.pop(0)]
    return df_list


