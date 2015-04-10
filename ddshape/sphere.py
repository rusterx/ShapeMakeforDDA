# -*- encoding:utf-8 -*-

import ddshape.inc as inc


def sphere(index=1, data="", center=(0, 0, 0), radius=25):
    """
    the function of create sphere shape.dat
    :param index: a number which indicate the line numbers of main shape data
    :param data: string with all shape data combined
    :param center: center of sphere
    :param radius: the radius of sphere
    :return: int, string
    """
    for j in range(-1*radius, radius+1):
        for k in range(-1*radius, radius+1):
            for m in range(-1*radius, radius+1):
                sqrt_sum = j**2 + k**2 + m**2
                if sqrt_sum <= radius**2:
                    data += inc.print_line(index, center, (j, k, m))
                    index += 1
    return index, data


# example of usage
# from ddshape import *
# index, data = sphere.sphere()
# inc.writeshape((50, 50, 50), index, data)