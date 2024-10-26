class Usuario():
    def __init__(self, nome, sobrenome, idade, cidade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade

    def informacaoSaida(self):
        print(f'Meu Nome é',self.nome.title(),self.sobrenome.title(),', Tenho',self.idade,'Anos'', Sou de',self.cidade.title(),)
    
usuario1 = Usuario(input('Digite o Nome: '), input('Digite o Sobrenome: '), input('Digite a Idade: '),input('Digite a cidade: '))
usuario2 = Usuario(input('Digite o Nome: '), input('Digite o Sobrenome: '), input('Digite a Idade: '),input('Digite a cidade: '))
usuario3 = Usuario(input('Digite o Nome: '), input('Digite o Sobrenome: '), input('Digite a Idade: '),input('Digite a cidade: '))
usuario1.informacaoSaida()
usuario2.informacaoSaida()
usuario3.informacaoSaida()