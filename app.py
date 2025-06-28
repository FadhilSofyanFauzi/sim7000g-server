from flask import Flask, request

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def data():
    suhu = request.args.get('suhu', '')
    humi = request.args.get('humi', '')
    with open("log.txt", "a") as f:
        f.write(f"Suhu: {suhu}, Humi: {humi}\n")
    return "OK"
