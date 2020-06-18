import sqlite3

MASTER_PASSWORD = "123123"

senha = input("Insira sua senha master: ")
if senha != MASTER_PASSWORD:
    print("senha inválida! Encerrando ...")
    exit()

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("****************************")
    print("* i : inserir nova senha   *")
    print("* l : listar senhas salvas *")
    print("* r : recuperar senha      *")
    print("* s : sair                 *")
    print("****************************")

def get_passaword(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')
    
    if cursor.rowcount == 0:
        print("Serviço Não Cadastrado (Use 'l' Para Verificar Os Serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(service, username, password):
    cursor.execute(f'''
        INSERT INTO users (service, username, password)
        VALUES ('{service}', '{username}', '{password}')
    ''')
    conn.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users;
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    op = input("O que deseja fazer? ")
    if op not in ['i', 'l', 'r', 's']:
        print("Opção inválida")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o Nome Do Serviço? ')
        username = input('Qual o Nome de Usuario? ')
        password = input('Qual é a sua senha? ')
        insert_password(service, username, password)

    if op == 'l':
        show_services()

    if op == 'r':
        service = input('Qual o Serviço Para Qual Quer a Senha? ')
        get_passaword(service)

conn.close()
