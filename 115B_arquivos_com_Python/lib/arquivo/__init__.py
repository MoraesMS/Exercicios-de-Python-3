from lib.interface import *


def arquivoExiste(nome):
    try:
        a = open(nome, 'rt') # rt = leitura de arquivo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:                      # wt = gravação de arquivo texto
        a = open(nome, 'wt+') # linha de comando para criar um arquivo txt, o sinal de + faz a criação
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')



def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        print(a.read())
