class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.value = "I am the only instance!"
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)     
print(obj1.value)          