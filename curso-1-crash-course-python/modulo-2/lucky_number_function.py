# Descrição: Demonstração de como funções eliminam repetição de código (DRY).

# --- Sem o uso de funções (Código Repetido) ---
name = "Kay"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9
print("Hello " + name + ". Your lucky number is " + str(number))

print("-" * 30)

# --- Com o uso de funções (Código Otimizado) ---
def lucky_number(name):
    # A lógica é escrita apenas uma vez
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

# Chamadas simples e limpas
lucky_number("Kay")
lucky_number("Cameron")
