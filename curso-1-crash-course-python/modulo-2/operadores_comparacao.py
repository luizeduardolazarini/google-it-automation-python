# Descrição: Estudo de operadores lógicos e de comparação.

# --- Operadores de Comparação (Retornam True ou False) ---
a = 10
b = 5

print(f"Igual a (==): {a == b}")        # False
print(f"Diferente de (!=): {a != b}")    # True
print(f"Maior que (>): {a > b}")         # True
print(f"Menor que (<): {a < b}")         # False
print(f"Maior ou igual (>=): {a >= 10}") # True
print(f"Menor ou igual (<=): {b <= 3}")  # False

print("-" * 30)

# --- Operadores Lógicos (Combinam condições) ---
idade = 22
tem_cnh = True

# AND: Só é True se AMBOS forem verdadeiros
pode_dirigir = idade >= 18 and tem_cnh
print(f"Pode dirigir? (and): {pode_dirigir}")

# OR: É True se PELO MENOS UM for verdadeiro
estudante = True
trabalhador = False
tem_desconto = estudante or trabalhador
print(f"Tem desconto? (or): {tem_desconto}")

# NOT: Inverte o valor (True vira False e vice-versa)
print(f"Inverso de tem_cnh (not): {not tem_cnh}")

print("-" * 30)

# --- Comparação de Strings ---
# No Python, a comparação de strings diferencia maiúsculas de minúsculas!
usuario_esperado = "admin"
usuario_digitado = "Admin"

print(f"Usuário está correto? {usuario_esperado == usuario_digitado}") # False
