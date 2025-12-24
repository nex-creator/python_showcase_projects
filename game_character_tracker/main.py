from game_character import GameCharacter

def main():
    # Create a new character
    hero = GameCharacter("Kratos")

    # Print initial stats
    print("Initial Stats:")
    print(hero)

    # Update health and mana
    hero.health = 80
    hero.mana = 30
    print("\nAfter updating health and mana:")
    print(hero)

    # Level up
    print("\nLeveling up:")
    hero.level_up()

    # Print updated stats
    print("\nUpdated Stats:")
    print(hero)

if __name__ == "__main__":
    main()