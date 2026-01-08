from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/process", methods=["POST"])
def process():
    name = request.form.get("name")
    return jsonify({"message": f"Hello {name}, data processed by Flask!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
