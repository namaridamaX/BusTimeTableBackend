import tabula
import pandas as pd

PDF_Path = "PDF/bus.pdf"

def ReadPdf():
    # PDFファイルの読み取り（dfsの形式はList）
    dfs = tabula.read_pdf(PDF_Path, lattice=True, pages=1)
    return dfs

def ListDfs(dfs):
    df_list = [df.dropna(axis=1) for df in dfs]
    df_list = [df_list.pop(0), df_list.pop(0)]
    return df_list


