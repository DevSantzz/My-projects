print("=== ANALISADOR DE TEXTO ===")

linhas = []

for i in range(20):
    texto = input(f"Digite a linha {i + 1} (Enter para terminar): ")
    if texto == "":
        break
    linhas.append(texto)

texto = " ".join(linhas)

caracteres = len(texto)
palavras = texto.split()
quantidade_palavras = len(palavras)
maiusculo = texto.upper()
minusculo = texto.lower()

print("\n=== RESULTADO ===")
print(f"Quantidade de caracteres: {caracteres}")
print(f"Quantidade de palavras: {quantidade_palavras}")
print(f"Texto em maiúsculas: {maiusculo}")
print(f"Texto em minúsculas: {minusculo}")

