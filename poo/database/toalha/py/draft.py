class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0


    def __str__(self) -> str:
        return f"Cor: {self.color}, tamanho:{self.size}, umidade: {self.wetness}"  

    def dry(self, amount: int) -> None:
        self.wetness += amount  
        if self.wetnesss > self.getMaxWetness():
            print("Toalha encharcada")
            self.wetness = 0


    def getMaxWetness(self) -> int:
        if self.size == "p":
            return 10
        if self.size == "m":
            return 20
        if self.size == "g":
            return 30
        return 0
    
    def __str__(self) -> str:
        return f"Cor:{self.color}, Tam:{self.size}, Umidade:{self.wetness}"


    def main():
Toalha = Towel ("", "")
        while True:
            print("$", end="")
            line: str = input()
            args: list[str] = line.split(" ")


            if args[0] == "end":
                break
            elif args[0] =="new": # color size
                color = args[1]
                size = args[2]
                toalha = Towel(color, size)
            elif args[0] == "show":
                print(toalha)
            elif args[0] == "dry":  # amount
            amount = int(args[1])
            toalha.dry(amount)

            else:
                print("fail: comando desconhecido")

        main()
             
            

azul = Towel ("blue", "G")
amarelo = Towel("yellow", "P")
vermelho = Towel("red", "M")

print(amarelo.size)
print(amarelo.color)

print(azul.size)
print(azul.color)

print(azul) 
azul.dry(5)
azul.dry(10)
print(azul)




