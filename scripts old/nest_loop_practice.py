# Nested loops can produce the different combinations of pips (dots) in
# a set of dominoes.
for left in range(7):
    for right in range(left, 7, 1):
        print(f"[{left}|{right}]", end=" ")
    print('\n')