import os
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def main():
    return render_template("contacts.html")


if __name__ == '__main__':
    app.run()
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
