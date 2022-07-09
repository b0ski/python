def max_num(param):
    for instance_l1 in param:
        for instance_l2 in param:
            if instance_l1 < instance_l2:
                maximum = instance_l2
    return maximum, param.index(maximum)
#   print(max(param), param.index(max(param))) python method
