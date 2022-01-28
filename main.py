def stat_calculator(base, growth, level, rounded):
    if rounded:
        return round(base + growth * (level - 1) * (.7025 + 0.0175 * (level - 1)))
    else:
        return base + growth * (level - 1) * (.7025 + 0.0175 * (level - 1))


def lethality_calculator(lethality, level):
    return lethality * (.6 + (.4 * level / 18))


def percentage_of_calculator(new, percent_of):
    return (new / percent_of) * 100


def atk_spd_calculator(atk_spd_ratio, base_atk_spd, bonus_atk_spd):
    return base_atk_spd + bonus_atk_spd * atk_spd_ratio


# Aphelios ad is 57 with an ad growth of 3
# Aphelios base atk spd is .64, as is his attack spd ratio
# Aphelios has 2.1 atk spd growth
# His q upgrade grants 4 ad per rank
# His e upgrade grants 3.5 lethality per rank
# His w upgrade grants 6 attack speed per rank
# Galeforce is 60 ad 20% atk spd
# Shieldbow is 55 ad 20% atk spd and 5 ad per mythic
# Kraken Slayer is 65 ad 25% atk spd and 10% atk spd per mythic
# Collector is 55 ad 12 lethality
# Runaan's is 45% atk spd
# phantom dancer is 25(55)% atk spd 20 ad
# Adaptive force minor is 5.4 ad
# Atk spd minor is 10%
# Doran blade is 8 ad
# Noonquiver is 30 ad 15% atk spd
# Berserker's Greaves is 35% atk spd
# infinity edge is 70 ad

# print(stat_calculator(57, 3, 9, True))
# print(atk_spd_calculator(.64, .64, stat_calculator(0, .021, 9, False)))

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 3 with doran blade
print("Level 3, d blade")
print("q -----> " + str(percentage_of_calculator(12, stat_calculator(57, 3, 3, True) + 13.4)))
print("e -----> " + str(lethality_calculator(10.5, 3)))
print("w -----> " + str(percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 3, False) + .1))))
print("2q -> 1w " + str(percentage_of_calculator(8, stat_calculator(57, 3, 3, True) + 13.4) + percentage_of_calculator(.06 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 3, False) + .1))))
print("2e -> 1w " + str(lethality_calculator(7, 3) + percentage_of_calculator(.06 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 3, False) + .1))))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 6 with doran blade
print("Level 6, d blade")
print("q -> e " + str(percentage_of_calculator(16, stat_calculator(57, 3, 6, True) + 13.4) + lethality_calculator(7, 6)))
print("e -> q " + str(lethality_calculator(14, 6) + percentage_of_calculator(8, stat_calculator(57, 3, 6, True) + 13.4)))
print("q -> w " + str(percentage_of_calculator(16, stat_calculator(57, 3, 6, True) + 13.4) + percentage_of_calculator(.12 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 6, False) + .1))))
print("e -> w " + str(lethality_calculator(14, 6) + percentage_of_calculator(.12 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 6, False) + .1))))
print("3q -> 3w " + str(percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 6, False) + .1)) + percentage_of_calculator(12, stat_calculator(57, 3, 6, True) + 13.4)))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 7 with doran blade and noonquiver
print("Level 7, noonquiver, d blade")
print("q -> e " + str(percentage_of_calculator(20, stat_calculator(57, 3, 7, True) + 43.4) + lethality_calculator(7, 7)))
print("e -> q " + str(lethality_calculator(17.5, 7) + percentage_of_calculator(8, stat_calculator(57, 3, 7, True) + 43.4)))
print("q -> w " + str(percentage_of_calculator(20, stat_calculator(57, 3, 7, True) + 43.4) + percentage_of_calculator(.12 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 7, False) + .25))))
print("e -> w " + str(lethality_calculator(17.5, 7) + percentage_of_calculator(.12 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 7, False) + .25))))
print("3q -> 3w -> 1e " + str(lethality_calculator(3.5, 7) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 7, False) + .25)) + percentage_of_calculator(12, stat_calculator(57, 3, 7, True) + 43.4)))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 9 with galeforce, d blade, and zerk's
print("Level 9, galeforce, d blade, and zerk's")
print("q -> e " + str(percentage_of_calculator(24, stat_calculator(57, 3, 9, True) + 73.4) + lethality_calculator(10.5, 9)))
print("e -> q " + str(lethality_calculator(21, 9) + percentage_of_calculator(12, stat_calculator(57, 3, 9, True) + 73.4)))
print("q -> w " + str(percentage_of_calculator(24, stat_calculator(57, 3, 9, True) + 73.4) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 9, False) + .65))))
print("e -> w " + str(lethality_calculator(21, 9) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 9, False) + .65))))
print("3q -> 3w -> 3e " + str(lethality_calculator(10.5, 9) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 9, False) + .65)) + percentage_of_calculator(12, stat_calculator(57, 3, 9, True) + 73.4)))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 12 with galeforce, collector, and zerk's
print("Level 12, galeforce, collector/bloodthirster, and zerk's")
print("q -> e " + str(percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 128.4) + lethality_calculator(21, 12)))
print("e -> q " + str(lethality_calculator(21, 12) + percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 128.4)))
print("q -> w " + str(percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 128.4) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + .65))))
print("e -> w " + str(lethality_calculator(21, 12) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + .65))))
print("3q -> 3w -> 6e " + str(lethality_calculator(21, 12) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + .65)) + percentage_of_calculator(12, stat_calculator(57, 3, 12, True) + 128.4)))
print("6q -> 4w -> 2e " + str(lethality_calculator(7, 12) + percentage_of_calculator(.24 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + .65)) + percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 128.4)))
print("6q -> 2w -> 4e " + str(lethality_calculator(14, 12) + percentage_of_calculator(.12 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + .65)) + percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 128.4)))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 12 with galeforce, hurricane, and zerk's
print("Level 12, galeforce, hurricane, and zerk's")
print("q -> e " + str(percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 73.4) + lethality_calculator(21, 12)))
print("e -> q " + str(lethality_calculator(21, 12) + percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 73.4)))
print("q -> w " + str(percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 73.4) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + 1.1))))
print("e -> w " + str(lethality_calculator(21, 12) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + 1.1))))
print("3q -> 3w -> 6e " + str(lethality_calculator(21, 12) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + 1.1)) + percentage_of_calculator(12, stat_calculator(57, 3, 12, True) + 73.4)))
print("6q -> 4w -> 2e " + str(lethality_calculator(7, 12) + percentage_of_calculator(.24 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + 1.1)) + percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 73.4)))
print("6q -> 2w -> 4e " + str(lethality_calculator(14, 12) + percentage_of_calculator(.12 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 12, False) + 1.1)) + percentage_of_calculator(24, stat_calculator(57, 3, 12, True) + 73.4)))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 15 with galeforce, hurricane, ie and zerk's
print("Level 15, galeforce, hurricane, ie, and zerk's")
print("max q, max w, 3e " + str(percentage_of_calculator(24, stat_calculator(57, 3, 15, True) + 143.4) + lethality_calculator(10.5, 15) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 15, False) + 1.1))))
print("max w, max e, 3q " + str(lethality_calculator(21, 15) + percentage_of_calculator(12, stat_calculator(57, 3, 15, True) + 143.4) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 15, False) + 1.1))))
print("max q, max e, 3w " + str(lethality_calculator(21, 15) + percentage_of_calculator(24, stat_calculator(57, 3, 15, True) + 143.4) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 15, False) + 1.1))))
print("\n")

# Comparison of q -> e to e -> q  to q -> w to e -> w max at level 15 with galeforce, collector, ie and zerk's
print("Level 15, galeforce, hurricane, collector, and zerk's")
print("max q, max w, 3e " + str(percentage_of_calculator(24, stat_calculator(57, 3, 15, True) + 198.4) + lethality_calculator(10.5, 15) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 15, False) + .65))))
print("max w, max e, 3q " + str(lethality_calculator(21, 15) + percentage_of_calculator(12, stat_calculator(57, 3, 15, True) + 198.4) + percentage_of_calculator(.36 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 15, False) + .65))))
print("max q, max e, 3w " + str(lethality_calculator(21, 15) + percentage_of_calculator(24, stat_calculator(57, 3, 15, True) + 198.4) + percentage_of_calculator(.18 * .64, atk_spd_calculator(.64, .64, stat_calculator(0, .021, 15, False) + .65))))
print("\n")