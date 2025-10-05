class Calculadora:
    def __init__(self, batteryMax: int):
        self.display: float = 0.0
        self.battery: int = 0
        self.batteryMax: int = batteryMax

    def __str__(self):
        return f"display = {self.display:.2f}, battery = {self.battery}"
     
    def show(self):
        print(self.__str__())

    def charge(self, increment):
        if increment < 0:   
            return
        self.battery += increment
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a: float, b: float):
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return       
        self.display = a + b
        self.battery -= 1  

    def div(self, a: float, b: float):
        if self.battery == 0:
            print("fail: bateria insuficiente")
            return     
        if b == 0:
            print("fail: divisao por zero")
            self.battery -= 1
            return
        self.display = a / b
        self.battery -= 1


def main():
    calc = None
    while True:
        line = input()
        print(f"${line}")
        args = line.split()
        if args[0] == "end":
            break
        elif args[0] == "init":
            batteryMax = int(args[1])
            calc = Calculadora(batteryMax)
        elif args[0] == "show":
            calc.show()
        elif args[0] == "charge":
            inc = int(args[1])
            calc.charge(inc)
        elif args[0] == "sum":
            a = float(args[1])
            b = float(args[2])
            calc.sum(a, b)
        elif args[0] == "div":
            a = float(args[1])
            b = float(args[2])  
            calc.div(a, b)   
        else:
            print("fail: comando invalido")


if __name__== "__main__":
    main()
