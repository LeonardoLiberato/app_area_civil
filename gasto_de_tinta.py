# Solicita as dimensões do cômodo ao usuário


# Este programa permite ao usuário inserir as dimensões do cômodo,
# a capacidade da lata de tinta e o rendimento da tinta por litro,
# e então calcula a quantidade de tinta necessária em litros
# e quantas latas de tinta serão necessárias com base nas informações fornecidas.

print("Vamos descobrir quanto de tinta você vai precisar para pintar o local informado! ")
comprimento = float(input("Digite o comprimento do cômodo em metros: "))
largura = float(input("Digite a largura do cômodo em metros: "))
altura = float(input("Digite a altura do cômodo em metros: "))

# Calcula a área da parede a ser pintada
area_parede = 2 * (comprimento + largura) * altura

# Solicita informações sobre a lata de tinta
capacidade_lata = float(input("Digite quantos litros tem na lata de tinta: "))
rendimento_por_litro = float(input("Digite o rendimento que a lata de tinta fala que faz (em metros quadrados por litro): "))

# Calcula a quantidade de tinta necessária em litros
litros_de_tinta_necessarios = area_parede / rendimento_por_litro

# Calcula a quantidade de latas de tinta necessárias
latas_de_tinta_necessarias = litros_de_tinta_necessarios / capacidade_lata

# Exibe o resultado para o usuário
print(f"Serão necessários {litros_de_tinta_necessarios:.2f} litros de tinta.")
print(f"Isto equivale a {latas_de_tinta_necessarias:.2f} latas de tinta de {capacidade_lata} litros.")
