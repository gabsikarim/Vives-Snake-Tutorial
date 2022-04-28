import random
from typing import List

class Branch:
    def __init__(self, leafs: int = 5, length: float = 0.3):
        self.leafs: int = leafs
        self.length: float = length # in meters

class Tree:
    def __init__(self, name: str):
        # initialisatiefunctie
        self.name: str = name
        self.branches: List[Branch] = []
        self.length = 1.5 # 1.5 meters groot.

        self.__generate_branches()

    def __generate_branches(self):
        for i in range(random.randint(1, 50)):
            leafs = random.randint(0, 10)
            length = random.uniform(0.1, 1.5)
            self.branches.append(Branch(leafs=leafs, length=length))

    def grow(self, n: float = 0.1):
        self.length += n

    def __str__(self):
        return f"{self.name} is {self.length} meters high with {len(self.branches)} branches."

def MyFirstFunction():
    print("Welkom op de management days!")

def main():
    MyFirstFunction() # uitvoering van een methode/functie

    myTree: Tree = Tree("Oak Tree") # aanmaken van een boom
    print(myTree)
    myTree.grow(0.5)
    print(myTree)
    myTree.grow()
    print(myTree)

if __name__ == '__main__':
    # Start locatie voor executie van [dit] bestand.
    main() # Uitvoeren van de main - methode