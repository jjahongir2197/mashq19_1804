from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def min_number():

    if request.method == "POST":

        n1 = int(request.form["n1"])
        n2 = int(request.form["n2"])
        n3 = int(request.form["n3"])

        min_num = min(n1, n2, n3)

        return f"Eng kichik son: {min_num}"

    return render_template("index.html")

app.run(debug=True)
