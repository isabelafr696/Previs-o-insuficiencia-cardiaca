import cloudpickle
import numpy as np
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():

  int_features = [int(x) for x in request.form.values()]
  final_features = [np.array(int_features)]

 


  predicao = model.predict(final_features)
 
  return render_template('predicao.html', predicao=predicao[0])
  
  
app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)

# git add .

# git commit -m "nomenovo"
# git push
