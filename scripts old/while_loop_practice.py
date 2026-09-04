num = 0 
while num < 3:
    print(num) 
    num += 1


bugs = ['bug 1', 'bug 2', 'bug 3', 'bug 4', 'bug 5', 'bug 6']
while bugs:
    bug = bugs.pop(0)
    print(f"Fixing {bug}.")
print("All bugs fixed.")