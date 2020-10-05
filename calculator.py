class Calculator:
    def __add(self, num1, num2):
        return num1 + num2

    def __subtract(self, num1, num2):
        return num1 - num2

    def __multiply(self, num1, num2):
        return num1 * num2

    def __divide(self, num1, num2):
        return num1 / num2

    def __remainder(self, num1, num2):
        return num1 % num2

    def __compute(self, operation, num1, num2):
        return operation(num1, num2)

    def use_calc(self):
        switch = {
            "add": self.__add,
            "sub": self.__subtract,
            "mul": self.__multiply,
            "div": self.__divide,
            "rem": self.__remainder,
        }
        operation = switch.get(
            input(
                (
                    "add(add), subtract(sub), multiply(mul), "
                    "divide(div) or remainder(rem)?"
                ),
            ), "not valid input"
        )
        num1 = int(input("First number: "))
        num2 = int(input("second number: "))
        print(self.__compute(operation, num1, num2))


calc = Calculator()
calc.use_calc()
