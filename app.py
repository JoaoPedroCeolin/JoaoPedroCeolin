from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

ips_visitantes = set()
cliques = 0
recorde_global = 0

@app.route("/")
def home():
    ip = request.remote_addr

    if ip not in ips_visitantes:
        ips_visitantes.add(ip)

    return render_template(
        "index.html",
        visitas=len(ips_visitantes),
        cliques=cliques,
        recorde=recorde_global
    )

@app.route("/click", methods=["POST"])
def click():
    global cliques
    cliques += 1
    return jsonify({"cliques": cliques})

@app.route("/recorde", methods=["POST"])
def recorde():
    global recorde_global

    dados = request.get_json()
    pontos = dados.get("pontos", 0)

    if pontos > recorde_global:
        recorde_global = pontos

    return jsonify({"recorde": recorde_global})

@app.route("/aura")
def aura():
    return render_template("aura.html")

@app.route("/snake")
def snake():
    return render_template("snake.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)