class Deer:
    sound = "Buck Buck"
    breath = "Breath in Air"

    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs

    def make_sound(self):
        return type(self).sound

    def breathe(self):
        return type(self).breath

    def grow(self):
        self.age_in_months += 1
        self.required_food_in_kgs += 2


class Lion:
    sound = "Roar Roar"
    breath = "Breath in Air"

    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs

    def make_sound(self):
        return type(self).sound

    def breathe(self):
        return type(self).breath

    def grow(self):
        self.age_in_months += 1
        self.required_food_in_kgs += 4


class Shark:
    sound = "Shark Sound"
    breath = "Breath in Water"

    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs

    def make_sound(self):
        return type(self).sound

    def breathe(self):
        return type(self).breath

    def grow(self):
        self.age_in_months += 1
        self.required_food_in_kgs += 8


class GoldFish:
    sound = "Hum Hum"
    breath = "Breath in Water"

    def __init__(self, age_in_months, breed, required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs

    def make_sound(self):
        return type(self).sound

    def breathe(self):
        return type(self).breath

    def grow(self):
        self.age_in_months += 1
        self.required_food_in_kgs += 2


class Zoo:
    total_animals_in_all_zoos = 0

    def __init__(self):
        self.reserved_food_in_kgs = 0
        self.total_animals = []

    def add_food_to_reserve(self, food):
        self.reserved_food_in_kgs = food

    def count_animals(self):
        return len(self.total_animals)

    def add_animal(self, animal):
        self.total_animals.append(animal)
        Zoo.total_animals_in_all_zoos += 1

    def feed(self, animal):
        self.reserved_food_in_kgs -= animal.required_food_in_kgs

    @classmethod
    def count_animals_in_all_zoos(cls):
        return cls.total_animals_in_all_zoos

    @classmethod
    def count_animals_in_given_zoo(cls,zoo):
        return zoo.count_animals()


gold_fish = GoldFish(1, "Nemo", 0.5)

zoo = Zoo()
zoo.add_food_to_reserve(10000000)
zoo.add_animal(gold_fish)
print(zoo.reserved_food_in_kgs)
zoo.feed(gold_fish)
print(zoo.count_animals())
print(zoo.reserved_food_in_kgs)
print(Zoo.count_animals_in_given_zoos(zoo))
