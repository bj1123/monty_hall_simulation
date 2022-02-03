import random

def monty_hall():
    x = [0, 0, 1]
    random.shuffle(x)
    selected = random.choice([i for i in range(3)])
    removed = random.choice([i for i in range(3) if i is not selected and x[i] is 0])
    changed = [i for i in range(3) if i not in (selected, removed)][0]
    return x[changed], x[selected]

if __name__ == '__main__':
    n_simulation = 100000
    win_changed = 0
    win_unchanged = 0
    for i in range(n_simulation):
        res_changed, res_unchanged = monty_hall()
        win_changed += res_changed
        win_unchanged += res_unchanged
    print(f'total number of simulation : {n_simulation}')
    print(f'win ratio if answer changed : {win_changed / n_simulation}')
    print(f'win ratio if answer is not changed : {win_unchanged / n_simulation}')