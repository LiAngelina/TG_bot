import aiohttp

API_KEY = "41dc09da6aae7e0f82a4665d15f8a901"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

async def get_weather():
    params = { 
        "q": "Алматы",  
        "appid": API_KEY,
        "units": "metric",
        "lang": "ru"
    }
    async with aiohttp.ClientSession() as session:
        async with session.get(WEATHER_URL, params=params) as response:
            data = await response.json()  
            if response.status == 200:  
                return (
                    f"Температура в Алматы: {data['main']['temp']}°C\n"
                    f"Ветер: {data['wind']['speed']} м/с\n"
                    f"Погода: {data['weather'][0]['description'].capitalize()}"
                )
            else:
                return "Ошибка. Не удалось получить погоду для Алматы."