import requests
import json

# Получаю токен по ключу, который сделал в веб интерфейсе Гигачата (в целом пока не нужно)
def get_token(key):

  url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

  payload={
    'scope': 'GIGACHAT_API_PERS'
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '3c9a6c74-3ca2-420c-b782-7600f4c50870',
    'Authorization': f'Basic {key}'
  }

  response = requests.request("POST", url, headers=headers, data=payload, verify=False)

  data = json.loads(response.text)

  access_token = data['access_token']

  return access_token

# По запросу из url получаю список моделей (в целом пока не нужно)
def get_models(access_token):

  url = "https://gigachat.devices.sberbank.ru/api/v1/models"

  payload={}
  headers = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {access_token}'
  }

  response = requests.request("GET", url, headers=headers, data=payload, verify = False)

  print(response.text)

# По ключу, не по токену! получаю ответ от модели. Здесь используется библиотека gigachat
# По сути две первые функции можно пропустить.
def answer_model(key,model_name,scope):
  from gigachat import GigaChat

  giga = GigaChat(
   credentials=key,
   scope=scope,
   model=model_name,
   verify_ssl_certs=False
  )

  response = giga.chat("Расскажи о себе в двух словах?")

  print(response.choices[0].message.content)


def answer_model2(key,model_name,scope):
  from langchain_gigachat.chat_models import GigaChat
  from langchain_core.messages import HumanMessage


  giga = GigaChat(
   credentials=key,
   scope=scope,
   model=model_name,
   verify_ssl_certs=False
  )

  user_message = HumanMessage(content="Прибыть, в 314 кабинет")

  response = giga.invoke([user_message])

  print(response.content)

# access_token = get_token('YmQ0MzIzODMtNzI1Ni00NzRiLWFkMDQtNjRmNDA4MThhYWEzOjdhNmI1YWNiLTA0OWMtNDI2OC1iZmM0LWM3YTRhMzAyZTJiZQ==')

# get_models(access_token)

answer_model2('YmQ0MzIzODMtNzI1Ni00NzRiLWFkMDQtNjRmNDA4MThhYWEzOjdhNmI1YWNiLTA0OWMtNDI2OC1iZmM0LWM3YTRhMzAyZTJiZQ==','GigaChat','GIGACHAT_API_PERS')





