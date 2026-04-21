# Descrição: Estudo sobre legibilidade de código e uso de comentários.

# --- Exemplo 1: Código Pouco Legível ---
# Nomes de variáveis como 'q', 'z' e 'd' não explicam o que o código faz.
def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5) # Output is 78.5

print("-" * 30)

# --- Exemplo 2: Código Legível (Self-Documenting) ---
# Nomes como 'radius', 'pi' e 'area' tornam o código autoexplicativo.
def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5) # Output is 78.5

# --- Como escrever comentários em Python ---
# Use o símbolo hash (#) no início da linha para explicar o PORQUÊ 
# de uma lógica complexa, não apenas o QUE o código está fazendo.
