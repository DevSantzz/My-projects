print("=== ANALISADOR DE TEXTO ===")

texto = input("Digite um texto: ")

# Quantidade de caracteres
caracteres = len(texto)

# Quantidade de palavras
palavras = texto.split()
quantidade_palavras = len(palavras)

# Texto em maiúsculas
maiusculo = texto.upper()

# Texto em minúsculas
minusculo = texto.lower()

print("\n=== RESULTADO ===")
print(f"Quantidade de caracteres: {caracteres}")
print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Texto em maiúsculas: {maiusculo}")
print(f"Texto em minúsculas: {minusculo}")
