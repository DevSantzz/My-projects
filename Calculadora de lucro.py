print("=== CALCULADORA DE LUCRO ===")

produto = input("Nome do produto: ")

custo = float(input("Quanto você gastou no produto: R$ "))
venda = float(input("Por quanto você vendeu o produto: R$ "))

lucro = venda - custo
margem = (lucro / venda) * 100

print("\n=== RESULTADO ===")
print(f"Produto: {produto}")
print(f"Custo: R$ {custo:.2f}")
print(f"Venda: R$ {venda:.2f}")
print(f"Lucro: R$ {lucro:.2f}")
print(f"Margem de lucro: {margem:.2f}%")
