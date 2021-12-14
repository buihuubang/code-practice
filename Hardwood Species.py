def print_tree(d, count_tree):
    od = {k: v for k, v in sorted(d.items())}
    for k, v in od.items():
        print(k, "{:.4f}".format((v / count_tree) * 100))
    d = dict()
    count_tree = 0
    return d, count_tree


def main():
    t = int(input())
    tc = 0
    temp_ip = input()
    d = dict()
    count_tree = 0
    while tc < t:
        try:
            tree_name = input()
            if len(tree_name) > 0:
                get_num_spe = d.get(tree_name)
                if get_num_spe == None:
                    d[tree_name] = 1
                else:
                    d[tree_name] = get_num_spe + 1
                count_tree += 1
            else:
                d, count_tree = print_tree(d, count_tree)
                tc += 1
        except EOFError:
            print_tree(d, count_tree)
            break


if __name__ == '__main__':
    main()

'''
TEST CASE:

INPUT:
1

Red Alder
Ash
Aspen
Basswood
Ash
Beech
Yellow Birch
Ash
Cherry
Cottonwood
Ash
Cypress
Red Elm
Gum
Hackberry
White Oak
Hickory
Pecan
Hard Maple
White Oak
Soft Maple
Red Oak
Red Oak
White Oak

OUTPUT:
Ash 16.6667
Aspen 4.1667
Basswood 4.1667
Beech 4.1667
Cherry 4.1667
Cottonwood 4.1667
Cypress 4.1667
Gum 4.1667
Hackberry 4.1667
Hard Maple 4.1667
Hickory 4.1667
Pecan 4.1667
Red Alder 4.1667
Red Elm 4.1667
Red Oak 8.3333
Soft Maple 4.1667
White Oak 12.5000
Yellow Birch 4.1667
'''