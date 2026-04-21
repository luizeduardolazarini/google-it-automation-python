# --- Interação com f-strings e Strings ---
month = "September"
# O uso do 'f' antes das aspas permite injetar variáveis direto no texto entre chaves {}
# É a forma mais moderna e eficiente de criar mensagens dinâmicas em Python.
print(f"Investigate failed login attempts during {month} if more than 100")

# --- Identificação de Tipos ---
# O comando type() é essencial para debug: ele revela se o dado é uma String, Inteiro, Lista, etc.
print(type("This is a string")) # Exibe <class 'str'>

# --- Conversão de Tipos (Casting) ---
number = 12
# str() converte um número em texto para que ele possa ser concatenado ou salvo em arquivos de log.
string_representation = str(number)
print(string_representation)

# --- Manipulação de Listas (Análise de Dados) ---
time_list = [12, 2, 32, 19, 57, 22, 14]

# sorted() organiza a lista em ordem crescente, mas ATENÇÃO:
# ele gera uma CÓPIA ordenada. A lista original 'time_list' continua bagunçada.
print(f"Lista ordenada (cópia): {sorted(time_list)}")
print(f"Lista original permanece igual: {time_list}")

# min() e max() são funções estatísticas básicas.
# Na automação, você usaria isso para achar, por exemplo, o horário do primeiro (mínimo) 
# e do último (máximo) acesso de um usuário no servidor.
print(f"Menor valor da lista: {min(time_list)}") # Útil para achar o início de um log
print(f"Maior valor da lista: {max(time_list)}") # Útil para achar o fim de um log
