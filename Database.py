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

    def select(self):
        self.connect()

        try:
            self.cursor.execute("SELECT * FROM cliente")
            result = self.cursor.fetchall()
            return result

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def select_by_id(self,id):
        self.connect()

        try:
            self.cursor.execute(f"SELECT * FROM cliente WHERE id_cli = {id}")                       
            dado = self.cursor.fetchone()
            return dado

        except Exception as err:
            print(err)

        finally:
            self.close_connection()

    def update(self,id_cli):
        self.connect()
        tupla = self.select_by_id(id_cli)
        try:
            self.cursor.execute(f"""    UPDATE cliente SET nome = '{tupla[1]}' WHERE id_cli = {tupla[0]}    """)
            self.conn.commit()
            return True

        except Exception as err:
            print(err)

        finally:
            self.close_connection()    


    def delete(self,id_cli):
        self.connect()

        try:
            self.cursor.execute(f"DELETE FROM cliente WHERE id_cli = {id_cli} ")
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

# id_cli = int(input("Digite o id do cliente que voce quer deletar: "))

# dados = ("Emily","66655544423","67955338811","PA")
# inserir = db.insert(dados)                
# if inserir == True:
#     print("Cadastrado com sucesso!")

# excluir = db.delete(id_cli)
# if excluir == True:
#     print("Excluido com sucesso")    

# clientes = db.select()
# for cli in clientes:
#     print(f'ID: {cli[0]} | Nome: {cli[1]} | CPF: {cli[2]} | Fone: {cli[3]} | Cidade: {cli[4]}')

cliente = db.select_by_id(1)
if cliente:
    print("Cliente encontrado:")
    print(f"ID: {cliente[0]}")
    print(f"Nome: {cliente[1]}")
    print(f"CPF: {cliente[2]}")
    print(f"Fone: {cliente[3]}")
    print(f"Cidade: {cliente[4]}")
else:
    print("Cliente não encontrado.")    

#     id_select = int(input("Qual cliente deseja selecionar? "))
#     clie = db.select_by_id(id_select)
#     print(clie)

# teste = db.update()
