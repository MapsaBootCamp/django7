from typing import List, Tuple

def f_knapsack(input_val_weight: List[Tuple], capacity):
    density_val_weight: List[Tuple] = []

    for elm in input_val_weight:
        density_val_weight.append((*elm, elm[0]/elm[1])) # (val, weight, density)

    density_val_weight = sorted(density_val_weight, key=lambda x: x[2], reverse=True)
    result = []
    for elm in density_val_weight:
        if capacity >= elm[1]:
            result.append((elm[0], elm[1], 1))
            capacity -= elm[1]
            if capacity == 0:
                break
        else:
            result.append((elm[0], elm[1], capacity/elm[1]))
            break
    return result


W = 16
tools = [(3, 12), (12, 4), (8, 9), (6, 15)]
print(f_knapsack(tools, W))