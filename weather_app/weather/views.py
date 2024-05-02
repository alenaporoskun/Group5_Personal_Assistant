from django.shortcuts import render
import requests
from utils import get_weather, get_city_from_user

def weather(request):
    city = request.GET.get('city', 'Kyiv')  # Отримуємо назву міста з GET-параметра 'city', якщо не вказано, використовуємо 'Kyiv' за замовчуванням
    weather_data = get_weather(city)  # Отримуємо погодні дані для вказаного міста
    context = {'weather': weather_data}  # Створюємо контекст для передачі у шаблон
    return render(request, 'weather_app/weather.html', context)