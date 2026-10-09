
class AttributeTable:
    def __init__(self, layer_name: str, field_names: list):
        self.layer_name = layer_name
        self.field_names = field_names
        self.records = []

    def add_record(self, record: dict) -> None:
        for key in record:
            if key not in self.field_names:
                print(f"Ключа {key} не существует в описании слоя")
                return
        self.records.append(record)

    def find_by_field(self, field: str, value) -> list:
        return [record for record in self.records if record.get(field) == value]

    def filter_by_condition(self, field: str, min_value: int | float) -> list:
        return [record for record in self.records 
                if isinstance(record.get(field),(int, float)) and record.get(field) >= min_value]

    def count_records(self) -> int:
        return len(self.records)

    def unique_values(self, field: str) -> list:
        return list(set(record.get(field) for record in self.records))

    def sum_field(self, field: str) -> int | float:
        return sum([record.get(field) for record in self.records 
                    if isinstance(record.get(field), (int, float))])

    def print_all(self):
        print(f"Слой: {self.layer_name}\n"
              "Поля:", *self.field_names,
              "\n--------------------------")
        for record in self.records:
            print(*[record.get(field) for field in self.field_names])
