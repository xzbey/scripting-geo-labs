from attribute_table import AttributeTable


table = AttributeTable("regions", ["id", "name", "area", "type"])

records = [
	{"id": 1, "name": "Москва", "area": 2561, "type": "город"},
	{"id": 2, "name": "Питер", "area": 1439, "type": "город"},
	{"id": 3, "name": "Ленобласть", "area": 83908, "type": "область"},
	{"id": 4, "name": "Московская область", "area": 44329, "type": "область"},
	{"id": 5, "name": "Калининград", "area": 15125, "type": "область"},
]

for record in records:
	table.add_record(record)

print("Вся таблица:")
table.print_all()

print("\nЗаписи с типом 'город':")
print(*table.find_by_field("type", "город"), sep='\n')

print("\nЗаписи с площадью не менее 5000:")
print(*table.filter_by_condition("area", 5000), sep="\n")

print("\nУникальные типы:")
print(table.unique_values("type"))

print(f"\nСуммарная площадь: {table.sum_field('area')}")

print("\nПопытка добавить запись с лишним полем:")
records_before = table.count_records()
table.add_record({
	"id": 6,
	"name": "Тестовый регион",
	"area": 1000,
	"type": "область",
	"population": 100000,
})
print(f"Количество записей до попытки: {records_before}")
print(f"Количество записей после попытки: {table.count_records()}")
