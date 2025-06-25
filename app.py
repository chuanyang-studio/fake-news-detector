from flask import Flask, request, jsonify, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    # user prompt
    data = request.get_json()
    text = data.get("text", "")

    # system prompt
    system_prompt = '''請你扮演一位新聞事實查核員，根據下列新聞內容，判斷是否可能為假新聞，並給出以下格式的 JSON 回應： {
        "score": 0-100,
        "explanation": xxx,
        "advice": xxx
    }
    '''

    # make request
    endpoint = 'https://text.pollinations.ai/openai'
    messages = []
    messages.append({'role': 'system', 'content': system_prompt})
    messages.append({'role': 'user', 'content': text})
    
    resp = requests.post(endpoint, json={'messages': messages, 'model': 'openai', 'jsonMode': 'true'})
    result = resp.json()
    result = result['choices'][0]['message']['content']

    # get json response
    return json.loads(result)

if __name__ == "__main__":
    app.run(debug=False)
