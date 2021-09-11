from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/ping", methods=['GET'])
def ping():
    return jsonify({"result":"pong"})
    

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3333)
