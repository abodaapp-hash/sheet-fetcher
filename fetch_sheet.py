import requests
import os
from datetime import datetime

# رابط Google Sheets
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRcHQh5q4mx9jG0FcE1JF1wQo3_luOpO1wWgE_R_iQztu3jziT7juyIWaFWpje2_QwbXnXThCl9Mv--/pub?output=csv"

# إنشاء مجلد data
os.makedirs("data", exist_ok=True)
print("✅ تم إنشاء مجلد data")

# تحميل البيانات
response = requests.get(URL)
print(f"📥 تم التحميل: {len(response.text)} حرف")

# حفظ كـ latest.csv
with open("data/latest.csv", "w", encoding="utf-8") as f:
    f.write(response.text)
print("✅ تم حفظ data/latest.csv")

# حفظ نسخة بتاريخ
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"data/sheet_{timestamp}.csv"
with open(filename, "w", encoding="utf-8") as f:
    f.write(response.text)
print(f"✅ تم حفظ {filename}")

print("🎉 اكتمل بنجاح!")
