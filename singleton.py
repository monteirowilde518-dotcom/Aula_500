class SingletonMeta(type):
    _instancias = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instancias:
           cls._instancias[cls] = super().__call__(*args, **kwargs)
        return cls._instancias[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        self.conexao = "conectado"

db1 = DatabaseConnection()
db2 = DatabaseConnection()
print(db1 is db2)

class Comando:
    def executar(self): ...
    def desfazer(self): ...

class Luz:
    def ligar(self): print("luz ligada")
    def desligar(self): print("luz desligada")

class LigarLuz(Comando):
    def __init__(self, luz): self.luz = luz
    def executar(self): self.luz.ligar()
    def desfazer(self): self.luz.desligar()

class Controle:
    def __init__(self): self.historico = []
    def apertar(self, cmd):
        cmd.executar()
        self.historico.append(cmd)
    def voltar(self):
        self.historico.pop().desfazer()

controle = Controle()
controle.apertar(LigarLuz(Luz()))
controle.voltar()

class Cafe:
    def custo(self): return 5.0
    def descricao(self): return "Cafe"

class Adicional:
    def __init__(self, bebida):
        self.bebida = bebida

class Leite(Adicional):
    def custo(self): return self.bebida.custo() + 2.0
    def descricao(self): return self.bebida.descricao() + "+leite"

class Chantilly(Adicional):
    def custo(self): return self.bebida.custo() + 3.0
    def descricao(self): return self.bebida.descricao() + "+chantilly"

pedido = Chantilly(Leite(Cafe()))
print(pedido.descricao())






