from flask import Flask, request
from flask.templating import render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        text = request.form.get("text")
        options = request.form.get("options")
        output = ""
        punc = [".", ",", "'", '"', "!","@", "#", "%", "$", "^", "&", "*", "(", ")", "/", "\\","}", "{", "|", "-","_","+", "=", "?", ":"]
        if options == "removepunc":
            for letter in text:
                if letter not in punc:
                    output+=letter
            return render_template("result.html", output = output)
        elif options == "cap":
            output = text.capitalize()
            return render_template("result.html", output = output)
        elif options == "upper":
            output = text.upper()
            return render_template("result.html", output = output)
        elif options == "lower":
            output = text.lower()
            return render_template("result.html", output = output)
    return render_template('index.html')




if __name__ == '__main__':
    app.run()