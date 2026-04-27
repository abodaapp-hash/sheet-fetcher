import requests
import os
import time

URL = "https://docs.google.com/spreadsheets/d/e/2PACX-1vT7VyU_we2Rc3vYaE3ZzodM5wsub_OdlLQ5CYZPvfzlIfpXi19x58aYAavXxs0UvFuIUSnYQ0foIv41/pub?output=csv"
os.makedirs("data", exist_ok=True)

# كسر الكاش
url_with_time = URL + "&t=" + str(int(time.time()))

response = requests.get(url_with_time)
response.encoding = 'utf-8-sig'

# حفظ الملف الأساسي فقط
with open("data/latest.csv", "w", encoding="utf-8-sig") as f:
    f.write(response.text)
    # إضافة سطر في النهاية للتأكد من وجود تغيير لعمل الـ Commit
    f.write(f"\n# Last Update: {time.ctime()}")

print("✅ Updated latest.csv")
