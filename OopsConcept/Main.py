from Enemy import *
from Zombie import *
enemy = Enemy('Goblin', 100, 10)
# print(enemy.health_points)
#
# enemy_1 = Enemy()
# print(enemy_1.health_points)
#
# enemy_2 = Enemy()
# enemy_2.health_points = 200
# print(enemy_2.health_points)
#
# enemy.type_of_enemy = 'Orc'
#
# print(f'{enemy.type_of_enemy} has {enemy.health_points} health points and can do an attack of {enemy.attack_damage} '
#       )
#
# enemy.type_of_enemy = 'Goblin'
#
# print(enemy.talk())
# print(enemy.walk_forward())
# print(enemy.attack())


print(enemy.health_points)
print(enemy.talk())
print(enemy.attack())
print(enemy.get_type_of_enemy())

zombie = Enemy('Zombie', 80, 5)
print(zombie.get_type_of_enemy(), zombie.health_points, zombie.attack_damage)

zombie = Zombie(10, 1)
print(zombie.get_type_of_enemy(), zombie.health_points, zombie.attack_damage)
zombie.zombie_talk = zombie.talk()
print(zombie.talk())



