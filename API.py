# importing libraries for working with API
import requests

url = "https://restcountries.com/v3.1/independent?status=true"

# Barcha mamlakatlarni olish
countries = requests.get(url)
if countries.status_code == 200:
    print(f"Jami mamlakatlar: {len(countries.json())}")

# Nom bo'yicha qidirish
uzbekistan = requests.get('https://restcountries.com/v3.1/name/uzbekistan').json()[0]
print(f"\nMamlakat: {uzbekistan['name']['common']}")
print(f"Poytaxt: {uzbekistan['capital'][0]}")
print(f"Aholisi: {uzbekistan['population']:,}")
print(f"Mintaqa: {uzbekistan['region']}")
print(f"Til: {list(uzbekistan['languages'].values())[-1]}")

# Region bo'yicha mamlakatlar
asia_countries = requests.get('https://restcountries.com/v3.1/region/asia').json()
print(f"\nOsiyo mamlakatlar soni: {len(asia_countries)}")

# Valyuta bo'yicha qidirish
usd_countries = requests.get('https://restcountries.com/v3.1/currency/usd').json()
print(f"USD ishlatuvchi mamlakatlar: {len(usd_countries)}")