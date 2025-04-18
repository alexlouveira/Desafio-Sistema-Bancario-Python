maior_idade = 18
idade_especial = 16

idade = int(input("Informe sua idade:"))

if idade >= maior_idade:
    print("maior de idade, pode tirar a CNH.")

if idade < maior_idade:
    print("Ainda não pode tirar a CNH")


if idade >= maior_idade:
    print("Maior de idade, pode tirar a CNH")
elif idade >= idade_especial:
    print("Pode fazer aulas teoricas, mas nao praticas")
else:
    print("Não pode tirar CNH")


