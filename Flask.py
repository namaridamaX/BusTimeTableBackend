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

    Selenium_PDF.Selenium_pdf()
    dfs = ChengePDF.ReadPdf()
    List_Time = ChengePDF.ListDfs(dfs)
    bus_list = pd.concat([List_Time[0], List_Time[1]], axis=1)

    json_data = bus_list.to_json()

    return json_data

if __name__ == '__main__':
    app.run()