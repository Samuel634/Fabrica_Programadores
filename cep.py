import requests

cep = input("Digite seu cep: ")
via_cep = f"http://viacep.com.br/ws/{cep}/json/"
requisicao = requests.get(via_cep)

print(requisicao)

print(f"CEP: {requisicao.json()['cep']}")
print(f"CEP: {requisicao.json()['logradouro']}")
print(f"CEP: {requisicao.json()['bairro']}")
print(f"CEP: {requisicao.json()['localidade']}")
print(f"CEP: {requisicao.json()['estado']}")