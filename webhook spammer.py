import requests

webhook_url = 'TON_WEBHOOK'
nombre_message = 10  

contenu_message = 'TON_MESSAGE'

for _ in range(nombre_message):
    payload = {'content': contenu_message}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print('Message envoyé !')
    else:
        print('je ne peux pas envoyer le message !')
