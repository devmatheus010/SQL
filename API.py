import requests
import mysql.connector

banco = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "123456",
    database = "turma_c"
)
meucursor = banco.cursor()

cep = input("Digite seu CEP: ")
if len(cep) == 8:
    link = f"https://viacep.com.br/ws/{cep}/json"
    requisicao = requests.get(link)
    print(requisicao)
    dic_requisicao = requisicao.json()
    cep = dic_requisicao["cep"]
    logradouro = dic_requisicao["logradouro"]
    complemento = dic_requisicao["complemento"]
    print(dic_requisicao)
    sql = "insert into endereco(logradouro, complemento, cep) values (%s, %s, %s)"
    data = (logradouro,complemento,cep)
    meucursor.execute(sql,data)
    banco.commit()
    meucursor.close()
    banco.close()
else:
    print("CEP inváldio")


