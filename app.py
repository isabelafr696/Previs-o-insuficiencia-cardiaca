import cloudpickle
from flask import Flask, render_template, request
import numpy as np

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('\template\Predict Churn.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
    int_features=[int(x) for x in request.form.values()]
    genero = request.form['genero']
    idade = request.form['idade']
    telefone= request.form['telefone']
    suporte= request.form['suporte']
    streaming= request.form['streaming']
    predicao = model.predict([genero],[idade],[telefone],[suporte],[streaming])
    return render_template('resposta.html', predicao=predicao[0])

app.run(debug=True)





