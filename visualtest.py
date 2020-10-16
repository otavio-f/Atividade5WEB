import requests #<-- required, install with pip
import json

url = "http://localhost:8080/api/"

def delete_all(endpoint):
	contents = requests.get(endpoint).json()
	for data in contents:
		requests.delete(endpoint+str(data['id']))

#Teste visual

# T U R M A S #

endpoint = url+"turmas/"
print("Resetting entries... ", end="")
delete_all(endpoint)
print("Done!")

dados = {"id": 0, "nome":"Musica", "turno":"noturno"}

print(f"\nPOST para {endpoint} com dados {dados}")
response = requests.post(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")

dados2 = {"id": 0, "nome":"Teatro", "curso":"diurno"}
print(f"\nPOST para {endpoint} com dados {dados2}")
response = requests.post(endpoint, json=dados2)
print(f"{response.status_code}: {response.text}")

print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
print(type(response.text))

endpoint += 1
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
dados = response.json()
dados["nome"] = "Atletismo"

print(f"\nPUT para {endpoint}")
response = requests.put(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")

endpoint = url+"turmas/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")

endpoint += "1"
print(f"\nDELETE para {endpoint}")
response = requests.delete(endpoint)
print(f"{response.status_code}: {response.text}")

endpoint = url+"turmas/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")

# A L U N O S #

endpoint = url+"alunos/"
dados = {"id": 0, "nome":"Jose", "curso":"outro"}

print(f"\nPOST para {endpoint} com dados {dados}")
response = requests.post(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")

dados2 = {"id": 0, "nome":"Maria", "curso":"algum"}
print(f"\nPOST para {endpoint} com dados {dados2}")
response = requests.post(endpoint, json=dados2)
print(f"{response.status_code}: {response.text}")

print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")

endpoint += "1"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")
dados = response.json()
dados["nome"] = "Joao"

print(f"\nPUT para {endpoint}")
response = requests.put(endpoint, json=dados)
print(f"{response.status_code}: {response.text}")

endpoint = url+"alunos/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")

endpoint += "1"
print(f"\nDELETE para {endpoint}")
response = requests.delete(endpoint)
print(f"{response.status_code}: {response.text}")

endpoint = url+"alunos/"
print(f"\nGET para {endpoint}")
response = requests.get(endpoint)
print(f"{response.status_code}: {response.text}")

input()