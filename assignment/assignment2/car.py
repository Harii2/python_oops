class Car:
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")
        self._color = color
        self._max_speed = max_speed
        self._acceleration = acceleration
        self._tyre_friction = tyre_friction
        self._is_started = False
        self._current_speed = 0
        self._sound = "Beep Beep"

    def get_color(self):
        return self._color

    def set_color(self, x):
        self._color = x

    def get_max_speed(self):
        return self._max_speed

    def set_max_speed(self, max_speed):
        self._max_speed = max_speed

    def get_acceleration(self):
        return self._acceleration

    def set_acceleration(self, acceleration):
        self._acceleration = acceleration

    def get_tyre_friction(self):
        return self._tyre_friction

    def set_tyre_friction(self, friction):
        self._tyre_friction = friction

    def get_is_started(self):
        return self._is_started

    def set_is_started(self, is_started):
        self._is_started = is_started

    def get_current_speed(self):
        return self._current_speed

    def set_current_speed(self, speed):
        self._current_speed = speed

    def start_engine(self):
        self.set_is_started(True)

    def get_sound(self):
        return self._sound

    def is_engine_started(self):
        return self.get_is_started()

    #
    def accelerate(self):
        if not self.get_is_started():
            self.set_is_started(True)
        if self.get_current_speed() < self.get_max_speed():
            self.set_current_speed(self.get_current_speed() + self.get_acceleration())

    def apply_brakes(self):
        if self.get_current_speed() > self.get_tyre_friction():
            self.set_current_speed(self.get_current_speed() - self.get_tyre_friction())
        else:
            self.set_current_speed(0)

    def stop_engine(self):
        self.set_is_started(False)

    def sound_horn(self):
        return self._sound


class Truck(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._max_cargo_weight = max_cargo_weight
        self._sound = "Honk Honk"
        self._current_load = 0

    def get_max_cargo_weight(self):
        return self._max_cargo_weight

    def set_max_cargo_weight(self, max_weight):
        self._max_cargo_weight = max_weight

    def get_current_load(self):
        return self._current_load

    def set_current_load(self, load):
        self._current_load = load

    def load(self, cargo_weight):
        if self.get_is_started():
            raise Exception("Cannot load during a motion")
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")

        if cargo_weight + self.get_current_load() > self.get_max_cargo_weight():
            raise Exception("Cannot load cargo more than max limit : {}".format(cargo_weight))
        self.set_current_load(self.get_current_load() + cargo_weight)

    def unload(self, cargo_weight):
        if self.get_is_started():
            raise Exception("Cannot load during a motion")
        if cargo_weight < 0:
            raise ValueError("Invalid value for cargo_weight")
        self.set_current_load(self.get_current_load() - cargo_weight)


class RaceCar(Car):
    def __init__(self, color, max_speed, acceleration, tyre_friction):
        super().__init__(color, max_speed, acceleration, tyre_friction)
        self._sound = "Peep Peep\nBeep Beep"
        self._nitro_points = 0

    def get_nitro_points(self):
        return self._nitro_points

    def set_nitro_points(self, points):
        self._nitro_points = points

    def apply_brakes(self):
        if (self.get_max_speed() / 2) < self.get_current_speed():
            self.set_nitro_points(self.get_nitro_points() + 10)
        super().apply_brakes()

    def accelerate(self):
        super().accelerate()
        if self.get_nitro_points() > 0:
            added_acceleration = round(self.get_acceleration() * 0.3)
            if self.get_current_speed() + added_acceleration >= self.get_max_speed():
                self.set_current_speed(self.get_max_speed())
            else:
                self.set_current_speed(self.get_current_speed() + added_acceleration)

            self.set_nitro_points(self.get_nitro_points() - 10)


racecar = RaceCar("Red", 250, 50, 30)
racecar.start_engine()
racecar.accelerate()
racecar.accelerate()
racecar.accelerate()
print(racecar.get_current_speed())
racecar.apply_brakes()
print(racecar.get_current_speed())
print(racecar.get_nitro_points())
racecar.accelerate()
print(racecar.get_current_speed())
print(racecar.get_nitro_points())
