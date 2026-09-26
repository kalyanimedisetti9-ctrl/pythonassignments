class Temperature:
    def __init__(self, degree):
        self.degree = degree

    def __gt__(self, other):
        return self.degree > other.degree


t1 = Temperature(35)
t2 = Temperature(30)

print(t1 > t2)