from flask import Flask, render_template, request


import mode

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])


def model():
    if request.method == 'POST':
        text = request.form['english']
        spanish = mode.translate(text)
        print(spanish[:-4])
        spa = spanish[:-4]

    return render_template("flask_index.html", text = spa)


# @app.route("/sub", methods = ['POST'])
# def submit():
#     if request.method == 'POST':
#         name = request.form["username"]

#     return render_template("sub.html", n = name)



if __name__ == "__main__":
    app.run(debug = True)