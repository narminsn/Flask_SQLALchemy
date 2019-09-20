from flask import Flask, jsonify,request
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)
url="https://www.pexels.com/search/forest/"
@app.route("/")
def helloWorld():
    search=request.args.get("q")

    url="https://www.pexels.com/search/" + search

    data=requests.get(url)
    parser=BeautifulSoup(data.text,"html.parser")

    div=parser.find("div", {"class": "photos"})

    return jsonify({
        # "code": str(div)
        "code":data.text
    })

app.run(debug=True, host='0.0.0.0', port=5001)
