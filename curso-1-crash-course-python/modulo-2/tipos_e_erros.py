# --- OPERAÇÕES BÁSICAS E TIPOS (INTEIROS E FLOATS) ---
print("--- Operações Numéricas ---")
print(7 + 8)          # Soma de inteiros (Resultado: 15)
print(7 * 8)          # Multiplicação
print(2 ** 3)         # Exponenciação (2 elevado a 3 = 8)
print(type(7))        # <class 'int'>
print(type(7.5))      # <class 'float'>


# --- TRABALHANDO COM TEXTO (STRINGS) ---
print("\n--- Manipulação de Strings ---")
print("hello " + "world")  # Concatenação de strings
print("Python " * 3)       # Repetição de strings


# --- FORMATTAÇÃO MODERNA (f-strings) ---
print("\n--- Exemplos de f-strings ---")
print(f"2 + 2 = {(2 + 2)}") # Processamento dentro da string

# Exemplo aplicado ao seu contexto:
nome_personagem = "Artemis"
dano_ataque = 12
print(f"A personagem {nome_personagem} causou {dano_ataque} de dano!")


# --- COMPARAÇÕES LÓGICAS (BOOLEANOS) ---
print("\n--- Comparações e Booleano ---")
print(10 > 1)          # True
print("cat" == "dog")  # False
print(type(True))      # <class 'bool'>


# --- CONVERSÃO DE TIPOS (CASTING) ---
print("\n--- Conversão de Tipos ---")
numero_texto = "8"
# print(7 + numero_texto) # <-- Isso causaria um TypeError!
# O correto é converter antes:
print(7 + int(numero_texto)) # Resultado: 15


# --- EXEMPLOS DE ERROS COMUNS (Para estudo) ---
print("\n--- Notas sobre Erros ---")
# TypeError: Acontece quando você tenta somar tipos incompatíveis (ex: 7 + "8")
# SyntaxError: Acontece quando falta um parêntese ou aspas (como o dquote que vimos)
# NameError: Acontece quando você tenta usar uma variável que ainda não criou
