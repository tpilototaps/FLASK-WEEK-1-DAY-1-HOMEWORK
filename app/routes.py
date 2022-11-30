from app import app
from flask import render_template

@app.route('/')
@app.route('/Index')
def home():
    return render_template('index.html')

@app.route('/Favorite5')
def favorite5():
    rides = ('Lamborgini Huracan Perfomate', 'Lamborghini Sesto Elemento', 'Bugatti Noir Voiture', 'Ferrari LeFerrari', 'Porsche GT3 RS')
    return render_template('favorite5.html', top5 = rides)