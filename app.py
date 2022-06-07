import cloudpickle
from flask import Flask, render_template, request

with open('model.pkl', 'rb') as file_in:
  model = cloudpickle.load(file_in)

app = Flask(__name__)

@app.route('/')
def homepage():
  return render_template('homepage.html', nome='Fulano')

@app.route('/predicao', methods=['POST'])
def predicao():
  age = int(request.form['age'])
  anaemia = int(request.form['anaemia'])
  creatinine_phosphokinase = int(request.form['creatinine_phosphokinase'])
  diabetes = int(request.form['diabetes'])
  ejection_fraction = int(request.form['ejection_fraction'])
  high_blood_pressure = int(request.form['high_blood_pressure'])
  platelets = int(request.form['platelets'])
  serum_creatinine = int(request.form['serum_creatinine'])
  serum_sodium = int(request.form['serum_sodium'])
  sex = int(request.form['sex'])
  smoking = int(request.form['smoking'])
  time = int(request.form['time'])
  predicao = model.predict(['age'])
  predicao = model.predict(['anaemia'])
  predicao = model.predict(['creatinine_phosphokinase'])
  predicao = model.predict(['diabetes'])
  predicao = model.predict(['ejection_fraction'])
  predicao = model.predict(['high_blood_pressure'])
  predicao = model.predict(['platelets'])
  predicao = model.predict(['serum_creatinine'])
  predicao = model.predict(['serum_sodium'])
  predicao = model.predict(['sex'])
  predicao = model.predict(['smoking'])
  predicao = model.predict(['time'])
  return render_template('predicao.html', predicao=predicao[0])
  
  
app.run(debug=True)

# pip install -r requirements.txt (instala as bibliotecas)
# python app.py (para executar)

# git add .

# git commit -m "nomenovo"
# git push
