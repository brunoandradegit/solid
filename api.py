class Combustivel:
    def abastecer(self, quantidade):
        pass

class Gasolina(Combustivel):
    def abastecer(self, quantidade):
        return f"Abastecendo {quantidade} litros de gasolina."

class Etanol(Combustivel):
    def abastecer(self, quantidade):
        return f"Abastecendo {quantidade} litros de etanol."

class PostoGasolina:
    def __init__(self, combustivel: Combustivel):
        self.combustivel = combustivel

    def abastecer(self, quantidade):
        return self.combustivel.abastecer(quantidade)

    def realizar_pagamento(self, valor):
        return f"Pagamento de R${valor:.2f} realizado."

gasolina = Gasolina()
posto = PostoGasolina(gasolina)
print(posto.abastecer(20))
print(posto.realizar_pagamento(100.00))