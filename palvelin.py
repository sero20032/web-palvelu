from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, crferfWorld!'

@app.route('/tulos')
def nayta_tulos():
    luku1 = request.args.get('luku1')
    luku2 = request.args.get('luku2')
    try:
        return "näiden lukjen summa on "+str(float(luku1)+float(luku2))
    except (ValueError, TypeError):
        return "Virheelliset luvut!"

@app.route('/seikkailu')
def nayta_laatikko_sivu():
    return """
<p>Laita tähän kaksi jännittävä laukua:
<form action="/tulos" enctype="application/x-www-urlencoded">
Eka luku:<input name=luku1 type=text> <br>
Toka luku : <input name=luku2 type=text> <br>
<input type=submit value="Tee jotain !">
</form>
"""


@app.route('/poks')
def poks():
    return 'Onnistuit sanomaan poks!'

if __name__ == '__main__':
    app.run(debug=True)
