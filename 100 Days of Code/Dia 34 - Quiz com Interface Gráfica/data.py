import requests

# Dicionário contendo os parâmetros de consulta na solicitação da API.
parameters = {"amount": 10, "category": 15, "difficulty": "medium", "type": "boolean"}

# Enviando uma solicitação GET para a API do Open Trivia DB.
response = requests.get("https://opentdb.com/api.php", params=parameters)
# Verificando se houve algum erro na requisição.
response.raise_for_status()

# Obtendo os dados das perguntas.
question_data = response.json()["results"]