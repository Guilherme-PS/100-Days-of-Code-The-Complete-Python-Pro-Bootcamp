import requests
import datetime as dt

# Dados do usuário.
TOKEN = "SEU TOKEN"
USERNAME = "SEU NOME DE USUÁRIO"
GRAPH_ID = "ID DO GRÁFICO"
GRAPH_NAME = "NOME DO GRÁFICO"
UNIT = "UNIDADE"
TYPE = "TIPO (INT OU FLOAT)"

# Token
HEADER = {"X-USER-TOKEN": TOKEN}

## Cria uma conta na API pixe.la.
# create_account_parameters = {"token": TOKEN, "username": USERNAME, "agreeTermsOfService": "yes", "notMinor": "yes"}
# response = requests.post(f"https://pixe.la/v1/user, json=create_account_parameters)

## Cria um gráfico.
# graph_parameters = {"id": GRAPH_ID, "name": GRAPH_NAME, "unit": UNIT, "type": TYPE, "color": "ajisai"}
# response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs", json=graph_parameters, headers=HEADER)

# Adiciona um pixel no dia atual.
today = dt.datetime.now()

create_pixel_parameter = {"date": today.strftime("%Y%m%d"), "quantity": input("Quantas páginas você leu hoje? ")}

response = requests.post(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}", json=create_pixel_parameter,
                         headers=HEADER)

## Atualiza um pixel em um dia especificado.
# update_graph_parameters = {"quantity": "10"}
#
# another_day = dt.datetime(year=2023, month=1, day=25)

## Deleta um pixel em um dia especificado.
# response = requests.put(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{another_day.strftime('%Y%m%d')}",
#                         json=update_graph_parameters, headers=HEADER)

# response = requests.delete(f"https://pixe.la/v1/users/{USERNAME}/graphs/{GRAPH_ID}/{another_day.strftime('%Y%m%d')}",
#                            headers=HEADER)



