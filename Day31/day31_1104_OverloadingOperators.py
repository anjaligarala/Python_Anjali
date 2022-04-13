class vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f"Vector{self.a, self.b}"

    def __add__(self, other):
        return f"Vector{self.a + other.a, self.b + other.b}"


v1 = vector(3, 2)
v2 = vector(2, -1)
print(v1 + v2)

# Output = Vector(5, 1)
