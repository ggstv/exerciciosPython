import requests
from tkinter import *
def pegar_cotacoes():
    req = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
    req_dic = req.json()

    cotacao_dolar = req_dic["USDBRL"]['bid']
    cotacao_euro = req_dic["EURBRL"]['bid']
    cotacao_btc = req_dic["BTCBRL"]['bid']
    
    texto = f'''
    Dólar = {cotacao_dolar}
    Euro = {cotacao_euro}
    BTC = {cotacao_btc}'''
    texto_cotacoes["text"] = texto




janela = Tk()
janela.title('Cotação Moedas')

texto_orientacao = Label(janela, text='Clique no botão para ver as cotações das moedas.')
texto_orientacao.grid(column=0,row=0, padx=10, pady=10)

botao = Button(janela, text='Buscar Cotações', command=pegar_cotacoes)
botao.grid(column=0,row=1, padx=10, pady=10)

texto_cotacoes = Label(janela, text='')
texto_cotacoes.grid(column=0,row=2, padx=10, pady=10)
janela.mainloop()