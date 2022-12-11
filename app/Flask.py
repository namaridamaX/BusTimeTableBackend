import pandas as pd
from flask import Flask
from flask_cors import CORS
import ChangePDF
import Selenium_PDF



app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/', methods=["GET"])
def SendTable():

    #バスPDFが期間外の場合のみseleniumを用いてPDFを更新
    if(ChangePDF.SerchPdf()):
        print("true")
        Selenium_PDF.Selenium_pdf() #seleniumを用いてPDFfileを読み取る <- 毎回行うと時間がかかる？

    dfs = ChangePDF.ReadPdf()
    List_Time = ChangePDF.ListDfs(dfs)
    bus_list = pd.concat([List_Time[0], List_Time[1]], axis=1)

    json_data = bus_list.to_json()

    return json_data

@app.route('/hello')
def hello():
    return 'hello'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
