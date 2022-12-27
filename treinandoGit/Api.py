Criando API em Python



replite.com

impot pandas as pd
from flask import Flask, jsonfy

app = Flask

#construir as funcionalidades
@app.route('/')
def home page():
return 'A API esta no ar'
@app.route('/pegarvendas')
def pegar vendas():
tabela = pd.read_csv('advertising.csv')
total_vendas = tabela['vendas'].sum()
resposta = {'total_vendas': total_vendas}
return jsonfy(resposta)
------------------------------------------------
na IDE

import request
link = 