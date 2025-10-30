from Database import Database

class Cliente:
    def __init__(self,nome=None,cpf=None,fone=None,cidade=None):
        self.nome = nome
        self.cpf = cpf
        self.fone = fone
        self.cidade = cidade
        self.db = Database()

    def cadastrar(self):
        self.db = Database()
        tupla = (self.nome,self.cpf,self.fone,self.cidade)
        result = self.db.insert(tupla)
        return result
    
    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados



gafanhoto = Cliente()
gafanhoto.nome = input("Digite seu nome: ")
gafanhoto.cpf = input("Digite seu cpf: ")
gafanhoto.fone = input("Digite seu fone: ")
gafanhoto.cidade = input("Digite sua cidade: ")
gafanhoto.cadastrar()


clientes = gafanhoto.buscar()    