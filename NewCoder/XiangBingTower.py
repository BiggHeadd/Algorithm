# coding:utf-8

def solution(tower, n, m):
    tower_ml = [0] * n
    for i in range(m):
        # print(tower_ml)
        inputs_ins = list(map(int, input().split()))
        instruction = inputs_ins[0]
        actions = inputs_ins[1:]
        # print(instruction)
        if instruction == 2:
            layer_start = actions[0] - 1
            water_total = actions[1]
            while water_total > 0:
                if layer_start < n:
                    if water_total + tower_ml[layer_start] > tower[layer_start]:
                        # print(tower_ml, water_total, tower[layer_start], tower_ml[layer_start])
                        get = tower[layer_start] - tower_ml[layer_start]
                        water_total = water_total - get
                        tower_ml[layer_start] = tower[layer_start]
                        layer_start += 1
                    else:
                        tower_ml[layer_start] += water_total
                        water_total = 0
                else:
                    break
        else:
            # print(actions[0], tower_ml)
            print(tower_ml[actions[0] - 1])


if __name__ == "__main__":
    inputs = list(map(int, input().split()))
    n, m = inputs[0], inputs[1]
    tower = list(map(int, input().split()))
    solution(tower, n, m)

    # input sample 2
"""
5 4
1 2 2 10 1
1 3
2 2 5
2 4 3
1 4
"""
