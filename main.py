class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.status = False

class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"{item_name} успешно добавлен в ассортимент магазина {self.name}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"{item_name} успешно удален из ассортимента магазина {self.name}")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена на товар {item_name} обновлена. Новая цена: {new_price}")

# Создаем несколько магазинов
store1 = Store("Магазин 1", "Улица Пушкина, дом Колотушкина")
store2 = Store("Магазин 2", "Проспект Лермонтова, дом Тургенева")
store3 = Store("Магазин 3", "Площадь Гоголя, дом Достоевского")

# Добавляем товары в ассортимент магазина 1
store1.add_item("Яблоки", 0.5)
store1.add_item("Бананы", 0.75)

# Обновляем цену на товар в магазине 1
store1.update_price("Яблоки", 0.6)

# Удаляем товар из ассортимента магазина 1
store1.remove_item("Бананы")

# Тестируем методы для получения цены
print(store1.get_price("Яблоки"))
print(store1.get_price("Бананы"))  # Выведет None, так как товар удален
