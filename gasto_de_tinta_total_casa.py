#   Este programa permite ao usuário inserir informações sobre um ou mais cômodos,
#   calcula a quantidade de tinta necessária para cada um e exibe os resultados individualmente.
#   O usuário pode continuar adicionando cômodos ou sair do programa digitando "0" como o comprimento do cômodo.

print("Esse sistema é para você descobrir quanto vai precisar de tinta para cada comodo de sua casa")


def calcular_tinta_necessaria(area_parede, capacidade_lata, rendimento_por_litro):
        # Calcula a quantidade de tinta necessária em litros
        litros_de_tinta_necessarios = area_parede / rendimento_por_litro

        # Calcula a quantidade de latas de tinta necessárias
        latas_de_tinta_necessarias = litros_de_tinta_necessarios / capacidade_lata

        return litros_de_tinta_necessarios, latas_de_tinta_necessarias


    # Inicializa as variáveis para armazenar informações sobre as latas de tinta
capacidade_lata = float(input("Digite quantos litros tem na lata de tinta: "))
rendimento_por_litro = float(input("Digite o rendimento que a lata de tinta fala que faz (em metros quadrados por litro): "))

    # Inicializa uma lista para armazenar informações sobre os cômodos
comodos = []

    # Solicita informações sobre os cômodos até que o usuário pare de inserir
while True:
        comprimento = float(input("Digite o comprimento do cômodo em metros (ou digite 0 para sair): "))

        if comprimento == 0:
            break

        largura = float(input("Digite a largura do cômodo em metros: "))
        altura = float(input("Digite a altura do cômodo em metros: "))

        area_parede = 2 * (comprimento + largura) * altura

        litros, latas = calcular_tinta_necessaria(area_parede, capacidade_lata, rendimento_por_litro)

        comodo_info = {
            "comprimento": comprimento,
            "largura": largura,
            "altura": altura,
            "area_parede": area_parede,
            "litros_de_tinta": litros,
            "latas_de_tinta": latas
        }

        comodos.append(comodo_info)

    # Exibe os resultados para cada cômodo
for i, comodo in enumerate(comodos, start=1):
        print(f"\nCômodo {i}:")
        print(f"Área da parede: {comodo['area_parede']:.2f} metros quadrados")
        print(f"Serão necessários {comodo['litros_de_tinta']:.2f} litros de tinta.")
        print(f"Isto equivale a {comodo['latas_de_tinta']:.2f} latas de tinta de {capacidade_lata} litros.")
        
        
        