from flask import Flask, request, jsonify, render_template
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
Чи Монголын химийн ЭЕШ-д бэлтгэдэг чадварлаг багш.

Дүрэм:
1. Алхамчилж тайлбарла
2. Томьёо ашигла
3. Жишээ өг
4. Эцэст нь товч дүгнэлт бич
5. Хариуг ойлгомжтой байлга
"""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
     return jsonify({"reply": "TEST OK"})
    
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ]
    )

    reply = response.choices[0].message.content

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
