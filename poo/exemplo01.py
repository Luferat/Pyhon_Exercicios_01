class Carro:
    
    # Método contrutor
    def __init__(self):

        # Atributos
        self.cor = ""
        self.marca = ""
        self.modelo = None
        pass

    # Métodos
    def ligar(self):
        print("Vrum vrum")

    def desligar(self):
        print("Cof Cof")


# Cria um objeto `fuscao`
fuscao = Carro() # ou criando um "instância" do tipo Carro

# Cor do meu carro
fuscao.cor = "preto"

# Ligar o carro
fuscao.ligar()

# Desligar o carro
fuscao.desligar()

# ler a cor do carro
print(fuscao.cor)


# Cria outro objeto
opalao = Carro()
opalao.cor = 'vermelho'
opalao.ligar()
print(opalao.cor)
opalao.desligar()