import pandas as pd
from flask import Flask,jsonify
from flask_cors import CORS
from flask import request
import ChengePDF
import CheckTime



app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False #文字化けを解消してくれる？

@app.route('/', methods=["GET"])
def SendTable():

    dfs = ChengePDF.ReadPdf()
    List_Time = ChengePDF.ListDfs(dfs)
    bus_list = pd.concat([List_Time[0], List_Time[1]], axis=1)

    json_data = bus_list.to_json()

    return json_data

# @app.route('/', methods=["POST"])
# def CheckTime():
#
#     json_data = request.get_json()
#     SearchTime = json_data['RequestTime']
#
#     dfs = ChengePDF.ReadPdf()
#     List_Time = ChengePDF.ListDfs(dfs)
#     List_bus_time = CheckTime.timecheck(List_Time, 1, SearchTime)
#
#     return jsonify({'Titose':List_bus_time[0],'minami':List_bus_time[1],
#                     'kenkyu':List_bus_time[2],'honbu':List_bus_time[3]},)


if __name__ == '__main__':
    app.run()