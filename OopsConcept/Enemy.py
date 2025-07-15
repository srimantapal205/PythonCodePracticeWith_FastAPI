class Enemy :
    #Encapsulation
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 2

    # Abstraction
    def talk(self) :
        print(f'{self.type_of_enemy}. Be prepared to fight!')

    def walk_forward(self):
        print(f'{self.type_of_enemy} moves closer to you!')

    def attack(self):
        print(f'{self.type_of_enemy} attacks you for {self.attack_damage} damage!')

    # Inheritance


    # Polymorphism


    