from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.get_json()
    text = data.get("text", "")
    
    # ⛔ 模擬結果（之後可以串 GPT）
    result = {
        "score": 42,
        "explanation": "這段新聞缺乏來源且誇大不實，可信度偏低。",
        "advice": "請查閱可信來源或事實查核平台。"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
