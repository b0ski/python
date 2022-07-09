def max_num(param):
    for instance_l1 in param:
        for instance_l2 in param:
            if instance_l1 < instance_l2:
                maximum = instance_l2
    print(maximum, param.index(maximum))


max_num((1, 666662, 43, 2345, 3245, 4232))
