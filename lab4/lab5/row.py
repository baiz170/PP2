import re

with open("row.txt", "r", encoding="utf-8") as file:
    data = file.read()

product_pattern = re.compile(r'(\d+)\.\n(.*?)\n(\d+,\d+)\s+x\s+([\d\s]+,\d+)\n([\d\s]+,\d+)')
products = product_pattern.findall(data)

print("Список товаров:")
for product in products:
    item_number = product[0]
    item_name = product[1].strip()
    quantity = product[2]
    price_per_unit = product[3].replace(" ", "")
    total_price = product[4].replace(" ", "")

    print(f"{item_number}. {item_name}: {quantity} шт. x {price_per_unit} = {total_price}")

total_pattern = re.search(r"ИТОГО:\n([\d\s]+,\d+)", data)
if total_pattern:
    total_amount = total_pattern.group(1).replace(" ", "")
    print("\nИтоговая сумма:", total_amount)
else:
    print("\nИтоговая сумма не найдена.")
