from flask import Flask, render_template, url_for

app = Flask(__name__)
app.debug = True


@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/categories_laptops_%uygfr%HFvk')
def kategorie():
    return render_template('kategorie.html')


if __name__ == '__main__':
    app.run(debubg=True)
