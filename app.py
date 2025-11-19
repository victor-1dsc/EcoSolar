from flask import Flask, render_template, request, redirect, url_for
import csv
import os

app = Flask(__name__)
DATA_FILE = 'data/energy_offers.csv'

# Garante que a pasta e o arquivo existam
os.makedirs('data', exist_ok=True)
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['nome_produtor', 'energia_kwh', 'preco_kwh'])


# 🏠 Página inicial
@app.route('/')
def index():
    return render_template('index.html')


# 💡 Página de ofertas
@app.route('/offers')
def offers():
    offers_list = []
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            offers_list.append(row)
    return render_template('offers.html', offers=offers_list)


# ➕ Página para cadastrar nova oferta
@app.route('/new_offer', methods=['GET', 'POST'])
def new_offer():
    if request.method == 'POST':
        nome = request.form['nome_produtor']
        energia = request.form['energia_kwh']
        preco = request.form['preco_kwh']

        with open(DATA_FILE, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([nome, energia, preco])

        return redirect(url_for('offers'))  # corrigido

    return render_template('new_offer.html')


# ℹ️ Página sobre
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')


# 🚀 Inicializa o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)
