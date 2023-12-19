import os
import sqlite3
from sqlite3 import Error
import random

#Conexão
def conexãoBanco():
    caminho = "C:\\Users\\jcoel\\Sqlite\\lista_de_funcionarios.db"
    try:
        con = sqlite3.connect(caminho)
    except Error as ex :
        print(ex)
    return con

vcon = conexãoBanco()

def menuPrincipal():
    os.system('cls')
    print('1 - Inserir novo colaborador: ')
    print('2 - Deletar colaborador: ')
    print('3 - Editar colaborador: ')
    print('4 - Consultar lista de colaboradores: ')
    print('5 - Sortear colaboradores: ')
    print('6 - Sair')

def query(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except Error as ex:
        print(ex)

    finally:
        print('Coneção realizada com sucesso! ')

def consultar(conexao, sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    return res

def menuInserir():
    os.system('cls')
    vnome = str(input('Digite o nome: '))
    vmatricula = str(input('Digite a matrícula: '))
    vsql = "INSERT INTO Colaboradores (NOME_COLABORADOR, MATRICULA_COLABORADOR) VALUES ('"+vnome+"', '"+vmatricula+"') "
    query(vcon, vsql)

def menuDeletar():
    os.system('cls')
    vid = str(input('Digite o ID do registro a ser apagado: '))
    vsql ="DELETE FROM Colaboradores WHERE ID_COLABORADOR = " + vid
    query(vcon, vsql)

def menuAtualizar():
    os.system('cls')
    vid = input('Informe o ID que deseja editar: ')
    r = consultar(vcon, "SELECT * FROM Colaboradores WHERE ID_COLABORADOR = " +vid)
    rnome =r[0][1]
    rmatricula = r[0][2]
    vnome = input('Digite o nome: ')
    vmatricula = input('Digite a matricula: ')
    if (len(vnome) == 0):
        vnome = rnome
    elif (len(vmatricula) == 0):
        vmatricula = rmatricula
    vsql = "UPDATE Colaboradores SET NOME_COLABORADOR = '"+vnome+"' , MATRICULA_COLABORADOR = '"+vmatricula+"' WHERE ID_COLABORADOR =" +vid
    query(vcon, vsql)

def menuConsultar():
    os.system('cls')
    vsql = "SELECT * FROM Colaboradores"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print('ID: {0:_<3} Nome: {1:_<30} Matricula: {2:_<6}'.format(r[0], r[1], r[2]))
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system('pause')
            os.system('cls')
    print('Fim de lista')

def sortear():
    os.system('cls')
    vsql = "SELECT * FROM Colaboradores"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    list = []
    for r in res:
        print('ID: {0:_<3} Nome: {1:_<30} Matricula: {2:_<6}'.format(r[0], r[1], r[2]))
        list.append(r[1])
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system('pause')
            os.system('cls')
    for i in range(len(list) - 1, 0, -1):
        j = random.randint(0, i + 1)

        list[i], list[j] = list[j], list[i]

    print('Lista sorteada: ')
    for c in list:
        print(c)

def menuConsultaNome():
    vnome = input('Digite um nome: ')
    vsql = "SELECT * FROM Colaboradores WHERE NOME_COLABORADOR LIKE '%"+vnome+"%'"
    res = consultar(vcon, vsql)
    vlim = 10
    vcont = 0
    for r in res:
        print('ID: {0:_<3} Nome: {1:_<30} Matricula: {2:_<6}'.format(r[0], r[1], r[2]))
        vcont += 1
        if vcont >= vlim:
            vcont = 0
            os.system('pause')
            os.system('cls')
    print('Fim de lista')
    os.system('pause')

opc = 0
while opc != 6:
    menuPrincipal()
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        menuInserir()
    elif opc == 2:
        menuDeletar()
    elif opc == 3:
        menuAtualizar()
    elif opc == 4:
        menuConsultar()
    elif opc == 5:
        sortear()
    elif opc == 6:
        os.system('cls')
        print('Programa finalizado')
        break
    else:
        os.system('cls')
        print('Informe um valor válido')
        os.system('pause')







