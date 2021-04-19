from flask import Flask
import pandas as pd
import os

app = Flask(__name__)

@app.route("/api_train")
def api_download():
    os.chdir("../assets")
    data_train = pd.read_csv("train.csv")
    return data_train.to_json()


@app.route("/api_test")
def api_test():
    os.chdir("../assets")
    data_test = pd.read_csv("test.csv")
    return data_test.to_json()



if __name__ == "__main__":
    app.run(debug=True)