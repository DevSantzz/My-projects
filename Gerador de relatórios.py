print("=== REPORT GENERATOR ===")

nome = input("Nome do relatório: ")
responsavel = input("Responsável: ")

print("\nDigite os dados do relatório:")

total_vendas = int(input("Quantidade de vendas: "))
faturamento = float(input("Faturamento total: R$ "))
despesas = float(input("Despesas: R$ "))

lucro = faturamento - despesas

if faturamento > 0:
    margem = (lucro / faturamento) * 100
else:
    margem = 0

if lucro > 0:
    status = "LUCRO"
elif lucro < 0:
    status = "PREJUÍZO"
else:
    status = "EMPATE"

relatorio = f"""
========================================
           RELATÓRIO
========================================

Nome: {nome}
Responsável: {responsavel}

----------------------------------------
DADOS
----------------------------------------

Quantidade de vendas: {total_vendas}
Faturamento: R$ {faturamento:.2f}
Despesas: R$ {despesas:.2f}

----------------------------------------
RESULTADOS
----------------------------------------

Lucro/Prejuízo: R$ {lucro:.2f}
Margem de lucro: {margem:.2f}%
Status: {status}

========================================
        FIM DO RELATÓRIO
========================================
"""

print(relatorio)

arquivo = input("Nome do arquivo para salvar: ")

if not arquivo.endswith(".txt"):
    arquivo += ".txt"

with open(arquivo, "w", encoding="utf-8") as f:
    f.write(relatorio)

print(f"\nRelatório salvo como: {arquivo}")
