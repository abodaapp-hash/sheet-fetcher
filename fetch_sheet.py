import requests
import os
from datetime import datetime
import time

# رابط Google Sheets (CSV)
URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRcHQh5q4mx9jG0FcE1JF1wQo3_luOpO1wWgE_R_iQztu3jziT7juyIWaFWpje2_QwbXnXThCl9Mv--/pub?output=csv"

# إنشاء مجلد data
os.makedirs("data", exist_ok=True)

# كسر الكاش بإضافة وقت
url_with_time = URL + "&t=" + str(int(time.time()))

# تحميل البيانات
response = requests.get(url_with_time)
response.encoding = 'utf-8-sig'

# إضافة توقيت داخل الملف (يضمن التحديث)
content = response.text + f"\n# updated: {datetime.now()}"

# حفظ latest.csv
with open("data/latest.csv", "w", encoding="utf-8-sig") as f:
    f.write(content)

# حفظ نسخة بتاريخ
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"data/sheet_{timestamp}.csv"

with open(filename, "w", encoding="utf-8-sig") as f:
    f.write(content)

print("✅ تم التحديث بنجاح")