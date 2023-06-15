from flask import Flask, request, json
import main as ia

app = Flask(__name__)
@app.route("/", methods=['GET'])
def flask():
    content = json.loads(request.data)
    v = json.dumps(content['variance'])
    c = json.dumps(content['curtosis'])
    s = json.dumps(content['skewness'])
    e = json.dumps(content['entropy'])
    predict = ia.user_entries(v, c, s, e)
    return str(predict)
  
if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0', port=5000)