from typing import Any


class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            + f"Health: {self.health}, Hidden: {self.hidden}}}"
        )

    @classmethod
    def __str__(cls) -> str:
        return "[" + ", ".join(repr(instance) for instance in cls.alive) + "]"


class Herbivore(Animal):

    def hide(self) -> None:
        if self.hidden:
            self.hidden = False
        else:
            self.hidden = True


class Carnivore(Animal):

    def bite(self, animal: Any) -> None:
        print(f"{self.name} bite {animal.name}")
        print(len(Animal.alive))
        if animal in Animal.alive and isinstance(animal, Herbivore):
            if not animal.hidden:
                animal.health -= 50
                print(f"{animal.name} health = {animal.health}")
            else:
                print(
                    f"{self.name} cannot bite {animal.name} because she hide"
                )
            if animal.health <= 0:
                Animal.alive.remove(animal)
        else:
            print(f"{self.name} cannot bite because she dead")
        print(len(Animal.alive))
