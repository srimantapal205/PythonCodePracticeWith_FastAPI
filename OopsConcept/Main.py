from Enemy import *
enemy = Enemy()
print(enemy.health_points)

enemy_1 = Enemy()
print(enemy_1.health_points)

enemy_2 = Enemy()
enemy_2.health_points = 200
print(enemy_2.health_points)

enemy.type_of_enemy = 'Orc'

print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage} '
      )

enemy.type_of_enemy = 'Goblin'

print(enemy.talk())
print(enemy.walk_forward())
print(enemy.attack())



