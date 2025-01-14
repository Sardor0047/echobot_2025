import requests
import os
TOKEN = os.getenv("Token")
base_u = f"https://api.telegram.org/bot{TOKEN}/" 

def get_update():
    respond = requests.get(base_u + 'getUpdates')
    return respond.json()

def get_id():
    respond = requests.get(base_u + 'getUpdates').json()
    return respond['result'][-1]['message']['chat']['id']


def send_massage(chat_id, text):
    respond = requests.get(base_u + 'sendMessage', params={
        'chat_id' : chat_id,
        'text' : text,
        'parse_mode' : 'MarkdownV2'
    })
    return respond.json()

def echo_with_MarkdownV2():
    update = get_update()

    chat_id = update['result'][-1]['message']['chat']['id']
    text = update['result'][-1]['message']['text']
    markdown = {
        'bold' : '*',
        'italic' : '_',
        'stric' : '~',
        'hidden' : '||'
    }
    send_massage(chat_id,f"{markdown['hidden']}{text}{markdown['hidden']}")

def send_photo(chat_id, photo_url):
    respond = requests.get(base_u + 'sendPhoto', params={
        'chat_id': chat_id,
        'photo': photo_url  
    })
    return respond.json()

def photo_message():
    chat_id = get_id()
    photo_url = "https://ih1.redbubble.net/image.2464906586.5278/raf,360x360,075,t,fafafa:ca443f4786.jpg"
    send_photo(chat_id,photo_url)

def send_contact(chat_id, phone_number, first_name="", last_name=""):

    respond = requests.post(base_u + 'sendContact', data={
        'chat_id': chat_id,          
        'phone_number': phone_number,  
        'first_name': first_name,     
        'last_name': last_name       
    })
    return respond.json()

def send_contact_message():
    chat_id = get_id() 
    phone_number = '+998917004711' 
    first_name = "Sardor"      
    

    send_contact(chat_id, phone_number, first_name)

def send_dice(chat_id,emoji="🎯"):
    respond = requests.get(base_u + 'sendDice',data={
        'chat_id' : chat_id,
        'emoji' : emoji
    })

    return respond.json()


def dice_massage():
    chat_id = get_id()
    send_dice(chat_id)

def send_Loacation(chat_id,latitude,longitude):
    respond = requests.get(base_u + 'sendLocation',data={
        'chat_id' : chat_id,
        'latitude':latitude,
        'longitude':longitude
    })
    return respond.json()

def message_location():
    chat_id = get_id()
    latitude = 39.6542
    longitude = 66.9598

    send_Loacation(chat_id,latitude,longitude)

def send_Vanue(chat_id,latitude,longitude):
    respond = requests.get(base_u + 'sendVanue',params={
        'chat_id':chat_id,
        'latitude':latitude,
        'longitude':longitude
    })
    return respond.json()

def message_Vanue():
    chatId = get_id()
    latitude = 39.6542
    longitude = 66.9598
    send_Vanue(chatId,latitude,longitude)

def send_Audio(chat_id,audio):
    respond = requests.get(base_u + 'sendAudio',data={
        'chat_id' : chat_id,
        'audio' : audio
    })
    return respond.json()

def messaga_audio():
    audio_url = 'https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3'
    chat_id = get_id()
    send_Audio(chat_id,audio_url)

echo_with_MarkdownV2()
send_contact_message()
photo_message()
dice_massage()
message_location()
messaga_audio()
message_Vanue()

