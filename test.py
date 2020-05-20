import requests

def send_audio():
    # print('attempting to send audio')
    url = 'http://127.0.0.1:5000/upload'
    with open('/Users/DanielLongo/Desktop/accent_score/computer_recordings/admin_c.wav', 'rb') as file:
        files = {'file': file}

        req = requests.post(url, files=files, data={'correct_word': 'pajaro'})
        print(req.status_code)
        print(req.text)


if __name__ == "__main__":
    send_audio()
