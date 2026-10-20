def canFight(combat_level, monster_level):
    """Tests if the `combat_level` is higher than the `monster_level`.

    Args:
        combat_level (int): Player's combat level.
        monster_level (int): Monster's combat level.

    Returns:
        True: The player has a high enough level (level greater than the monster) to fight the monster.
        False: The player has insufficient level to fight the monster.
    """
    if combat_level >= monster_level:
        print("you can fight the monster\n")
        return True
    else:
        print("you aren’t high enough level\n")
        return False
        # exit(0)


def getHealths():
    """Gets the monster and player's healths from `healths.txt`.

    Returns:
        mh: The read monster's health.
        ph: The read player's health.

    Raises:
        FileNotFoundError: If `healths.txt` is not in the same directory as `part5_documented.py`.
        ValueError: If any values other than 2 integers are at the beginning of `healths.py`.
    """
    with open('healths.txt', 'r') as file:
        mh = int(file.readline().strip())
        ph = int(file.readline().strip())

    return mh, ph


def fight(monster_health, player_health):
    """Allows the player to choose between kicking (causing 3 damage) and punching (causing 1 damage) \
        the monster until either the player or monster dies. \
        If the player attacks the monster attacks with a fireball causing 2 damage.

    Args:
        monster_health (int): Monster's health.
        player_health (int): Player's health.

    Returns:
        monster_health (int): Updated monster's health after the fight.
        player_health (int): Updated player's health after the fight.
    """
    while monster_health > 0 and player_health > 0:
        move = input("(K/k)ick -or- (P/p)unch? ")
        if move == "k" or move == "K":
            print("\nyou kick the monster")
            monster_health = monster_health - 3
        elif move == "p" or move == "P":
            print("\nyou punch the monster")
            monster_health = monster_health - 1
        else:
            print("\ninvalid move\n")
            continue

        print("the monster shoots a fireball at you")
        player_health = player_health - 2

        print(f"\nPlayer health: {player_health}")
        print(f"Monster health: {monster_health}\n")

    return monster_health, player_health


def determineWinner(monster_health, player_health):
    """Prints if the monster or player died, based on their healths being zero or less.

    Args:
        monster_health (int): Monster's health.
        player_health (int): Player's health.
    """
    if monster_health <= 0:
        print("you killed the monster")
    if player_health <= 0:
        print("the monster killed you")


def writeHealths(monster_health, player_health):
    """ Writes the monster and player's healths to `healths.txt`.

    Args:
        monster_health (int): Monster's health.
        player_health (int): Player's health.

    Raises:
        FileNotFoundError: If `healths.txt` is not in the same directory as `part5_documented.py`.
    """
    with open("healths.txt", "w", encoding="utf-8") as file:
        file.write(f"{monster_health}\n")
        file.write(f"{player_health}")


def system():
    """ Allows the player to fight the monster if their combat level is higher then the monster's (50).
    """
    name = input("Character's name: ")
    combat_level = int(input("Combat level: "))

    print(f"\nWelcome, {name}!")
    print(f"Combat level: {combat_level}\n")

    monster_level = 50

    if not canFight(combat_level, monster_level):
        exit(0)

    monster_health, player_health = getHealths()

    monster_health, player_health = fight(monster_health, player_health)

    determineWinner(monster_health, player_health)

    writeHealths(monster_health, player_health)


if __name__ == "__main__":
    system()
