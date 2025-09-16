class Towel:
    def __init__(self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0


    def __str__(self) -> str:
        return f"Cor: {self.color}, tamanho:{self.size}, umidade: {self.wetness}"  

    def dry(self, amount: int) -> None:
        self.wetness += amount  

azul = Towel ("blue", "G")
amarelo = Towel("yellow", "p")

print(amarelo.size)
print(amarelo.color)

print(azul.size)
print(azul.color)

print(azul) 
azul.dry(5)
azul.dry(10)
print(azul)




