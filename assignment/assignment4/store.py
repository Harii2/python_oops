class Item:
    def __init__(self, name, price, category):
        if price <= 0:
            raise ValueError("Invalid Price for price got {}".format(price))
        self._name = name
        self._price = price
        self._category = category

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_price(self):
        return self._price

    def set_price(self, price):
        self._price = price

    def get_category(self):
        return self._category

    def set_category(self, category):
        self._category = category

    def __str__(self):
        return "{}@{}-{}".format(self.get_name(), self.get_price(), self.get_category())


class Query:
    def __init__(self, field, operation, value):
        self._field = field
        self._operation = operation
        self._value = value

    def get_field(self):
        return self._field

    def set_field(self, field):
        self._field = field

    def get_operation(self):
        return self._operation

    def set_operation(self, operation):
        self._operation = operation

    def get_values(self):
        return self._value

    def set_values(self, value):
        self._value = value

    def get_field_name_with_in_item(self, item):
        if self.get_field() == "name":
            return item.get_name()
        elif self.get_field() == "price":
            return item.get_price()
        return item.get_category()

    def __str__(self):
        return "{} {} {}".format(self.get_field(), self.get_operation(), self.get_value())


class Store:
    def __init__(self):
        self.items_list = []

    def add_item(self, item):
        self.items_list.append(item)

    def filter(self, query):
        filtered_store = Store()
        if query.get_operation() == "IN":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) in query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "EQ":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) == query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "GT":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) > query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "GTE":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) >= query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "LT":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) < query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "LTE":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) <= query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "STARTS_WITH":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item).startswith(query.get_values()):
                    filtered_store.add_item(item)
        elif query.get_operation() == "ENDS_WITH":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item).endswith(query.get_values()):
                    filtered_store.add_item(item)
        elif query.get_operation() == "CONTAINS":
            for item in self.items_list:
                if query.get_values() in query.get_field_name_with_in_item(item):
                    filtered_store.add_item(item)
        elif query.get_operation() == "IN":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) in query.get_values():
                    filtered_store.add_item(item)
        if len(filtered_store.items_list) == 0:
            return "No Items"
        return filtered_store

    def exclude(self,query):
        filtered_store = Store()
        if query.get_operation() == "IN":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) not in query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "EQ":
            for item in self.items_list:
                if query.get_field_name_with_in_item(item) != query.get_values():
                    filtered_store.add_item(item)
        elif query.get_operation() == "GT":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item) > query.get_values()):
                    filtered_store.add_item(item)
        elif query.get_operation() == "GTE":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item) >= query.get_values()):
                    filtered_store.add_item(item)
        elif query.get_operation() == "LT":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item) < query.get_values()):
                    filtered_store.add_item(item)
        elif query.get_operation() == "LTE":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item) <= query.get_values()):
                    filtered_store.add_item(item)
        elif query.get_operation() == "STARTS_WITH":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item).startswith(query.get_values())):
                    filtered_store.add_item(item)
        elif query.get_operation() == "ENDS_WITH":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item).endswith(query.get_values())):
                    filtered_store.add_item(item)
        elif query.get_operation() == "CONTAINS":
            for item in self.items_list:
                if not (query.get_values() in query.get_field_name_with_in_item(item)):
                    filtered_store.add_item(item)
        elif query.get_operation() == "IN":
            for item in self.items_list:
                if not (query.get_field_name_with_in_item(item) in query.get_values()):
                    filtered_store.add_item(item)
        if len(filtered_store.items_list) == 0:
            return "No Items"
        return filtered_store

    def count(self):
        return len(self.items_list)

    def __str__(self):
        result = ""
        for item in self.items_list:
            result += str(item)
            result += "\n"
        return result


item = Item("Oreo Biscuits", 40, "Food")
# print(item)
item1 = Item("Boost Biscuits", 20, "Food")
item3 = Item("Butter", 10, "Grocery")
store = Store()
store.add_item(item)
store.add_item(item1)
store.add_item(item3)
# print(store)
query = Query(field="price", operation="GT", value=15)
results = store.exclude(query)
print( type(results))
print(results.count())
