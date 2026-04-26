import requests
import os
from datetime import datetime

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRcHQh5q4mx9jG0FcE1JF1wQo3_luOpO1wWgE_R_iQztu3jziT7juyIWaFWpje2_QwbXnXThCl9Mv--/pub?output=csv"

os.makedirs("data", exist_ok=True)
response = requests.get(URL)
response.raise_for_status()

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"data/sheet_{timestamp}.csv"

with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)

with open("data/latest.csv", "w", encoding="utf-8") as f:
    f.write(response.text)

print(f"✅ تم حفظ {len(response.text)} حرف")
print(f"📁 الملف: {filename}")
