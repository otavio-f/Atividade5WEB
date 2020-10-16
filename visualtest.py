import requests #<-- required, install with pip
import json

url = "https://first-heroku-app-is-a-spring.herokuapp.com/api/"
#url = "http://localhost:8080/api/"

def delete_all(endpoint: str):
	contents = requests.get(endpoint).json()
	for data in contents:
		requests.delete(endpoint+str(data['id']))

#Teste visual

# T U R M A S #

print("Limpando base de dados... ", end="")
delete_all(url+"turmas/")
delete_all(url+"alunos/")
print("Feito!")

endpoint = url+"turmas/"

# Insert #
dados = {"id": 0, "nome":"Musica", "turno":"noturno"}
print(f"\nInserindo uma turma... ", end="")
response = requests.post(endpoint, json=dados)
assert response.status_code == 201
response_data = response.json()
assert response_data == {"id": 1, "nome":"Musica", "turno":"noturno"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos: \n\t{response_data}")

# Insert #
dados = {"id": 0, "nome":"Teatro", "turno":"diurno"}
print(f"\nInserindo uma turma... ", end="")
response = requests.post(endpoint, json=dados)
assert response.status_code == 201
response_data = response.json()
assert response_data == {"id": 2, "nome":"Teatro", "turno":"diurno"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos: \n\t{response_data}")

# Get all turmas #
print("\nRecuperando dados de todas as turmas... ", end="")
response = requests.get(endpoint)
assert response.status_code == 200
response_data = response.json()
assert len(response_data) == 2
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos:\n\t\t{response_data[0]}\n\t\t{response_data[1]}")

# Get turma/1 #
endpoint = url+"turmas/1"
print("\nRecuperando dados de uma turma... ", end="")
response = requests.get(endpoint)
assert response.status_code == 200
response_data = response.json()
assert response_data == {"id": 1, "nome":"Musica", "turno":"noturno"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos:\n\t{response_data}")

# Modify turma/1 #
dados = response.json()
dados["nome"] = "Atletismo"
print("\nModificando turma anterior... ", end="")
response = requests.put(endpoint, json=dados)
assert response.status_code == 200
response_data = response.json()
assert response_data == {"id": 1, "nome":"Atletismo", "turno":"noturno"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos:\n\t{response_data}")

# Delete turma/1 #
endpoint = url+"turmas/1"
print("\nDeletando uma turma... ", end="")
response = requests.delete(endpoint)
assert response.status_code == 200
# Check if turma count is 1 #
response = requests.get(url+"turmas/")
response_data = response.json()
assert len(response_data) == 1
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados restantes:\n\t{response_data}")

# A L U N O S #

endpoint = url+"alunos/"

# Insert #
dados = {"id": 0, "nome":"Jose", "curso":"outro"}
print(f"\nInserindo um aluno... ", end="")
response = requests.post(endpoint, json=dados)
assert response.status_code == 201
response_data = response.json()
assert response_data == {"id": 1, "nome":"Jose", "curso":"outro"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos: \n\t{response_data}")

# Insert #
dados = {"id": 0, "nome":"Maria", "curso":"algum"}
print(f"\nInserindo um aluno... ", end="")
response = requests.post(endpoint, json=dados)
assert response.status_code == 201
response_data = response.json()
assert response_data == {"id": 2, "nome":"Maria", "curso":"algum"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos: \n\t{response_data}")

# Get all alunos #
print("\nRecuperando dados de todos os alunos... ", end="")
response = requests.get(endpoint)
assert response.status_code == 200
response_data = response.json()
assert len(response_data) == 2
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos:\n\t\t{response_data[0]}\n\t\t{response_data[1]}")

# Get aluno/1 #
endpoint = url+"alunos/1"
print("\nRecuperando dados de um aluno... ", end="")
response = requests.get(endpoint)
assert response.status_code == 200
response_data = response.json()
assert response_data == {"id": 1, "nome":"Jose", "curso":"outro"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos:\n\t{response_data}")

# Modify aluno/1 #
dados = response.json()
dados["nome"] = "Joao"
print("\nModificando aluno anterior... ", end="")
response = requests.put(endpoint, json=dados)
assert response.status_code == 200
response_data = response.json()
assert response_data == {"id": 1, "nome":"Joao", "curso":"outro"}
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados recebidos:\n\t{response_data}")

# Delete aluno/1 #
endpoint = url+"alunos/1"
print("\nDeletando um aluno... ", end="")
response = requests.delete(endpoint)
assert response.status_code == 200
# Check if aluno count is 1 #
response = requests.get(url+"alunos/")
response_data = response.json()
assert len(response_data) == 1
print(f"OK!\n\tCodigo {response.status_code}.\n\tDados restantes:\n\t{response_data}")

print("\n\nLimpando base de dados... ", end="")
delete_all(url+"turmas/")
delete_all(url+"alunos/")
print("Feito!")

input()