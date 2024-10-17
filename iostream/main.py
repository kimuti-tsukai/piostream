class Ref:
    def __init__(self, value: list):
        assert value.__len__() == 1, "Length of value list must be 1"
        self.__value = value

    def get(self):
        return self.__value[0]

    def set(self, value):
        self.__value[0] = value
        return self.get()

    def __call__(self, value=None):
        if value == None:
            return self.get()
        else:
            return self.set(value)

    def __str__(self):
        return self().__str__()

class Cin:
    def __init__(self):
        self.iter = Cin.values()

    def values():
        while True:
            yield from input().strip().split()

    def __rshift__(self, rhs: Ref):
        rhs(type(rhs())(self.iter.__next__()))
        return self

if __name__ == "__main__":
    cin = Cin()

    a = Ref([0])
    b = Ref([""])
    cin >> a >> b

    print(a, b)
