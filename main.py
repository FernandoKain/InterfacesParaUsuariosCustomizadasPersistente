# pip install PySimpleGUI

import PySimpleGUI as sg


class TelaPython:
    def __init__(self):
        # sg.theme_previewer() # Para visualizar todos os temas basta descomentar o código desta linha
        sg.change_look_and_feel('DarkGreen5')
        # Para mais é só acessar: https://www.geeksforgeeks.org/themes-in-pysimplegui/

        # Layout
        layout = [
            [sg.Text('Nome', size=(5,0)), sg.Input(size=(40,0), key='nome')], # Primeiro Campo da Janela
            [sg.Text('Idade', size=(5,0)), sg.Input(size=(15,0), key='idade')], # Segundo Campo da Janela
            [sg.Text('Quais provedores de e-mail são aceitos?')],
            [sg.Checkbox('Gmail', key='gmail'), sg.Checkbox('Outlook', key='outlook'), sg.Checkbox('Yahoo', key='yahoo')],
            [sg.Text('Aceita cartão?')],
            [sg.Radio('Sim', 'cartoes', key='aceitaCartao'),sg.Radio('Não', 'cartoes', key='naoAceitaCartao')],
            [sg.Slider(range=(0,255), default_value=0, orientation='h', size=(15, 20), key='sliderVelocidade')],
            [sg.Button('Enviar Dados')], # Bottão para Enviar os Dados
            [sg.Output(size=(30, 20))]

        ]
        # Janela
        self.janela = sg.Window('Dados do Usuário').layout(layout) # Cabeçalho da Janela


    def Iniciar(self):
        while True:
            # Extraindo dados agora constantemente
            self.button, self.values = self.janela.Read()
            nome = self.values['nome']
            idade = self.values['idade']
            aceita_gmail = self.values['gmail']
            aceita_outlook = self.values['outlook']
            aceita_yahoo = self.values['yahoo']
            aceita_cartao = self.values['aceitaCartao']
            nao_aceita_cartao = self.values['naoAceitaCartao']
            velocidade_script = self.values['sliderVelocidade']
            print(f'nome: {nome}')
            print(f'idade: {idade}')
            print(f'aceita gmail: {aceita_gmail}')
            print(f'aceita outlook: {aceita_outlook}')
            print(f'aceita yahoo: {aceita_yahoo}')
            print(f'Aceita cartão: {aceita_cartao}')
            print(f'Não aceita Cartão: {nao_aceita_cartao}')
            print(f'Velocidade atual do script: {velocidade_script}')


tela = TelaPython()
tela.Iniciar()
