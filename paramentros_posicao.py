def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
   
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")



def make_car(*, modelo, ano, placa, marca, motor, combustivel):

    print(modelo, ano, placa, marca, motor, combustivel)

make_car(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")



