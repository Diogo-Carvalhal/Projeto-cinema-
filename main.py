
class Filme:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao


class Sessao:
    def __init__(self, filme, horario, lugares):
        self.filme = filme
        self.horario = horario
        self.lugares = lugares

    def mostrar_sessao(self):
        print(f"{self.filme.titulo} às {self.horario} - Lugares disponíveis: {self.lugares}")

    def vender_lugar(self):
        if self.lugares > 0:
            self.lugares -= 1
            return True
        else:
            return False

class Cliente:
    def __init__(self, nome, nif):
        self.nome = nome
        self.nif = nif
        self.bilhetes = []

    def comprar(self, sessao):
        if sessao.vender_lugar():
            self.bilhetes.append(sessao)
            print(f"{self.nome} comprou bilhete para {sessao.filme.titulo} às {sessao.horario}")
        else:
            print("Não há lugares disponíveis.")

    def ver_bilhetes(self):
        if not self.bilhetes:
            print("Nenhum bilhete comprado.")
        else:
            print("Bilhetes comprados:")
            for s in self.bilhetes:
                print(f"{s.filme.titulo} às {s.horario}")


class Cinema:
    def __init__(self):
        self.sessoes = []
        self.clientes = {}

    def adicionar_sessao(self, sessao):
        self.sessoes.append(sessao)

    def mostrar_sessoes(self):
        if not self.sessoes:
            print("Não há sessões.")
        else:
            for i, s in enumerate(self.sessoes):
                print(f"{i + 1}. ", end="")
                s.mostrar_sessao()

    def adicionar_cliente(self, cliente):
        if cliente.nif in self.clientes:
            print("Cliente já existe.")
        else:
            self.clientes[cliente.nif] = cliente
            print("Cliente adicionado.")

    def encontrar_cliente(self, nif):
        return self.clientes.get(nif)

cinema = Cinema()

while True:
    print("\n--- MENU CINEMA ---")
    print("1 - Adicionar Sessão")
    print("2 - Ver Sessões")
    print("3 - Adicionar Cliente")
    print("4 - Comprar Bilhete")
    print("5 - Ver Bilhetes do Cliente")
    print("6 - Sair")

    escolha = input("Opção: ")

    if escolha == "1":
        titulo = input("Título do filme: ")
        duracao = int(input("Duração: "))
        hora = input("Hora da sessão: ")
        lugares = int(input("Lugares disponíveis: "))

        filme = Filme(titulo, duracao)
        sessao = Sessao(filme, hora, lugares)
        cinema.adicionar_sessao(sessao)
        print("Sessão adicionada.")

    elif escolha == "2":
        cinema.mostrar_sessoes()

    elif escolha == "3":
        nome = input("Nome: ")
        nif = input("NIF: ")
        cliente = Cliente(nome, nif)
        cinema.adicionar_cliente(cliente)

    elif escolha == "4":
        cinema.mostrar_sessoes()
        if not cinema.sessoes:
            continue

        try:
            num = int(input("Escolha o número da sessão: ")) - 1
            sessao = cinema.sessoes[num]
        except:
            print("Sessão inválida.")
            continue

        nif = input("Digite o NIF do cliente: ")
        cliente = cinema.encontrar_cliente(nif)
        if cliente:
            cliente.comprar(sessao)
        else:
            print("Cliente não encontrado.")

    elif escolha == "5":
        nome = input("nome do cliente")
        nif = input("NIF do cliente: ")
        cliente = cinema.encontrar_cliente(nif)
        if cliente:
            cliente.ver_bilhetes()
        else:
            print("Cliente não encontrado.")

    elif escolha == "6":
        print("Até à próxima!")
        break

    else:
        print("Opção inválida.")
