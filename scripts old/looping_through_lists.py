# Create a list of tuples, each representing the name, age, and position of a
# player on a basketball team.
team = [
    ('Marta', 20, 'center'),
    ('Ana', 22, 'point guard'),
    ('Gabi', 22, 'shooting guard'),
    ('Luz', 21, 'power forward'),
    ('Lorena', 19, 'small forward'),
]

# Create a function to extract and names and positions from the team list and
# format them to be printed. Returns a list.
def player_position(players):
    result = []
    for name, age, position in players:
        result.append('Name: {}\nPosition: {}'.format(name, position))
    return result


for player in player_position(team):
    print(player)
