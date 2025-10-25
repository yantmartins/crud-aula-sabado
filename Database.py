import mysql.connector

class Database:
    def __init__(self, banco = "perkal") -> None:
        self.banco = banco

    def connect(self):
        self.conn = mysql.connector.connect(host='localhost', database=self.banco,user='root',password='')
        if self.conn.is_connected():
            self.cursor = self.conn.cursor()
            db_info = self.conn.get_server_info()
            print("CONECTADO COM SUCESSO")
        else:
            print("ERROOOO")

    def insert(self,tupla):
        self.connect()

        try:
            self.cursor.execute('INSERT INTO cliente (nome,cpf,fone,cidade) VALUES (%s,%s,%s,%s)',tupla)
            self.conn.commit()
            return True
        
        except Exception as err:
            print(err)

        finally:
            self.close_connection()                

    def close_connection(self):
        if self.conn.is_connected():
            self.cursor.close()
            self.conn.close()
            print("Conexão encerrada com sucesso")

db = Database()

dados = ("Emily","66655544423","67955338811","PA")
cadastro = db.insert(dados)                
if cadastro == True:
    print("Cadastrado com sucesso!")