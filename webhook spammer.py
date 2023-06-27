import requests

webhook_url = 'TON_WEBHOOK'
message_count = 10  

message_content = 'TON_MESSAGE'

for _ in range(message_count):
    payload = {'content': message_content}
    response = requests.post(webhook_url, json=payload)
    if response.status_code == 204:
        print('Message envoyé !')
    else:
        print('je ne peux pas envoyer le message !')