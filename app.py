from flask import Flask,jsonify
import pandas as pd


app = Flask(__name__)


@app.route('/all',methods = ["GET"])
def india_indices_sensex():
    df = pd.read_html('https://www.moneycontrol.com/markets/indian-indices')
    scr = df[0]
    to = len(scr)-1
    all_json = []
    for i in range(to):
        all_json.append({"company":scr[0][i],
                        "LTP":scr[1][i],
                        "%Charge":scr[2][i],
                        "Volume":scr[3][i],
                        "Buy Price":scr[4][i],
                        "Sell Price":scr[5][i],
                        "Buy Qty":scr[6][i],
                        "Sell Qty":scr[7][i]})
    return jsonify(all_json), 200

if __name__ == "__main__":
    app.run(debug=True)