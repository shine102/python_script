from flask import Flask, render_template, request
import pandas as pd
import json

app = Flask(__name__)

SUCCESS = {
    "message" : "success"
}

FAIL = {
    "message" : "fail"
}

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/store", methods=["GET"])
def get_all():
    return json.dumps(retrieve_data())

@app.route("/store/<int:id>", methods=["GET"])
def get_by_id(id):
    data = retrieve_data()
    if (id >= len(data)):
        return "Invalid id"
    return json.dumps(retrieve_data()[id])

@app.route("/store", methods=["POST"])
def post():
    data = retrieve_data()
    new_product = request.get_json(silent=True, force=True)
    for i in range(len(data)):
        if data[i]["product"] == new_product["product"]:
            return json.dumps(FAIL)
    data.append(new_product)
    save_data(data)
    return json.dumps(SUCCESS)
    

@app.route("/store", methods=["PUT"])
def put():
    data = retrieve_data()
    change = request.get_json()
    for i in range(len(data)):
        if data[i]["product"] == change["product"]:
            data[i]["amount"] = change["amount"]
            save_data(data)
            return json.dumps(SUCCESS)
    return json.dumps(FAIL)

@app.route("/store/<int:id>", methods=["DELETE"])
def delete(id):
    data = retrieve_data()
    if (id >= len(data)):
        return json.dumps(SUCCESS)
    else:
        data.pop(id)
        save_data(data)
        return json.dumps(FAIL)
    

def retrieve_data():
    # read data from csv file
    df = pd.read_csv("store.csv")
    # convert to json
    data = df.to_json(orient="records")
    # convert to python dictionary
    data = json.loads(data)
    return data

def save_data(data):
    df = pd.DataFrame(data)
    df.to_csv("store.csv", index=False)


app.run(host='0.0.0.0', port=8099, debug=True)