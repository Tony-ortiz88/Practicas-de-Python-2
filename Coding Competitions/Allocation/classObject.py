class computer:
    wheels = 4

    def __init__(self, ram, cpu):
        self.cpu = cpu
        self.ram = ram
    def update(self):
        self.cpu = 44

    def config(self):
        print(1212332)

    @classmethod
    def info(cls):
        return cls.wheels
cm = computer(15, 30)
cm1 = computer(13, 33)
cm.config()
cm1.update()
print(cm1.cpu)
print(cm1.wheels)