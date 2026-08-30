states_visited = {
    'Eric': ['AK','WY','WA','NH'],
    'Isaac': ['CO','NY','AK']
}   

for name, states in states_visited.items():
    print(f'{name} has visited:')
    
    for state in states:
        print(f"  {state}")