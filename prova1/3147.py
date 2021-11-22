# Inputs
H, E, A, O, W, X = map(int, input().strip().split())

# Definindo os lados dos exercitos
good_army = H + E + A
bad_army = O + W

# Condição em que se chamam as águias
if good_army <= bad_army:
    good_army += X

# Vendo quem vence
print('Middle-earth is safe.') if good_army >= bad_army else print('Sauron has returned.')
