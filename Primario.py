import json
import sys
import os
import subprocess as sp

class PrimarioBot():
    #Construtor da classe
    # um construtor garante o uso de determinadas informações
    def __init__(self, name):
        try:
            memoria = open(name + ".json", "r") # 'r' é read/ler
        except FileNotFoundError:
            memoria = open(name + ".json", "w") # 'w' é write/escrever
            memoria.write(
                            "[['Primário'], {'oi': 'Oi! Qual é o seu nome?', 'tudo bem?': 'Tudo bem?', 'tchau': 'Tchau!'}]")
            memoria.close()
            memoria = open(name + ".json", "r")
        
        self.name = name
        self.conhecido, self.frases = json.load(memoria)
        memoria.close()
        self.historico = [None]

    def Ouvir(self, frase=None):
        if frase == None:
            frase = input('Digite aqui: ') 
        frase = str(frase)
        return frase
        
    def Pensar(self, frase):
        if frase in self.frases[frase]:
            return self.frases[frase]
        if frase == "aprende":
            return "O que você quer que eu aprenda?"
        if frase == "jogar":
            return "https://ncase.itch.io/wbwwb?fbclid=IwAR2YOC5VAXVba0YEiaWloHQw9hrJn0Uiwh54LIutzljyd2t1y7H8cDvcvHw"
        
        ultimaFrase = self.historico [-1]
        if ultimaFrase == 'Oi! Qual é o seu nome?':
            nome = self.pegaNome(frase)
            resposta = self.respostaNome(nome)
            return resposta 
        if ultimaFrase == "O que você quer que eu aprenda?":
            self.palavraChave = frase
            self.frases[self.palavraChave]
            return 'Digite o que eu devo responder:'
        if ultimaFrase == 'Digite o que eu devo responder:':
            resposta = frase
            self.frases[self.palavraChave] = resposta
            self.salvarMemoria()
            return "Aprendido!"
        
        try:
            resposta = str(eval(frase))
            return resposta
        except: 
            pass 
        return "Não entendi!"

    def pegaNome(self, nome):
        if "Meu nome é " in nome:
            nome = nome[12:]
        nome = nome.title()
        return nome

    def respostaNome(self, nome):
        if nome in self.conhecido:
            frase = 'Olá, '
        else:
            frase = "Prazer em conhecê-lo, "
            self.conhecido.append(nome)
            self.salvarMemoria()
        return frase + nome + "!"

    def salvarMemoria(self):
        memoria = open(self.name + '.json', 'w')
        json.dump([self.conhecido, self.frases], memoria)
        memoria.close()

    def Falar(self, frase):
        if 'Executa ' in frase:
            platform = sys.platform
            command = frase.replace('Executa ', '')
            if 'win' in platform:
                os.startfile(command)
            if 'linux' in platform:
                try:
                    sp.Popen(command)
                except FileNotFoundError:
                    sp.Popen(['xdg-open', command])
        else:
            print(frase)
        self.historico.append(frase)