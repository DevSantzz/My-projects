import sqlite3
import re
import os
from datetime import datetime

NOME_BANCO = "cadastro.db"


# ---------------------------------------------------------------------------
# Camada de banco de dados
# ---------------------------------------------------------------------------

def conectar():
    """Cria/abre a conexão com o banco de dados SQLite."""
    conexao = sqlite3.connect(NOME_BANCO)
    conexao.execute("PRAGMA foreign_keys = ON")
    return conexao


def criar_tabela():
    """Cria a tabela de usuários caso ela não exista."""
    with conectar() as conexao:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                idade INTEGER NOT NULL,
                telefone TEXT,
                data_cadastro TEXT NOT NULL
            )
            """
        )


# ---------------------------------------------------------------------------
# Validações
# ---------------------------------------------------------------------------

def validar_email(email: str) -> bool:
    padrao = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(padrao, email) is not None


def validar_idade(idade_str: str):
    if not idade_str.isdigit():
        return None
    idade = int(idade_str)
    if 0 < idade < 130:
        return idade
    return None


# ---------------------------------------------------------------------------
# Operações CRUD
# ---------------------------------------------------------------------------

def cadastrar_usuario():
    print("\n--- Cadastrar novo usuário ---")

    nome = input("Nome completo: ").strip()
    while not nome:
        print("O nome não pode ficar em branco.")
        nome = input("Nome completo: ").strip()

    email = input("E-mail: ").strip()
    while not validar_email(email):
        print("E-mail inválido. Tente novamente (ex: nome@exemplo.com).")
        email = input("E-mail: ").strip()

    idade_str = input("Idade: ").strip()
    idade = validar_idade(idade_str)
    while idade is None:
        print("Idade inválida. Digite um número entre 1 e 129.")
        idade_str = input("Idade: ").strip()
        idade = validar_idade(idade_str)

    telefone = input("Telefone (opcional): ").strip()

    data_cadastro = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    try:
        with conectar() as conexao:
            conexao.execute(
                """
                INSERT INTO usuarios (nome, email, idade, telefone, data_cadastro)
                VALUES (?, ?, ?, ?, ?)
                """,
                (nome, email, idade, telefone, data_cadastro),
            )
        print(f"\n✅ Usuário '{nome}' cadastrado com sucesso!")
    except sqlite3.IntegrityError:
        print("\n❌ Erro: já existe um usuário cadastrado com esse e-mail.")


def listar_usuarios():
    print("\n--- Lista de usuários cadastrados ---")
    with conectar() as conexao:
        cursor = conexao.execute(
            "SELECT id, nome, email, idade, telefone, data_cadastro FROM usuarios ORDER BY id"
        )
        usuarios = cursor.fetchall()

    if not usuarios:
        print("Nenhum usuário cadastrado ainda.")
        return

    for u in usuarios:
        id_, nome, email, idade, telefone, data_cadastro = u
        telefone = telefone if telefone else "-"
        print(
            f"\nID: {id_}"
            f"\nNome: {nome}"
            f"\nE-mail: {email}"
            f"\nIdade: {idade}"
            f"\nTelefone: {telefone}"
            f"\nCadastrado em: {data_cadastro}"
            f"\n{'-'*40}"
        )


def buscar_usuario():
    print("\n--- Buscar usuário ---")
    termo = input("Digite o ID ou parte do nome/e-mail: ").strip()

    with conectar() as conexao:
        if termo.isdigit():
            cursor = conexao.execute(
                "SELECT id, nome, email, idade, telefone, data_cadastro FROM usuarios WHERE id = ?",
                (int(termo),),
            )
        else:
            cursor = conexao.execute(
                """
                SELECT id, nome, email, idade, telefone, data_cadastro
                FROM usuarios
                WHERE nome LIKE ? OR email LIKE ?
                """,
                (f"%{termo}%", f"%{termo}%"),
            )
        resultados = cursor.fetchall()

    if not resultados:
        print("Nenhum usuário encontrado.")
        return

    for u in resultados:
        id_, nome, email, idade, telefone, data_cadastro = u
        telefone = telefone if telefone else "-"
        print(
            f"\nID: {id_}"
            f"\nNome: {nome}"
            f"\nE-mail: {email}"
            f"\nIdade: {idade}"
            f"\nTelefone: {telefone}"
            f"\nCadastrado em: {data_cadastro}"
        )


def atualizar_usuario():
    print("\n--- Atualizar usuário ---")
    id_str = input("Digite o ID do usuário que deseja atualizar: ").strip()

    if not id_str.isdigit():
        print("ID inválido.")
        return

    id_usuario = int(id_str)

    with conectar() as conexao:
        cursor = conexao.execute(
            "SELECT id, nome, email, idade, telefone FROM usuarios WHERE id = ?",
            (id_usuario,),
        )
        usuario = cursor.fetchone()

    if not usuario:
        print("Usuário não encontrado.")
        return

    _, nome_atual, email_atual, idade_atual, telefone_atual = usuario

    print("\nDeixe em branco para manter o valor atual.")

    novo_nome = input(f"Nome [{nome_atual}]: ").strip()
    novo_nome = novo_nome if novo_nome else nome_atual

    novo_email = input(f"E-mail [{email_atual}]: ").strip()
    if novo_email and not validar_email(novo_email):
        print("E-mail inválido. Atualização cancelada.")
        return
    novo_email = novo_email if novo_email else email_atual

    nova_idade_str = input(f"Idade [{idade_atual}]: ").strip()
    if nova_idade_str:
        nova_idade = validar_idade(nova_idade_str)
        if nova_idade is None:
            print("Idade inválida. Atualização cancelada.")
            return
    else:
        nova_idade = idade_atual

    novo_telefone = input(f"Telefone [{telefone_atual or '-'}]: ").strip()
    novo_telefone = novo_telefone if novo_telefone else telefone_atual

    try:
        with conectar() as conexao:
            conexao.execute(
                """
                UPDATE usuarios
                SET nome = ?, email = ?, idade = ?, telefone = ?
                WHERE id = ?
                """,
                (novo_nome, novo_email, nova_idade, novo_telefone, id_usuario),
            )
        print("\n✅ Usuário atualizado com sucesso!")
    except sqlite3.IntegrityError:
        print("\n❌ Erro: esse e-mail já está sendo usado por outro usuário.")


def excluir_usuario():
    print("\n--- Excluir usuário ---")
    id_str = input("Digite o ID do usuário que deseja excluir: ").strip()

    if not id_str.isdigit():
        print("ID inválido.")
        return

    id_usuario = int(id_str)

    with conectar() as conexao:
        cursor = conexao.execute("SELECT nome FROM usuarios WHERE id = ?", (id_usuario,))
        usuario = cursor.fetchone()

        if not usuario:
            print("Usuário não encontrado.")
            return

        confirmacao = input(
            f"Tem certeza que deseja excluir '{usuario[0]}'? (s/n): "
        ).strip().lower()

        if confirmacao == "s":
            conexao.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            print("\n✅ Usuário excluído com sucesso!")
        else:
            print("\nOperação cancelada.")


# ---------------------------------------------------------------------------
# Menu principal
# ---------------------------------------------------------------------------

def exibir_menu():
    print("\n" + "=" * 40)
    print("      SISTEMA DE CADASTRO - MENU")
    print("=" * 40)
    print("1 - Cadastrar novo usuário")
    print("2 - Listar todos os usuários")
    print("3 - Buscar usuário")
    print("4 - Atualizar usuário")
    print("5 - Excluir usuário")
    print("0 - Sair")
    print("=" * 40)


def main():
    criar_tabela()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_usuario()
        elif opcao == "2":
            listar_usuarios()
        elif opcao == "3":
            buscar_usuario()
        elif opcao == "4":
            atualizar_usuario()
        elif opcao == "5":
            excluir_usuario()
        elif opcao == "0":
            print("\nSaindo do sistema. Até logo!")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
