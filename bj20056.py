n, m, k = map(int, input().split())
fireball = {}
for _ in range(m):
    fire = list(map(int, input().split()))
    fire[0],fire[1]=fire[0]-1,fire[1]-1
    if (fire[0], fire[1]) in fireball:
        fireball[(fire[0], fire[1])].append(fire)
    else:
        fireball[(fire[0], fire[1])] = [fire]
dr, dc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]
for _ in range(k):
    new_fireball = {}
    dup_list = set([])
    for f in list(fireball.values()):
        for fire in f:
            new_r, new_c = (fire[0] + (dr[fire[4]] * fire[3])) % n, (fire[1] + (dc[fire[4]] * fire[3])) % n
            fire[0], fire[1] = new_r, new_c
            if (new_r, new_c) in new_fireball:
                new_fireball[(new_r, new_c)].append(fire)
                dup_list.add((new_r, new_c))
            else:
                new_fireball[(new_r, new_c)] = [fire]

    for r, c in dup_list:
        fs = new_fireball[(r, c)]
        count = 0
        mass = 0
        speed = 0
        even = 0
        odd = 0
        for f in fs:
            count += 1
            mass += f[2]
            speed += f[3]
            if f[4] % 2 == 0:
                even += 1
            else:
                odd += 1
        if mass // 5 == 0:
            del new_fireball[(r,c)]
            continue
        new_speed = speed // count
        if even == 0 or odd == 0:
            new_fireball[(r, c)] = [[r, c, mass // 5, new_speed, 0], [r, c, mass // 5, new_speed, 2],
                                    [r, c, mass // 5, new_speed, 4], [r, c, mass // 5, new_speed, 6]]
        else:
            new_fireball[(r, c)] = [[r, c, mass // 5, new_speed, 1], [r, c, mass // 5, new_speed, 3],
                                    [r, c, mass // 5, new_speed, 5], [r, c, mass // 5, new_speed, 7]]

    fireball=dict(new_fireball)
sum_value=0
for f in list(fireball.values()):
    for fire in f:
        sum_value+=fire[2]
print(sum_value)
