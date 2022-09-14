
# Consultando Cotação e Clima

# API fornece cotação

#importando a biblioteca que trabalha com a API
import requests

#importando a biblioteca que estrutura dados em formato de texto 
import json


# Armazenando a API de moedas numa variável 
requisicao = requests.get(' https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')

cotacao = json.loads(requisicao.text)

# Imprimindo a alta do dolar (Repare que eu utilizei para acessar o dicionário(valor da chave) do dolar e dps o valor da chave high)
print(cotacao['USDBRL']['high'])


print('Alta do Dolar :',cotacao['USDBRL']['high'])
print('Alta do Euro :',cotacao['EURBRL']['high'])
print('Alta do Bitcoin :',cotacao['BTCBRL']['high'])



