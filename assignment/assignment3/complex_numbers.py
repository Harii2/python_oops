import math
class ComplexNumber:
    def __init__(self, real_number=0, imaginary_number=0, sign="+"):
        if isinstance(real_number, str) and isinstance(imaginary_number, str):
            raise ValueError("Invalid value for both real and imaginary part")
        if isinstance(real_number, str):
            raise ValueError("Invalid value for real part")
        if isinstance(imaginary_number, str):
            raise ValueError("Invalid value for imaginary part")

        self._real_number = real_number
        self._imaginary_number = imaginary_number
        self._sign = sign

    def get_real_part(self):
        return self._real_number

    def set_real_part(self, real_number):
        self._real_number = real_number

    def get_imaginary_part(self):
        return self._imaginary_number

    def set_imaginary_part(self, imaginary_number):
        self._imaginary_number = imaginary_number

    def get_sign(self):
        return self._sign

    def set_sign(self, sign):
        self._sign = sign

    def conjugate(self):
        sign = ""
        if self.get_sign() == "+":
            sign = "-"
        else:
            sign = "+"
        conjugate_number = "{}{}{}i".format(self.get_real_part(), sign, self.get_imaginary_part())
        return conjugate_number

    def get_imaginary_part_with_sign(self):
        if self.get_sign() == "-":
            return -1 * self.get_imaginary_part()
        return self.get_imaginary_part()

    def __add__(self, other):
        real_part_sum = self.get_real_part() + other.get_real_part()
        imaginary_part_sum = self.get_imaginary_part_with_sign() + other.get_imaginary_part_with_sign()
        if imaginary_part_sum < 0:
            return ComplexNumber(real_part_sum, abs(imaginary_part_sum), "-")
        return ComplexNumber(real_part_sum, imaginary_part_sum)

    def __sub__(self, other):
        real_part_sub = self.get_real_part() - other.get_real_part()
        imaginary_part_sub = self.get_imaginary_part_with_sign()- other.get_imaginary_part_with_sign()
        if imaginary_part_sub < 0:
            return ComplexNumber(real_part_sub, abs(imaginary_part_sub), "-")
        return ComplexNumber(real_part_sub, imaginary_part_sub)

    def __mul__(self, other):
        real_part_mul = self.get_real_part() * other.get_real_part()
        imaginary_part_mul = self.get_imaginary_part_with_sign() * other.get_imaginary_part_with_sign()
        if imaginary_part_mul < 0:
            return ComplexNumber(real_part_mul, abs(imaginary_part_mul), "-")
        return ComplexNumber(real_part_mul, imaginary_part_mul)

    def __truediv__(self, other):
        real_part_div = round(self.get_real_part() / other.get_real_part(), 2)
        imaginary_part_div = round(self.get_imaginary_part_with_sign() / other.get_imaginary_part_with_sign(), 2)
        if imaginary_part_div < 0 :
            return ComplexNumber(real_part_div, abs(imaginary_part_div), '-')
        return ComplexNumber(real_part_div, imaginary_part_div)

    def __abs__(self):
        return math.sqrt(self.get_real_part() ** 2 + self.get_imaginary_part_with_sign() ** 2)

    def __eq__(self, other):
        return self.get_real_part() == other.get_real_part() and self.get_imaginary_part_with_sign() == other.get_imaginary_part_with_sign()

    def __str__(self):
        return "{}{}{}i".format(self.get_real_part(), self.get_sign(), self.get_imaginary_part())


one_plus_two_i = ComplexNumber(1, 2, "-")
three_plus_four_i = ComplexNumber(3, 4, "-")
four_plus_six_i = one_plus_two_i + three_plus_four_i
# print(four_plus_six_i)

one_plus_two_i = ComplexNumber(1,2)
absolute_value = abs(one_plus_two_i)
print(absolute_value)
print(ComplexNumber(1,2) == ComplexNumber(2,2))