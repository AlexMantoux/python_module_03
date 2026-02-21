if __name__ == "__main__":
    alice = set(["first_kill", "level_10", "treasure_hunter", "speed_demon"])
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(["level_10", "treasure_hunter", "boss_slayer", "speed_demon", "perfectionist"])

    print("=== Achievement Tracker System ===")
    print()
    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")
    print()

    print("=== Achievement Analytics ===")
    union_players = alice.union(bob).union(charlie)
    union_players2 = alice | bob | charlie
    print(f"All unique achievements: {sorted(union_players)}")
    print(f"Total unique achievements: {len(union_players)}")
    print()
    inter_players = alice.intersection(bob).intersection(charlie)
    rare_achiev =  (alice - bob - charlie) | (bob - alice - charlie) | (charlie - alice - bob)
    print(f"Common to all players: {sorted(inter_players)}")
    print(f"Rare achievements (1 player): {rare_achiev}")
    print()
    print(f"Alice vs Bob common: {alice.intersection(bob)}")
    alice_unique = alice - bob.union(charlie)
    print(f"Alice unique: {alice - (bob & charlie)}")


