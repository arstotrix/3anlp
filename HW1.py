import vk_api

# здесь нужно ввести данные своего аккаунта
# когда будете сдавать, не забудьте убрать эти две строчки из ноутбука
user = '89773410007' # вставьте сюда свой номер телефона
password = 'gl0rytoarst0tzka0709' # вставьте сюда свой пароль

# авторизация
vk_session = vk_api.VkApi(login=user, password=password)
vk_session.auth()

vk = vk_session.get_api() # объект с API
publics = ["futureisnow",
           "eternalclassic",
           "ukrlit_memes",
           "ukrainer_net",
           "amanzohel",
           "barg_kurumk_culture"]
items = {} # ключи — это паблики
for pub in publics:
    posts = vk.wall.get(domain=pub, count=100)
    items[pub] = posts

corpora = {}
for item in items:
    gneg = []
    for post in items[item]:
        if post == 'items':
            for i in items[item][post]:
                comments = vk.wall.getComments(owner_id=i['owner_id'], post_id=i['id'], count=100)
                for comment in comments:
                    if comment == 'items':
                        data = comments[comment]
                        for d in data:
                            try:
                                text = d['text']
                                if len(text)>10:
                                    gneg.append(text)
                            except KeyError:
                                print('...')
    corpora[item] = gneg
    print(gneg)

