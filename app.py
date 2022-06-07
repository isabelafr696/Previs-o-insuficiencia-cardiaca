importar  cloudpickle
from  flask  import  Flask , render_template , request

com  open ( 'model.pkl' , 'rb' ) como  file_in :
  modelo  =  cloudpickle . carregar ( arquivo_in )

app  =  Flask ( __name__ )

@aplicativo . _ rota ( '/' )
def  página inicial ():
  return  render_template ( 'homepage.html' , nome = 'Fulano' )

@aplicativo . _ route ( '/predicao' , métodos = [ 'POST' ])
def  predicao ():
  Gênero  =  int ( request . form [ 'Gender' ])
  Senior_Citizen  =  int ( request . form [ 'Senior_Citizen' ])
  Phone_Service  =  int ( request . form [ 'Phone_Service' ])
  Tech_Support  =  int ( request . form [ 'Tech_Support' ])
  Streaming_Movies  =  int ( request . form [ 'Streaming_Movies' ])
  Contrato  =  int ( request . form [ 'Contract' ])
  Payment_Method  =  int ( request . form [ 'Payment_Method' ])
  predicao  =  modelo . prever ([ 'Gênero' ])
  predicao  =  modelo . prever ([ 'Senior_Citizen' ])
  predicao  =  modelo . prever ([ 'Phone_Service' ])
  predicao  =  modelo . prever ([ 'Tech_Support' ])
  predicao  =  modelo . prever ([ 'Streaming_Movies' ])
  predicao  =  modelo . prever ([ 'Contrato' ])
  predicao  =  modelo . prever ([ 'Payment_Method' ])
  return  render_template ( 'predicao.html' , predicao = predicao [ 0 ])
  
  
aplicativo . execute ( debug = True )

# pip install -r requirements.txt (instala como bibliotecas)
# python app.py (para executar)

#git adicionar.

# git commit -m "nomenovo"
#git push
