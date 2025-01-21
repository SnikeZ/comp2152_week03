import random
BREAK_ROUND = 11

# Setup
diceOptions = list(range(1, 7))
weapons = ['Fist', 'Knife', 'Club', 'Gun', 'Bomb', 'Nuclear Bomb']
print("Available weapons: ")
for i in weapons:
    print(i)

combat_strength = 0
m_combat_strength = 0

while True:
    print("Enter your combat strength (1-6): ", end="")
    try:
        combat_strength = int(input())
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if combat_strength < 1 or combat_strength > 6:
        print("Invalid combat strength. Please enter a number between 1 and 6.")
        continue

    break


while True:
    print("Enter the monster's combat strength (1-6): ", end="")
    try:
        m_combat_strength = int(input())
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if m_combat_strength < 1 or m_combat_strength > 6:
        print("Invalid combat strength. Please enter a number between 1 and 6.")
        continue

    break

# Battle
for j in range(1, 21, 2):
    if j == BREAK_ROUND :
        print(f"Battle Truce declared in Round {BREAK_ROUND}. Game Over!")
        break

    hero_roll = random.randint(0, 5)
    monster_roll = random.randint(0, 5)

    hero_total_strength, monster_total_strength = combat_strength + hero_roll, m_combat_strength + monster_roll
    
    print(f"Round {j + 1}: Hero rolled {hero_roll + 1}, Monster rolled {monster_roll + 1}.")
    print(f"Hero selected {weapons[hero_roll]}, Monster selected {weapons[monster_roll]}.")
    print(f"Hero total strength: {hero_total_strength}, Monster total strength: {monster_total_strength}.")

    if hero_total_strength > monster_total_strength:
        print("Hero wins!")
    elif hero_total_strength < monster_total_strength:
        print("Monster wins!")
    else:
        print("Draw!")
    print()