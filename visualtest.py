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

endpoint = url+"turmas/"
print("Resetting database... ", end="")
delete_all(endpoint)
print("Done!")

dados = {"id": 0, "nome":"Musica", "turno":"noturno"}

print(f"\nPOST para {endpoint} com dados {dados}")
response = requests.post(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 201

dados2 = {"id": 0, "nome":"Teatro", "curso":"diurno"}
print(f"\nPOST para {endpoint} com dados {dados2}")
response = requests.post(endpoint, json=dados2)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 201

print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint += "1"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

dados = response.json()
dados["nome"] = "Atletismo"
print(f"\nPUT para {endpoint}")
response = requests.put(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint = url+"turmas/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint += "1"
print(f"\nDELETE para {endpoint}")
response = requests.delete(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint = url+"turmas/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

# A L U N O S #

endpoint = url+"alunos/"

dados = {"id": 0, "nome":"Jose", "curso":"outro"}
print(f"\nPOST para {endpoint} com dados {dados}")
response = requests.post(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 201

dados2 = {"id": 0, "nome":"Maria", "curso":"algum"}
print(f"\nPOST para {endpoint} com dados {dados2}")
response = requests.post(endpoint, json=dados2)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 201

print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint += "1"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

dados = response.json()
dados["nome"] = "Joao"
print(f"\nPUT para {endpoint}")
response = requests.put(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint = url+"alunos/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint += "1"
print(f"\nDELETE para {endpoint}")
response = requests.delete(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

endpoint = url+"alunos/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
assert response.status_code == 200

print("Cleaning up database... ", end="")
delete_all(url+"turmas/")
delete_all(url+"alunos/")
print("Done!")


input()