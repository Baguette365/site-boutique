from flask import Flask, render_template

app = Flask("le cottage floral")

@app.route('/')
def main():
    return render_template('main.html')