from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.client.default import DefaultBotProperties
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from api import TOKEN
import asyncio
import random

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode="HTML"))
dp = Dispatcher()

#Бд пользователей
user_data = {}

#Словарь из слов и фраз (100 слов и 100 фраз с эмодзи по смыслу)
words = [
    {"word": "яблоко", "translation": "алма", "emoji": "🍎"},
    {"word": "дом", "translation": "үй", "emoji": "🏠"},
    {"word": "книга", "translation": "кітап", "emoji": "📖"},
    {"word": "солнце", "translation": "күн", "emoji": "☀"},
    {"word": "вода", "translation": "су", "emoji": "💧"},
    {"word": "дерево", "translation": "ағаш", "emoji": "🌳"},
    {"word": "город", "translation": "қала", "emoji": "🏙"},
    {"word": "машина", "translation": "автомобиль", "emoji": "🚗"},
    {"word": "человек", "translation": "адам", "emoji": "👤"},
    {"word": "женщина", "translation": "әйел", "emoji": "👩"},
    {"word": "мужчина", "translation": "ер", "emoji": "👨"},
    {"word": "ребенок", "translation": "бала", "emoji": "👶"},
    {"word": "друг", "translation": "дос", "emoji": "🤝"},
    {"word": "семья", "translation": "отбасы", "emoji": "👪"},
    {"word": "работа", "translation": "жұмыс", "emoji": "💼"},
    {"word": "школа", "translation": "мектеп", "emoji": "🏫"},
    {"word": "учитель", "translation": "мұғалім", "emoji": "👩🏫"},
    {"word": "ученик", "translation": "оқушы", "emoji": "🎒"},
    {"word": "улица", "translation": "көше", "emoji": "🛣"},
    {"word": "дорога", "translation": "жол", "emoji": "🛣"},
    {"word": "река", "translation": "өзен", "emoji": "🌊"},
    {"word": "гора", "translation": "тау", "emoji": "⛰"},
    {"word": "лес", "translation": "орман", "emoji": "🌲"},
    {"word": "поле", "translation": "дала", "emoji": "🌾"},
    {"word": "цветок", "translation": "гүл", "emoji": "🌸"},
    {"word": "трава", "translation": "шөп", "emoji": "🌿"},
    {"word": "небо", "translation": "аспан", "emoji": "🌌"},
    {"word": "звезда", "translation": "жұлдыз", "emoji": "⭐"},
    {"word": "луна", "translation": "ай", "emoji": "🌙"},
    {"word": "дождь", "translation": "жаңбыр", "emoji": "🌧"},
    {"word": "снег", "translation": "қар", "emoji": "❄"},
    {"word": "ветер", "translation": "жел", "emoji": "🌪"},
    {"word": "огонь", "translation": "от", "emoji": "🔥"},
    {"word": "земля", "translation": "жер", "emoji": "🌍"},
    {"word": "воздух", "translation": "ауа", "emoji": "💨"},
    {"word": "хлеб", "translation": "нан", "emoji": "🍞"},
    {"word": "молоко", "translation": "сүт", "emoji": "🥛"},
    {"word": "мясо", "translation": "ет", "emoji": "🥩"},
    {"word": "рыба", "translation": "балық", "emoji": "🐟"},
    {"word": "фрукт", "translation": "жеміс", "emoji": "🍇"},
    {"word": "овощ", "translation": "көкөніс", "emoji": "🥦"},
    {"word": "чай", "translation": "шәй", "emoji": "🍵"},
    {"word": "кофе", "translation": "кофе", "emoji": "☕"},
    {"word": "сахар", "translation": "қант", "emoji": "🍚"},
    {"word": "соль", "translation": "тұз", "emoji": "🧂"},
    {"word": "масло", "translation": "май", "emoji": "🧈"},
    {"word": "рис", "translation": "күріш", "emoji": "🍚"},
    {"word": "суп", "translation": "сорпа", "emoji": "🍲"},
    {"word": "стол", "translation": "үстел", "emoji": "🪑"},
    {"word": "стул", "translation": "орындық", "emoji": "🪑"},
    {"word": "кровать", "translation": "төсек", "emoji": "🛏"},
    {"word": "окно", "translation": "терезе", "emoji": "🪟"},
    {"word": "дверь", "translation": "есік", "emoji": "🚪"},
    {"word": "стена", "translation": "қабырға", "emoji": "🧱"},
    {"word": "пол", "translation": "еден", "emoji": "🧹"},
    {"word": "потолок", "translation": "төбе", "emoji": "🏠"},
    {"word": "лампа", "translation": "шам", "emoji": "💡"},
    {"word": "телевизор", "translation": "теледидар", "emoji": "📺"},
    {"word": "компьютер", "translation": "компьютер", "emoji": "💻"},
    {"word": "телефон", "translation": "телефон", "emoji": "📱"},
    {"word": "часы", "translation": "сағат", "emoji": "⌚"},
    {"word": "деньги", "translation": "ақша", "emoji": "💵"},
    {"word": "кошелек", "translation": "әмиян", "emoji": "👛"},
    {"word": "ключ", "translation": "кілт", "emoji": "🔑"},
    {"word": "сумка", "translation": "сөмке", "emoji": "👜"},
    {"word": "одежда", "translation": "киім", "emoji": "👕"},
    {"word": "обувь", "translation": "аяқ киім", "emoji": "👟"},
    {"word": "шапка", "translation": "бас киім", "emoji": "🧢"},
    {"word": "рубашка", "translation": "жейде", "emoji": "👔"},
    {"word": "брюки", "translation": "шалбар", "emoji": "👖"},
    {"word": "платье", "translation": "көйлек", "emoji": "👗"},
    {"word": "куртка", "translation": "күрте", "emoji": "🧥"},
    {"word": "зима", "translation": "қыс", "emoji": "❄"},
    {"word": "весна", "translation": "көктем", "emoji": "🌱"},
    {"word": "лето", "translation": "жаз", "emoji": "🌞"},
    {"word": "осень", "translation": "күз", "emoji": "🍂"},
    {"word": "утро", "translation": "таң", "emoji": "🌅"},
    {"word": "день", "translation": "күн", "emoji": "🌞"},
    {"word": "вечер", "translation": "кеш", "emoji": "🌆"},
    {"word": "ночь", "translation": "түн", "emoji": "🌃"},
    {"word": "время", "translation": "уақыт", "emoji": "⏳"},
    {"word": "час", "translation": "сағат", "emoji": "🕒"},
    {"word": "минута", "translation": "минут", "emoji": "⏱"},
    {"word": "секунда", "translation": "секунд", "emoji": "⏲"},
    {"word": "неделя", "translation": "апта", "emoji": "📅"},
    {"word": "месяц", "translation": "ай", "emoji": "🌙"},
    {"word": "год", "translation": "жыл", "emoji": "📆"},
    {"word": "сегодня", "translation": "бүгін", "emoji": "📅"},
    {"word": "завтра", "translation": "ертең", "emoji": "⏭"},
    {"word": "вчера", "translation": "кеше", "emoji": "⏮"},
    {"word": "сейчас", "translation": "қазір", "emoji": "🕒"},
    {"word": "потом", "translation": "кейін", "emoji": "⏭"},
    {"word": "здесь", "translation": "осында", "emoji": "📍"},
    {"word": "там", "translation": "онда", "emoji": "🔭"},
    {"word": "везде", "translation": "барлық жерде", "emoji": "🌍"},
    {"word": "никогда", "translation": "ешқашан", "emoji": "🚫"},
    {"word": "всегда", "translation": "әрқашан", "emoji": "♾"},
]

phrases = [
    {"phrase": "Как дела?", "translation": "Қалың қалай?", "emoji": "🙂"},
    {"phrase": "Доброе утро", "translation": "Қайырлы таң", "emoji": "🌄"},
    {"phrase": "Спасибо", "translation": "Рахмет", "emoji": "🙏"},
    {"phrase": "Пожалуйста", "translation": "Өтінемін", "emoji": "🤲"},
    {"phrase": "Что нового?", "translation": "Жаңалық қандай?", "emoji": "🆕"},
    {"phrase": "Как тебя зовут?", "translation": "Сенің атың кім?", "emoji": "👤"},
    {"phrase": "Меня зовут...", "translation": "Менің атым...", "emoji": "📛"},
    {"phrase": "Где ты живешь?", "translation": "Сен қайда тұрасың?", "emoji": "🏠"},
    {"phrase": "Я живу в...", "translation": "Мен... тұрамын", "emoji": "📍"},
    {"phrase": "Сколько тебе лет?", "translation": "Сенің жасың қанша?", "emoji": "🎂"},
    {"phrase": "Мне ... лет", "translation": "Менің жасым...", "emoji": "🎂"},
    {"phrase": "Ты говоришь по-казахски?", "translation": "Сен қазақша сөйлейсің бе?", "emoji": "🗣"},
    {"phrase": "Я не понимаю", "translation": "Мен түсінбеймін", "emoji": "😕"},
    {"phrase": "Повтори, пожалуйста", "translation": "Қайталап беріңізші", "emoji": "🔄"},
    {"phrase": "Где туалет?", "translation": "Дәретхана қайда?", "emoji": "🚻"},
    {"phrase": "Сколько это стоит?", "translation": "Бұл қанша тұрады?", "emoji": "💲"},
    {"phrase": "Я голоден", "translation": "Мен ашымын", "emoji": "🍔"},
    {"phrase": "Я хочу пить", "translation": "Мен сусадым", "emoji": "🥤"},
    {"phrase": "Где остановка автобуса?", "translation": "Автобус аялдамасы қайда?", "emoji": "🚏"},
    {"phrase": "Как добраться до...?", "translation": "... қалай баруға болады?", "emoji": "🗺"},
    {"phrase": "У меня есть вопрос", "translation": "Менің сұрағым бар", "emoji": "❓"},
    {"phrase": "Я потерялся", "translation": "Мен адасып қалдым", "emoji": "😵"},
    {"phrase": "Помогите мне", "translation": "Маған көмектесіңіз", "emoji": "🆘"},
    {"phrase": "Где больница?", "translation": "Аурухана қайда?", "emoji": "🏥"},
    {"phrase": "Мне нужен врач", "translation": "Маған дәрігер керек", "emoji": "👨⚕"},
    {"phrase": "У меня болит голова", "translation": "Менің басым ауырады", "emoji": "🤕"},
    {"phrase": "Где можно поесть?", "translation": "Қайда тамақтануға болады?", "emoji": "🍽"},
    {"phrase": "Я люблю тебя", "translation": "Мен сені жақсы көремін", "emoji": "❤"},
    {"phrase": "До свидания", "translation": "Сау болыңыз", "emoji": "👋"},
    {"phrase": "Удачи!", "translation": "Сәттілік!", "emoji": "🍀"},
    {"phrase": "Сколько времени?", "translation": "Сағат қанша?", "emoji": "🕒"},
    {"phrase": "Я устал", "translation": "Мен шаршадым", "emoji": "😴"},
    {"phrase": "Я счастлив", "translation": "Мен бақыттымын", "emoji": "😊"},
    {"phrase": "Это дорого", "translation": "Бұл қымбат", "emoji": "💸"},
    {"phrase": "Это дешево", "translation": "Бұл арзан", "emoji": "💰"},
    {"phrase": "Где можно найти такси?", "translation": "Қайда такси табуға болады?", "emoji": "🚕"},
    {"phrase": "Мне нужно в аэропорт", "translation": "Маған әуежайға бару керек", "emoji": "✈"},
    {"phrase": "Где вокзал?", "translation": "Вокзал қайда?", "emoji": "🚉"},
    {"phrase": "Это вкусно", "translation": "Бұл дәмді", "emoji": "😋"},
    {"phrase": "Это невкусно", "translation": "Бұл дәмсіз", "emoji": "🤢"},
    {"phrase": "Я хочу домой", "translation": "Мен үйге баруды қалаймын", "emoji": "🏡"},
    {"phrase": "Где можно отдохнуть?", "translation": "Қайда дем алуға болады?", "emoji": "😌"},
    {"phrase": "Я заблудился", "translation": "Мен адасып қалдым", "emoji": "🗺"},
    {"phrase": "Где можно позвонить?", "translation": "Қайда телефон соғуға болады?", "emoji": "📞"},
    {"phrase": "У меня есть билет", "translation": "Менің билетім бар", "emoji": "🎫"},
    {"phrase": "Где можно купить билет?", "translation": "Қайда билет сатып алуға болады?", "emoji": "🎟"},
    {"phrase": "Я хочу путешествовать", "translation": "Мен саяхаттағым келеді", "emoji": "✈"},
    {"phrase": "Где можно арендовать машину?", "translation": "Қайда машина жалға алуға болады?", "emoji": "🚗"},
    {"phrase": "Где находится отель?", "translation": "Қонақ үй қайда орналасқан?", "emoji": "🏨"},
    {"phrase": "Можно счет, пожалуйста?", "translation": "Шотты әкеліңізші?", "emoji": "🧾"},
    {"phrase": "Какой у вас Wi-Fi пароль?", "translation": "Wi-Fi паролі қандай?", "emoji": "📶"},
    {"phrase": "Где ближайший банкомат?", "translation": "Ең жақын банкомат қайда?", "emoji": "🏧"},
    {"phrase": "У вас есть меню на казахском?", "translation": "Сізде қазақша мәзір бар ма?", "emoji": "📋"},
]

# Главное меню
def main_menu():
    builder = ReplyKeyboardBuilder()
    builder.row(types.KeyboardButton(text="📖 Новое слово"))
    builder.row(types.KeyboardButton(text="💬 Новая фраза"))
    builder.row(
        types.KeyboardButton(text="📝 Тест"), 
        types.KeyboardButton(text="🔁 Повторить ошибки")
    )
    builder.row(
        types.KeyboardButton(text="🎮 Игра в слова"), 
        types.KeyboardButton(text="📚 Грамматика")
    )
    builder.row(
        types.KeyboardButton(text="📊 Прогресс"), 
        types.KeyboardButton(text="ℹ Помощь")
    )
    return builder.as_markup(resize_keyboard=True)

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    user_id = message.from_user.id
    user_data[user_id] = {
        "used_words": [],
        "learned_words": [],
        "mistakes": [],
        "used_phrases": [],
        "learned_phrases": [],
        "word_game": None
    }
    await message.answer(
        f"🇰🇿 Сәлем, {message.from_user.first_name}!\n"
        "Я помогу тебе выучить казахский язык! 🎓\n"
        "Выбирай действие в меню ниже 👇",
        reply_markup=main_menu()
    )

@dp.message(lambda message: message.text == "📖 Новое слово")
async def send_new_word(message: types.Message):
    user_id = message.from_user.id
    data = user_data.setdefault(user_id, {
        "used_words": [], "learned_words": [], "mistakes": [],
        "used_phrases": [], "learned_phrases": [], "word_game": None
    })
    
    available = [w for w in words if w not in data["used_words"]]
    
    if not available:
        await message.answer("🎉 Ты изучил все слова! 🥳")
        return
    
    word = random.choice(available)
    data["used_words"].append(word)
    await message.answer(f"{word['emoji']} <b>Слово:</b> {word['translation']}\n📝 <b>Перевод:</b> {word['word']}")


@dp.message(lambda message: message.text == "💬 Новая фраза")
async def send_new_phrase(message: types.Message):
    user_id = message.from_user.id
    data = user_data.setdefault(user_id, {
        "used_words": [], "learned_words": [], "mistakes": [],
        "used_phrases": [], "learned_phrases": [], "word_game": None
    })
    
    available = [p for p in phrases if p not in data["used_phrases"]]
    
    if not available:
        await message.answer("🎉 Ты изучил все фразы! 🚀")
        return
    
    phrase = random.choice(available)
    data["used_phrases"].append(phrase)
    await message.answer(f"{phrase['emoji']} <b>Фраза:</b> {phrase['translation']}\n🗣 <b>Перевод:</b> {phrase['phrase']}")


@dp.message(lambda message: message.text == "📝 Тест")
async def start_test(message: types.Message):
    user_id = message.from_user.id
    data = user_data.get(user_id, {})
    
    
    pool = data.get("mistakes", []) + [
        item for item in data.get("used_words", []) 
        if item not in data.get("learned_words", [])
    ] + [
        item for item in data.get("used_phrases", []) 
        if item not in data.get("learned_phrases", [])
    ]
    
    
    seen = set()
    unique_pool = []
    for item in pool:
        identifier = item.get("word") or item.get("phrase")
        if identifier not in seen:
            seen.add(identifier)
            unique_pool.append(item)
    
    if not unique_pool:
        await message.answer("🎉 Все материалы изучены! Добавьте новые через меню")
        return
    
    item = random.choice(unique_pool)
    is_word = "word" in item
    question = item["word"] if is_word else item["phrase"]
    correct = item["translation"]
    
    options = [correct]
    source = words if is_word else phrases
    while len(options) < 3:
        random_item = random.choice(source)
        if random_item["translation"] not in options:
            options.append(random_item["translation"])
    
    random.shuffle(options)
    
    builder = InlineKeyboardBuilder()
    for option in options:
        builder.button(text=option, callback_data=f"test_{option}")
    builder.adjust(1)
    
    data["current_test"] = item
    await message.answer(f"❓ <b>Перевод:</b> {question}\nВыбери правильный вариант:", reply_markup=builder.as_markup())

# Проверка теста
@dp.callback_query(lambda callback: callback.data.startswith("test_"))
async def check_test(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    data = user_data.get(user_id, {})
    item = data.get("current_test")
    
    if not item:
        await callback.answer("⚠ Тест устарел!")
        return
    
    answer = callback.data.split("_")[1]
    correct = item["translation"]
    
    if answer == correct:
        target = "learned_words" if "word" in item else "learned_phrases"
        if item not in data[target]:
            data[target].append(item)
        
        if item in data.get("mistakes", []):
            data["mistakes"].remove(item)
        await callback.message.edit_text("✅ <b>Правильно!</b> 🎉")
    else:
        
        if item not in data.get("mistakes", []):
            data.setdefault("mistakes", []).append(item)
        await callback.message.edit_text(f"❌ <b>Ошибка!</b> Правильно: {correct}")
    
    data.pop("current_test", None)
    await callback.answer()

#Повторение ошибок
@dp.message(lambda message: message.text == "🔁 Повторить ошибки")
async def repeat_mistakes(message: types.Message):
    user_id = message.from_user.id
    data = user_data.get(user_id, {})
    
    if not data.get("mistakes"):
        await message.answer("🎉 У тебя нет ошибок для повторения!")
        return
    
    item = random.choice(data["mistakes"])
    is_word = "word" in item
    question = item["word"] if is_word else item["phrase"]
    correct = item["translation"]
    
    options = [correct]
    source = words if is_word else phrases
    while len(options) < 3:
        random_item = random.choice(source)
        if random_item["translation"] not in options:
            options.append(random_item["translation"])
    
    random.shuffle(options)
    
    builder = InlineKeyboardBuilder()
    for option in options:
        builder.button(text=option, callback_data=f"test_{option}")
    builder.adjust(1)
    
    data["current_test"] = item
    await message.answer(f"🔁 <b>Повторяем ошибку:</b>\n❓ Перевод: {question}", reply_markup=builder.as_markup())

#Игра в слова
@dp.message(lambda message: message.text == "🎮 Игра в слова")
async def start_word_game(message: types.Message):
    user_id = message.from_user.id
    data = user_data.get(user_id, {})
    
    if not data.get("learned_words"):
        await message.answer("📚 Сначала изучи несколько слов через кнопку '📖 Новое слово'")
        return
    
    word = random.choice(data["learned_words"])
    scrambled = ''.join(random.sample(word["translation"], len(word["translation"])))
    
    data["word_game"] = {
        "answer": f"{word['translation']}-{word['word']}",
        "attempts": 3
    }
    
    await message.answer(
        f"🔠 <b>Угадай слово:</b> {scrambled}\n"
        "Формат: <code>казахское-русское</code>\n"
        "У тебя 3 попытки! 💪"
    )

@dp.message(lambda message: user_data.get(message.from_user.id, {}).get("word_game"))
async def handle_game(message: types.Message):
    user_id = message.from_user.id
    data = user_data.get(user_id, {})
    
    # Если выбрана команда из меню - отменяем игру
    if message.text in ["📖 Новое слово", "💬 Новая фраза", "📝 Тест", 
                      "🔁 Повторить ошибки", "🎮 Игра в слова", 
                      "📚 Грамматика", "📊 Прогресс", "ℹ Помощь"]:
        data["word_game"] = None
        await message.answer("🔄 Игра отменена")
        return
    
    game = data.get("word_game")
    if not game:
        return
    
    try:
        user_kz, user_ru = message.text.strip().split("-")
        user_answer = (user_kz.strip().lower(), user_ru.strip().lower())
        correct = tuple(game["answer"].lower().split("-"))
        
        if user_answer == correct:
            await message.answer("🎉 <b>Правильно!</b> Ты молодец! 🥳")
            del data["word_game"]
        else:
            game["attempts"] -= 1
            if game["attempts"] > 0:
                await message.answer(f"❌ Неверно! Осталось попыток: {game['attempts']}\nПопробуй еще раз 💪")
            else:
                await message.answer(f"😞 Попытки закончились. Правильный ответ:\n<b>{game['answer'].split('-')[0]}</b> - <b>{game['answer'].split('-')[1]}</b>")
                del data["word_game"]
                
    except ValueError:
        await message.answer("⚠ Неправильный формат! Используй: <code>слово-перевод</code>")

GRAMMAR_RESPONSES = {
    "case": (
        "📌 <b>7 падежей казахского языка:</b>\n\n"
        "1. <u>Именительный</u> (атау септік)\n"
        "   • Вопросы: <i>Кім? Не?</i>\n"
        "   • Окончания: базовая форма\n"
        "   • Примеры:\n"
        "     - <code>Үй</code> (дом)\n"
        "     - <code>Қыз</code> (девочка)\n\n"
        "2. <u>Родительный</u> (ілік септік)\n"
        "   • Вопросы: <i>Кімнің? Нең?</i>\n"
        "   • Окончания: -дың/-дің/-тың/-тің\n"
        "   • Примеры:\n"
        "     - <code>Үйдің</code> (дома)\n"
        "     - <code>Қыздың</code> (девочки)\n\n"
        "3. <u>Дательный</u> (барыс септік)\n"
        "   • Вопросы: <i>Кімге? Неге?</i>\n"
        "   • Окончания: -ға/-ге/-қа/-ке\n"
        "   • Примеры:\n"
        "     - <code>Үйге</code> (к дому)\n"
        "     - <code>Қызға</code> (девочке)\n\n"
        "4. <u>Винительный</u> (табыс септік)\n"
        "   • Вопросы: <i>Кімді? Неді?</i>\n"
        "   • Окончания: -ды/-ді/-ты/-ті\n"
        "   • Примеры:\n"
        "     - <code>Үйді</code> (дом)\n"
        "     - <code>Қызды</code> (девочку)\n\n"
        "5. <u>Местный</u> (жатыс септік)\n"
        "   • Вопросы: <i>Кімде? Неде?</i>\n"
        "   • Окончания: -да/-де/-та/-те\n"
        "   • Примеры:\n"
        "     - <code>Үйде</code> (в доме)\n"
        "     - <code>Қызда</code> (у девочки)\n\n"
        "6. <u>Исходный</u> (шығыс септік)\n"
        "   • Вопросы: <i>Кімнен? Неден?</i>\n"
        "   • Окончания: -дан/-ден/-тан/-тен\n"
        "   • Примеры:\n"
        "     - <code>Үйден</code> (из дома)\n"
        "     - <code>Қыздан</code> (от девочки)\n\n"
        "7. <u>Творительный</u> (көмектес септік)\n"
        "   • Вопросы: <i>Кіммен? Немен?</i>\n"
        "   • Окончания: -мен/-бен/-пен\n"
        "   • Примеры:\n"
        "     - <code>Үймен</code> (с домом)\n"
        "     - <code>Қызбен</code> (с девочкой)"
    ),
    "tense": (
        "⏳ <b>Времена глаголов:</b>\n\n"
        "1. <u>Настоящее время</u> (осы шақ):\n"
        "   • Окончания: -амын/-емін, -асың/-есің, -ады/-еді\n"
        "   • Примеры:\n"
        "     - <code>Мен жазамын</code> (Я пишу)\n"
        "     - <code>Сен жазaсың</code> (Ты пишешь)\n"
        "     - <code>Ол жазaды</code> (Он пишет)\n\n"
        "2. <u>Прошедшее определенное</u> (өткен шақ):\n"
        "   • Окончания: -дым/-дім, -дың/-дің, -ды/-ді\n"
        "   • Примеры:\n"
        "     - <code>Мен жаздым</code> (Я написал)\n"
        "     - <code>Сен жаздың</code> (Ты написал)\n"
        "     - <code>Ол жазды</code> (Он написал)\n\n"
        "3. <u>Будущее время</u> (келер шақ):\n"
        "   • Окончания: -амын/-емін (намерение), -ар/-ер (нейтральное)\n"
        "   • Примеры:\n"
        "     - <code>Мен жазaмын</code> (Я буду писать)\n"
        "     - <code>Ол жазaр</code> (Он напишет)"
    ),
    "conjugation": (
        "🔄 <b>Спряжения глаголов:</b>\n\n"
        "1. <u>Глаголы на гласные</u>:\n"
        "   • Основа: <code>жазу</code> (писать)\n"
        "   • Спряжение:\n"
        "     - <code>Мен жазамын</code>\n"
        "     - <code>Сен жазасың</code>\n"
        "     - <code>Ол жазады</code>\n\n"
        "2. <u>Глаголы на согласные</u>:\n"
        "   • Основа: <code>оқу</code> (читать)\n"
        "   • Спряжение:\n"
        "     - <code>Мен оқимын</code>\n"
        "     - <code>Сен оқисың</code>\n"
        "     - <code>Ол оқиды</code>\n\n"
        "3. <u>Отрицательная форма</u>:\n"
        "   • Частица: <code>-ма/-ме/-ба/-бе</code>\n"
        "   • Примеры:\n"
        "     - <code>Жазбадым</code> (Я не писал)\n"
        "     - <code>Оқымады</code> (Он не читал)"
    ),
    "plural": (
        "👥 <b>Множественное число:</b>\n\n"
        "1. <u>Основные окончания</u>:\n"
        "   • После гласных: <code>-лар/-лер</code>\n"
        "     - <code>үй → үйлер</code> (дома)\n"
        "   • После звонких согласных: <code>-дар/-дер</code>\n"
        "     - <code>кітап → кітаптар</code> (книги)\n"
        "   • После глухих согласных: <code>-тар/-тер</code>\n"
        "     - <code>адам → адамдар</code> (люди)\n\n"
        "2. <u>Особые случаи</u>:\n"
        "   • Смена гласных: <code>қыз → қыздар</code>\n"
        "   • Удвоение согласных: <code>бала → балалар</code>\n\n"
        "3. <u>Исключения</u>:\n"
        "   • <code>көз → көздер</code> (глаза)\n"
        "   • <code>қол → қолдар</code> (руки)"
    )
}

@dp.message(lambda message: message.text == "📚 Грамматика")
async def show_grammar_menu(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.button(text="📌 Падежи", callback_data="grammar_case")
    builder.button(text="⏳ Времена", callback_data="grammar_tense")
    builder.button(text="🔄 Спряжения", callback_data="grammar_conjugation")
    builder.button(text="👥 Множественное", callback_data="grammar_plural")
    builder.adjust(1)
    await message.answer("📚 Выбери тему грамматики:", reply_markup=builder.as_markup())

@dp.callback_query(lambda callback: callback.data.startswith("grammar_"))
async def send_grammar(callback: types.CallbackQuery):
    topic = callback.data.split("_")[1]
    await callback.message.answer(GRAMMAR_RESPONSES.get(topic, "🚧 Раздел в разработке"))
    await callback.answer()

#Прогресс
@dp.message(lambda message: message.text == "📊 Прогресс")
async def show_progress(message: types.Message):
    user_id = message.from_user.id
    data = user_data.get(user_id, {})
    progress = (
        f"📊 <b>Твой прогресс:</b>\n\n"
        f"📖 Изучено слов: {len(data.get('learned_words', []))}\n"
        f"💬 Изучено фраз: {len(data.get('learned_phrases', []))}\n"
        f"⚠ Активных ошибок: {len(data.get('mistakes', []))}"
    )
    await message.answer(progress)

#Помощь
@dp.message(lambda message: message.text == "ℹ Помощь")
async def show_help(message: types.Message):
    help_text = (
        "🆘 <b>Доступные команды:</b>\n\n"
        "📖 Новое слово - Изучить новое слово\n"
        "💬 Новая фраза - Изучить новую фразу\n"
        "📝 Тест - Проверить знания\n"
        "🔁 Повторить ошибки - Работа над ошибками\n"
        "🎮 Игра в слова - Тренировка в игровой форме\n"
        "📚 Грамматика - Правила казахского языка\n"
        "📊 Прогресс - Статистика обучения\n"
        "ℹ Помощь - Это сообщение"
    )
    await message.answer(help_text)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())