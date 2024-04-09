class Calculator:
    def __init__(self, value):
        self.value = value

    def add(self, ather):
        self.value += ather
        return self

    def multiply(self, ather):
        self.value *= ather
        return self

    def divide(self, ather):
        self.value /= ather
        return self

    def get_result(self):
        return self.value


class Calculator2(Calculator):
    def __init__(self, value):
        super().__init__(value)

    def sqrt(self):
        self.value = self.value ** 0.5


if __name__ == "__main__":
    c = Calculator(5)
    c.add(3).multiply(2).divide(4)
    print(c.get_result())

    print("------------------------------")

    print(
        Calculator(5)
        .add(3)
        .multiply(2)
        .divide(4)
        .get_result()
    )

    print("--------------------------------")

    c2 = Calculator2(5)
    c2.add(3).multiply(2).divide(4).sqrt()
    print(c2.get_result())
