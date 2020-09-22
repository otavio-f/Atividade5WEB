import requests #<--
import json

url = "http://localhost:8080/api/"

#Teste visual

# T U R M A S #

test_point = "turmas"
dados = {"id": 0, "nome":"Musica", "turno":"noturno"}

print(f"Fazendo request post para {url+test_point} com dados {dados}")
response = requests.post(url+test_point, json=dados)
print(f"{response.status_code}: {response.text}")

dados2 = {"id": 0, "nome":"Teatro", "curso":"diurno"}
print(f"Fazendo request post para {url+test_point} com dados {dados2}")
response = requests.post(url+test_point, json=dados2)
print(f"{response.status_code}: {response.text}")

print(f"\nFazendo request get para {url+test_point}")
response = requests.get(url+test_point)
print(f"{response.status_code}: {response.text}")

test_point = "turmas/1"
print(f"\nFazendo request delete para {url+test_point}")
response = requests.delete(url+test_point, json=dados)
print(f"{response.status_code}: {response.text}")

test_point = "turmas"
print(f"\nFazendo request get para {url+test_point}")
response = requests.get(url+test_point)
print(f"{response.status_code}: {response.text}")

# A L U N O S #

test_point = "alunos"
dados = {"id": 0, "nome":"Jose", "curso":"outro"}

print(f"\nFazendo request post para {url+test_point} com dados {dados}")
response = requests.post(url+test_point, json=dados)
print(f"{response.status_code}: {response.text}")

dados2 = {"id": 0, "nome":"Maria", "curso":"algum"}
print(f"Fazendo request post para {url+test_point} com dados {dados2}")
response = requests.post(url+test_point, json=dados2)
print(f"{response.status_code}: {response.text}")

print(f"\nFazendo request get para {url+test_point}")
response = requests.get(url+test_point)
print(f"{response.status_code}: {response.text}")

test_point = "alunos/1"
print(f"\nFazendo request delete para {url+test_point}")
response = requests.delete(url+test_point, json=dados)
print(f"{response.status_code}: {response.text}")

test_point = "alunos"
print(f"\nFazendo request get para {url+test_point}")
response = requests.get(url+test_point)
print(f"{response.status_code}: {response.text}")