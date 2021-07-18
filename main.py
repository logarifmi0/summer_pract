import telebot
import requests
from telebot import types

bot = telebot.TeleBot('1700587633:AAEzqONYT99uAagbxTwluh1I9CLy1msV0Vs')


st_markup = types.ReplyKeyboardMarkup(row_width=6, resize_keyboard=True)
st_markup_btn1 = types.KeyboardButton('/start')
st_markup.add(st_markup_btn1)

topic_markup = types.ReplyKeyboardMarkup(row_width=6, resize_keyboard=True)
topic_markup_btn1 = types.KeyboardButton('Planets')
topic_markup_btn2 = types.KeyboardButton('People')
topic_markup_btn3 = types.KeyboardButton('Starships')
topic_markup_btn4 = types.KeyboardButton('Vehicles')
topic_markup_btn5 = types.KeyboardButton('Species')
topic_markup_btn6 = types.KeyboardButton('Films')
topic_markup.add(topic_markup_btn1, topic_markup_btn2, topic_markup_btn3)
topic_markup.add(topic_markup_btn4, topic_markup_btn5, topic_markup_btn6)

films_markup = types.ReplyKeyboardMarkup(row_width=6, resize_keyboard=True)
films_markup_btn1 = types.KeyboardButton('Episode 1')
films_markup_btn2 = types.KeyboardButton('Episode 2')
films_markup_btn3 = types.KeyboardButton('Episode 3')
films_markup_btn4 = types.KeyboardButton('Episode 4')
films_markup_btn5 = types.KeyboardButton('Episode 5')
films_markup_btn6 = types.KeyboardButton('Episode 6')
films_markup.add(films_markup_btn1, films_markup_btn2, films_markup_btn3)
films_markup.add(films_markup_btn4, films_markup_btn5, films_markup_btn6)

planetms = []
venicms = []
peoplems = []
starshipms = []
spcms = []
shipnf = [1, 4, 6, 7, 8, 14, 16, 18, 19, 20, 24, 25, 26, 30, 33, 34, 35]
venicnf = [1, 2, 3, 5, 9, 10, 11, 12, 13, 15, 17, 21, 22, 23, 27, 28, 29, 31, 32]


@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    chat_id = message.chat.id
    msg = bot.send_message(chat_id, 'chose topic', reply_markup=topic_markup)
    bot.register_next_step_handler(msg, asktopic)


def asktopic(message):
    chat_id = message.chat.id
    text = message.text.lower()
    if text == 'films':
        msg = bot.send_message(chat_id, 'Choose number of episod', reply_markup=films_markup)
        bot.register_next_step_handler(msg, askfilm)
    elif text == 'planets':
        msg = bot.send_message(chat_id, 'Chose planet from list')
        if len(planetms) == 0:
            i = 1
            ttr = '--------------------------------------------'
            while i < 52:
                strr = ''
                a = i
                while a < i + 10:
                    url = f'https://swapi.dev/api/planets/{a}/'
                    response = requests.get(url)
                    strr = strr + response.json()['name']
                    planetms.append(response.json()['name'].casefold())
                    strr = strr + '   '
                    a = a + 1
                i = i + 10
                bot.send_message(chat_id, strr)
                bot.send_message(chat_id, ttr)
        else:
            i = 1
            ttr = '--------------------------------------------'
            while i < 52:
                strr = ''
                a = i
                while a < i + 10:
                    strr = strr + planetms[a]
                    strr = strr + '   '
                    a = a + 1
                i = i + 10
                bot.send_message(chat_id, strr)
                bot.send_message(chat_id, ttr)
        bot.register_next_step_handler(msg, askplanet)
    elif text == 'people':
        if len(peoplems) == 0:
            i = 1
            ttr = '--------------------------------------------'
            while i < 76:
                strr = ''
                a = i
                while a < i + 8:
                    if a != 17:
                        url = f'https://swapi.dev/api/people/{a}/'
                        response = requests.get(url)
                        strr = strr + response.json()['name']
                        peoplems.append(response.json()['name'].casefold())
                        strr = strr + '   '
                    else:
                        peoplems.append('nf')
                    a = a + 1
                i = i + 8
                bot.send_message(chat_id, strr)
                bot.send_message(chat_id, ttr)
            strr = ''
            url = f'https://swapi.dev/api/people/{81}/'
            response = requests.get(url)
            peoplems.append(response.json()['name'].casefold())
            strr = strr + response.json()['name']
            strr = strr + '   '
            url = f'https://swapi.dev/api/people/{82}/'
            response = requests.get(url)
            peoplems.append(response.json()['name'].casefold())
            strr = strr + response.json()['name']
            bot.send_message(chat_id, strr)
        else:
            i = 0
            ttr = '--------------------------------------------'
            while i < 76:
                strr = ''
                a = i
                while a < i + 8:
                    if a != 16:
                        strr = strr + peoplems[a]
                        strr = strr + '   '
                    else:
                        peoplems.append('nf')
                    a = a + 1
                i = i + 8
                bot.send_message(chat_id, strr)
                bot.send_message(chat_id, ttr)
            strr = ''
            strr = strr + peoplems[80]
            strr = strr + '   '
            strr = strr + peoplems[81]
            bot.send_message(chat_id, strr)
        msg = bot.send_message(chat_id, 'Chose person from list')
        bot.register_next_step_handler(msg, askpeople)

    elif text == 'starships':
        msg = bot.send_message(chat_id, 'Chose starship from list')
        if len(starshipms) == 0:
            for i in range(1, 36):
                url = f'https://swapi.dev/api/starships/{i}/'
                response = requests.get(url)
                if i in shipnf:
                    starshipms.append("nf")
                else:
                    bot.send_message(chat_id, response.json()['name'])
                    starshipms.append(response.json()['name'].casefold())
        else:
            for i in range(35):
                if not (i + 1 in shipnf):
                    bot.send_message(chat_id, starshipms[i])
        bot.register_next_step_handler(msg, askstship)
    elif text == 'species':
        msg = bot.send_message(chat_id, 'Chose species from list')
        if len(spcms) == 0:
            for i in range(1, 38):
                url = f'https://swapi.dev/api/species/{i}/'
                response = requests.get(url)
                bot.send_message(chat_id, response.json()['name'])
                spcms.append(response.json()['name'].casefold())
        else:
            for i in range(37):
                bot.send_message(chat_id, spcms[i])
        bot.register_next_step_handler(msg, askspc)
    elif text == "vehicles":
        msg = bot.send_message(chat_id, 'Chose vehicles from list')
        if len(venicms) == 0:
            for i in range(1, 39):
                url = f'https://swapi.dev/api/vehicles/{i}/'
                response = requests.get(url)
                if i in venicnf:
                    venicms.append("nf")
                else:
                    bot.send_message(chat_id, response.json()['name'])
                    venicms.append(response.json()['name'].casefold())
        else:
            for i in range(38):
                if not (i + 1 in venicnf):
                    bot.send_message(chat_id, venicms[i])
        bot.register_next_step_handler(msg, askvenic)


def askfilm(message):
    chat_id = message.chat.id
    text = message.text.lower()
    frst, sec = text.split()
    url = f'https://swapi.dev/api/films/{sec}/'
    response = requests.get(url)
    bot.send_message(chat_id, f'Episode {sec}:  ' + response.json()['title'])
    bot.send_message(chat_id, response.json()['opening_crawl'])
    bot.send_message(chat_id, 'Director:  ' + response.json()['director'])
    bot.send_message(chat_id, 'Producer:  ' + response.json()['producer'])
    bot.send_message(chat_id, 'Release date:  ' + response.json()['release_date'])
    msg = bot.send_message(chat_id, "bot restarted then     may the 4th be with you", reply_markup=st_markup)
    bot.register_next_step_handler(msg, start_handler)


def askplanet(message):
    text = message.text.lower()
    chat_id = message.chat.id
    text = text.casefold()
    if text in planetms:
        num = planetms.index(text)
        num = num + 1
        url = f'https://swapi.dev/api/planets/{num}/'
        response = requests.get(url)
        bot.send_message(chat_id, response.json()['name'])
        bot.send_message(chat_id, "Diameter:  " + response.json()['diameter'])
        bot.send_message(chat_id, "Gravity:  " + response.json()['gravity'])
        bot.send_message(chat_id, "Climate:  " + response.json()['climate'])
        bot.send_message(chat_id, "Terrain:  " + response.json()['terrain'])
        bot.send_message(chat_id, "Population:  " + response.json()['population'])
        msg = bot.send_message(chat_id, "bot restarted then     may the 4th be with you", reply_markup=st_markup)
        bot.register_next_step_handler(msg, start_handler)
    else:
        msg = bot.send_message(chat_id, 'Please chose correct name of planet, type carefully')
        bot.register_next_step_handler(msg, askplanet)


def askstship(message):
    text = message.text.lower()
    chat_id = message.chat.id
    text = text.casefold()
    if text in starshipms:
        num = starshipms.index(text)
        num = num + 1
        url = f'https://swapi.dev/api/starships/{num}/'
        response = requests.get(url)
        bot.send_message(chat_id, response.json()['name'])
        bot.send_message(chat_id, response.json()['model'])
        bot.send_message(chat_id, "Starship class:  " + response.json()['starship_class'])
        bot.send_message(chat_id, "Manufacturer:  " + response.json()['manufacturer'])
        bot.send_message(chat_id, "Cost of starship:  " + response.json()['cost_in_credits'])
        bot.send_message(chat_id, "Crew:  " + response.json()['crew'])
        bot.send_message(chat_id, "Passengers:  " + response.json()['passengers'])
        msg = bot.send_message(chat_id, "bot restarted then     may the 4th be with you", reply_markup=st_markup)
        bot.register_next_step_handler(msg, start_handler)
    else:
        msg = bot.send_message(chat_id, 'Please chose correct name of starship, type carefully')
        bot.register_next_step_handler(msg, askstship)


def askvenic(message):
    text = message.text.lower()
    chat_id = message.chat.id
    text = text.casefold()
    if text in venicms:
        num = venicms.index(text)
        num = num + 1
        url = f'https://swapi.dev/api/vehicles/{num}/'
        response = requests.get(url)
        bot.send_message(chat_id, response.json()['name'])
        bot.send_message(chat_id, response.json()['model'])
        bot.send_message(chat_id, "Venicle class:  " + response.json()['vehicle_class'])
        bot.send_message(chat_id, "Manufacturer:  " + response.json()['manufacturer'])
        bot.send_message(chat_id, "Cost of vehicle:  " + response.json()['cost_in_credits'])
        bot.send_message(chat_id, "Max speed in atmosphere:  " + response.json()['max_atmosphering_speed'])
        bot.send_message(chat_id, "Len of vehicle:  " + response.json()['length'])
        bot.send_message(chat_id, "Crew:  " + response.json()['crew'])
        bot.send_message(chat_id, "Number of passengers:  " + response.json()['passengers'])
        msg = bot.send_message(chat_id, "bot restarted then     may the 4th be with you", reply_markup=st_markup)
        bot.register_next_step_handler(msg, start_handler)
    else:
        msg = bot.send_message(chat_id, 'Please chose correct name of vehicle, type carefully')
        bot.register_next_step_handler(msg, askvenic)


def askspc(message):
    text = message.text.lower()
    chat_id = message.chat.id
    text = text.casefold()
    if text in spcms:
        num = spcms.index(text)
        num = num + 1
        url = f'https://swapi.dev/api/species/{num}/'
        response = requests.get(url)
        bot.send_message(chat_id, response.json()['name'])
        bot.send_message(chat_id, "Average lifespan:  " + response.json()['average_lifespan'])
        bot.send_message(chat_id, "Eye colors:  " + response.json()['eye_colors'])
        bot.send_message(chat_id, "Hair colors:  " + response.json()['hair_colors'])
        bot.send_message(chat_id, "Skin colors:  " + response.json()['skin_colors'])
        bot.send_message(chat_id, "Language:  " + response.json()['language'])
        msg = bot.send_message(chat_id, "bot restarted then     may the 4th be with you", reply_markup=st_markup)
        bot.register_next_step_handler(msg, start_handler)
    else:
        msg = bot.send_message(chat_id, 'Please chose correct name of species, type carefully')
        bot.register_next_step_handler(msg, askspc)


def askpeople(message):
    text = message.text.lower()
    chat_id = message.chat.id
    text = text.casefold()
    if text in peoplems:
        num = peoplems.index(text)
        num = num + 1
        url = f'https://swapi.dev/api/people/{num}/'
        response = requests.get(url)
        bot.send_message(chat_id, response.json()['name'])
        bot.send_message(chat_id, "Birthday year:  " + response.json()['birth_year'])
        bot.send_message(chat_id, "Gender:  " + response.json()['gender'])
        bot.send_message(chat_id, "Eye color:  " + response.json()['eye_color'])
        bot.send_message(chat_id, "Hair color:  " + response.json()['hair_color'])
        bot.send_message(chat_id, "Skin color:  " + response.json()['skin_color'])
        url1 = response.json()['homeworld']
        rsp = requests.get(url1)
        bot.send_message(chat_id, "Home planet:  " + rsp.json()['name'])
        msg = bot.send_message(chat_id, "bot restarted then     may the 4th be with you", reply_markup=st_markup)
        bot.register_next_step_handler(msg, start_handler)
    else:
        msg = bot.send_message(chat_id, 'Please chose correct name of person, type carefully')
        bot.register_next_step_handler(msg, askpeople)


bot.polling()
