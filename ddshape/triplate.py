# -*- encoding:utf-8 -*-

import math
import ddshape.inc as inc


def triplate(index=1, data="", center=(0, 0, 0), l=100):
    """
    the function create triangle plate shape data
    :param index: a number which indicate the line numbers of main shape data
    :param data: string with all shape data combined
    :param center: center of bottom side
    :param l: the length of side
    :return: int, string
    """
    for j in range(-50, 51):
        for k in range(0, int(0.5 * l * math.sqrt(3)) + 1):
            r1 = k - math.sqrt(3) * j - 50 * math.sqrt(3)
            r2 = k + math.sqrt(3) * j - 50 * math.sqrt(3)
            if r1 < 0 and r2 < 0:
                for m in range(-3, 4):
                    data += inc.print_line(index, center, (j, k, m))
                    index += 1
    return index, data


def writeshape(out_radius=(50, 50, 50), index=1, data=""):
    """
    write data into shape.dat
    :param out_radius: out radius of A sphere
    :param index: a number which indicate the line numbers of main shape data
    :param data: string with all shape data combined
    :return: null
    """
    inc.write_shape((out_radius[0], out_radius[1], out_radius[2]), index, data)


# examples of the usage of this module
# ----
# from ddshape import *
# index, data = triplate.triplate()
# triplate.writeshape((100, 100, 100), index, data)