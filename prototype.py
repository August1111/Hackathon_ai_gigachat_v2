import requests
import json
from langchain_gigachat.chat_models import GigaChat
from langchain_core.messages import HumanMessage
from langchain_core.messages import HumanMessage
from langchain_core.messages import AIMessage
from langchain_core.messages import ToolMessage
from langchain_core.messages import SystemMessage
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import base64

# Что нужно:
# Понять зачем вообще получать токены, если можно авторизоваться по ключу?
# Создать именно ai агента с памятью ит.д.
# Почему-то возвращает пустой результат по звуку

#1. Подключиться и получить текстовый ответ (работает)

def answer_model2(key,model_name,scope):

  giga = GigaChat(
    # base_url = .... прописать, когда будем подключаться к стенду
   credentials=key,
   scope=scope,
   model=model_name,
   verify_ssl_certs=False
  )

  user_message = HumanMessage(content="Прибыть, в 314 кабинет")

  response = giga.invoke([user_message])

  print(response.content)

# answer_model2('YmQ0MzIzODMtNzI1Ni00NzRiLWFkMDQtNjRmNDA4MThhYWEzOjdhNmI1YWNiLTA0OWMtNDI2OC1iZmM0LWM3YTRhMzAyZTJiZQ==','GigaChat','GIGACHAT_API_PERS')

#2. Подключиться и отправить картинку, в ответ нужно получить расшифрованный текст (работает)
# Загружаем картинку и конвертируем в base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
def load_image_to_giga():
    # Указываем путь к картинке
    image_path = r"C:\Users\artem\YandexDisk\Hackathon_ai_gigachat\Hackathon_ai_gigachat_v2\4giga.jpg"
    image_base64 = load_image_as_base64(image_path)

    # Создаем сообщение с изображением
    message_with_image = HumanMessage(
        content=[
            {"type": "text", "text": "Пожалуйста, распознай текст на этом изображении."},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
    )

    # Инициализируем GigaChat
    chat = GigaChat(
        credentials='YmQ0MzIzODMtNzI1Ni00NzRiLWFkMDQtNjRmNDA4MThhYWEzOjdhNmI1YWNiLTA0OWMtNDI2OC1iZmM0LWM3YTRhMzAyZTJiZQ==',  # замените на свой ключ
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS",  
        model="GigaChat-2-Max",
        auto_upload_images=True
    )

    # Отправляем сообщение и получаем результат
    response = chat.invoke([message_with_image])
    print(response.content)     

#2. Подключиться и отправить картинку, в ответ нужно получить расшифрованный текст (работает с использованием "GigaChat-2-Max")
# Загружаем картинку и конвертируем в base64
def load_image_as_base64(image_path):
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")
    
def load_image_to_giga():

    image_path = r"C:\Users\artem\YandexDisk\Hackathon_ai_gigachat\Hackathon_ai_gigachat_v2\4giga.jpg"
    image_base64 = load_image_as_base64(image_path)

    message_with_image = HumanMessage(
        content=[
            {"type": "text", "text": "Пожалуйста, распознай текст на этом изображении."},
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                }
            }
        ]
    )

    chat = GigaChat(
        credentials='YmQ0MzIzODMtNzI1Ni00NzRiLWFkMDQtNjRmNDA4MThhYWEzOjdhNmI1YWNiLTA0OWMtNDI2OC1iZmM0LWM3YTRhMzAyZTJiZQ==', 
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS",  
        model="GigaChat-2-Max",
        auto_upload_images=True
    )

    response = chat.invoke([message_with_image])
    print(response.content)   

#3. Подключиться и отправить звуковую дорожку, в ответ нужно получить расшифрованный текст ()
# Не работает, отдаёт - На данный момент у меня нет возможности обрабатывать аудиофайлы или извлекать информацию из звуковых записей. Однако вы можете описать содержание аудио текстом — тогда я смогу помочь вам проанализировать или 
#обработать эту информацию! Делаем через SaluteSpeech, см. след. пункт
def load_audio_as_base64(audio_path):
    with open(audio_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

def audio_to_giga():
    audio_path = r"C:\Users\artem\YandexDisk\Hackathon_ai_gigachat\Hackathon_ai_gigachat_v2\4giga.mp3"
    audio_base64 = load_audio_as_base64(audio_path)

    message_with_audio = HumanMessage(
        content=[
            {"type": "text", "text": "Пожалуйста, расшифруй это аудио."},
            {
                "type": "audio_url", 
                "audio_url": {
                    "url": f"data:audio/mp3;base64,{audio_base64}"
                }
            }
        ]
    )

    chat = GigaChat(
        credentials="YmQ0MzIzODMtNzI1Ni00NzRiLWFkMDQtNjRmNDA4MThhYWEzOjdhNmI1YWNiLTA0OWMtNDI2OC1iZmM0LWM3YTRhMzAyZTJiZQ==", 
        verify_ssl_certs=False,
        scope="GIGACHAT_API_PERS",    
        model="GigaChat-2-Max",
        auto_upload_images=True  
    )

    response = chat.invoke([message_with_audio])
    print(response.content)

#Отправляем аудио в SaluteAPI. Тут сначала поавторизационному ключу надо получить токен а потом с ним стучаться 
#Почему то возвращает пустой результат, но запрос явно проходит
def get_token_4salute():
    url = "https://ngw.devices.sberbank.ru:9443/api/v2/oauth"

    payload={
    'scope': 'SALUTE_SPEECH_PERS'
    }
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept': 'application/json',
    'RqUID': '21c4a7b6-ec09-463e-8530-6784af9f8d11',
    'Authorization': 'Basic Y2E1ZWM4MDUtZDhhNi00ZWNkLThhNTEtZDRiOTFmMjM1Y2M1OjQyNWVkOGRmLWNiOTQtNDliOS04NDAwLTFjNGY3MzFiMTIzYg=='
    }

    response = requests.request("POST", url, headers=headers, data=payload, verify=False)
    result = response.json()
    return result["access_token"]

def audio_to_salute():
    url = "https://smartspeech.sber.ru/rest/v1/speech:recognize"

    token = get_token_4salute()

    # Заголовки запроса
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": 'audio/mpeg'
    }

    # Открытие аудио файла в бинарном режиме
    with open(r"C:\Users\artem\YandexDisk\Hackathon_ai_gigachat\Hackathon_ai_gigachat_v2\4giga.wav", "rb") as audio_file:
        audio_data = audio_file.read()

    # Отправка POST запроса
    response = requests.post(url, headers=headers, data=audio_data, verify=False)

    # Обработка ответа
    if response.status_code == 200:
        result = response.json()
        print("Весь ответ API:", result)
        return result["result"]
    else:
        print("Ошибка:", response.status_code, response.text)
        return response.text

audio_to_salute()