# Explanation:
#  https://math.stackexchange.com/questions/1895119/how-many-ways-to-reach-nth-number-from-starting-point-using-any-number-steps-b

def rollDice(n):
    if n > 1:
        return rollDice(n-1) + rollDice(n-2) + rollDice(n-3) + \
        rollDice(n-4) + rollDice(n-5) + rollDice(n-6)
    elif n == 1:
        return 1
    elif n == 0:
        return 1
    else:
        return 0

# Python
def rollDiceIterate(n):
    total = 0
    divided = [1,0,0,0,0,0]

    for i in range(n+1):
        total = sum(divided)
        if i < 6:
            divided[i]=total
        else:
        # explain slice notation: https://stackoverflow.com/questions/509211/explain-slice-notation
        # 						  https://stackoverflow.com/a/44341431/1613961
        # append and extend in list: https://stackoverflow.com/a/252711/1613961
            divided = divided[1:] + [total]

    return total

print rollDiceIterate(610)
