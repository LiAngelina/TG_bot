import aiohttp
from api import API_KEY, WEATHER_URL

CITIES = {
    "Казахстан": ["Алматы", "Астана"],
    "Россия": ["Москва"]
}

async def get_weather(city: str = "Алматы"):
    """Получает погоду для указанного города."""
    params = {
        "q": city,  # Теперь город передается корректно
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(WEATHER_URL, params=params) as response:
            data = await response.json()
            if response.status == 200:
                return (
                    f"🌍 Погода в {city}:\n"  # Теперь правильно отображается выбранный город
                    f"🌡 Температура: {data['main']['temp']}°C\n"
                    f"💨 Ветер: {data['wind']['speed']} м/с\n"
                    f"☁️ {data['weather'][0]['description'].capitalize()}"
                )
            else:
                return f"❌ Ошибка: Не удалось получить погоду для {city}."

def get_available_cities():
    """Возвращает список доступных городов по странам."""
    return CITIES