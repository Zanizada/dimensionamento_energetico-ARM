import json

# def calculo_khw(equipamentos: list)

equipamentos = {
    "microondas": 1200,
    "geladeira": 150,
    "fogao a gas": 25,
    "fogao eletrico": 6000,
    "maquina de lavar": 400,
    "maquina lava e seca": 2000,
    "ferro de passar": 1500,
    "forno eletrico (air fryer)": 2000
}

equipamentos_usados = []
horas_por_equipamento = []
residencia = {"cep": 0, "numero": 0, "complemento": ""}

while True:
    residencia["cep"] = int(input("Qual o CEP da residência? "))
    residencia["numero"] = int(input("Qual o número da residência? "))
    pergunta = (input("Tem complemento? (s/n)")).lower()
    if pergunta == "s":
        residencia["complemento"] = input("Qual o complemento? ")

    print("Eletrodomésticos:")
    for equipamento in equipamentos:
        pergunta = (input(f"Contém {equipamento}? (s/n)")).lower()
        if pergunta == "s":
            equipamentos_usados.append(equipamento)
            horas = int(input("Quantas horas usou o equipamento por dia? "))
