import math

class Quadratic:
    def __init__(self, a=1.0, b=0.0, c=0.0):
        # Constructor to initialize the coefficients of the quadratic equation
        self.name = "quadratic"
        self.a = a
        self.b = b
        self.c = c

    def setA(self, A):
        # Setter method for 'a'
        self.a = A

    def setB(self, B):
        # Setter method for 'b'
        self.b = B

    def setC(self, C):
        # Setter method for 'c'
        self.c = C

    def getB(self):
        # Getter method for 'b'
        return self.b

    def getC(self):
        # Getter method for 'c'
        return self.c

    def numOfRoots(self):
        # Method to calculate the number of distinct real roots
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if self.a == 0 and self.b != 0:
            return 1
        elif self.a == 0 and self.b == 0:
            return 0
        elif discriminant > 0:
            return 2
        elif discriminant == 0:
            return 1
        else:
            return 0

    def root1(self):
        # Method to calculate the first root
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if self.a == 0 and self.b != 0:
            return -self.c / self.b
        elif self.a == 0 and self.b == 0:
            raise ValueError("No real solution exists")
        elif discriminant >= 0:
            return (-self.b + math.sqrt(discriminant)) / (2 * self.a)
        else:
            raise ValueError("No real solution exists")

    def root2(self):
        # Method to calculate the second root
        discriminant = self.b ** 2 - 4 * self.a * self.c
        if self.a == 0 and self.b != 0:
            return -self.c / self.b
        elif self.a == 0 and self.b == 0:
            raise ValueError("No real solution exists")
        elif discriminant >= 0:
            return (-self.b - math.sqrt(discriminant)) / (2 * self.a)
        else:
            raise ValueError("No real solution exists")

class Linear(Quadratic):
    def __init__(self, b=0.0, c=0.0):
        # Constructor for the Linear class, where 'a' is always 0
        super().__init__(0.0, b, c)
        self.name = "linear"


def testEquation():
    equations = [
        (1, 4, 1),  # x^2 + 4x + 1
        (1, 4, 4),  # x^2 + 4x + 4
        (1, 1, 1),  # x^2 + x + 1
        (0, 1, 1),  # x
        (0, 0, 1),  # 1 (constant, should be handled)
        (0, 1, 1)   # x + 1 (linear equation)
    ]

    for eq in equations:
        if eq[0] == 0:
            equation = Linear(eq[1], eq[2])
        else:
            equation = Quadratic(eq[0], eq[1], eq[2])

        try:
            roots = equation.numOfRoots()
            if roots == 0:
                print(f"The equation {equation.name} has no real solution.")
            elif roots == 1:
                root1 = equation.root1()
                print(f"The equation {equation.name} has one real solution: {root1}")
            else:
                root1 = equation.root1()
                root2 = equation.root2()
                print(f"The equation {equation.name} has two real solutions: {root1} and {root2}")
        except ValueError as ve:
            print(f"The equation {equation.name} raised an error: {ve}")

# Run the test function
testEquation()



