import re
import json

with open("raw.txt", "r") as f:
    text = f.read()

lines = text.split("\n")

#1

price_pattern = r"\d[\d ]*,\d{2}"
all_prices_raw = re.findall(price_pattern, text)

prices = []
for p in all_prices_raw:
    clean_price = p.replace(" ", "").replace(",", ".")
    prices.append(float(clean_price))

#2

product_names = []

for i in range(len(lines)):
    if re.match(r"\d+\.", lines[i].strip()):
        if i + 1 < len(lines):
            name = lines[i + 1].strip()
            product_names.append(name)


#3

total_amount = None

for i in range(len(lines)):
    if "ИТОГО" in lines[i]:
        if i + 1 < len(lines):
            total_line = lines[i + 1]
            match = re.search(price_pattern, total_line)
            if match:
                total_amount = float(match.group().replace(" ", "").replace(",", "."))

#4

datetime_match = re.search(r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}", text)

date = None
time = None

if datetime_match:
    dt = datetime_match.group()
    date, time = dt.split()

#5

payment_method = None

if "Банковская карта" in text:
    payment_method = "Банковская карта"
elif "Наличные" in text:
    payment_method = "Наличные"


result = {
    "products": product_names,
    "all_prices_found": prices,
    "total_amount": total_amount,
    "date": date,
    "time": time,
    "payment_method": payment_method
}

print(json.dumps(result, ensure_ascii=False, indent=4))