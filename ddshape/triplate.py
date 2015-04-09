# -*- encoding:utf-8 -*-

import math
import ddshape.inc as inc


def triplate(index=1, data="", center=(0, 0, 0), l=100):
    for j in range(-50, 51):
        for k in range(0, int(0.5 * l * math.sqrt(3)) + 1):
            r1 = k - math.sqrt(3) * j - 50 * math.sqrt(3)
            r2 = k + math.sqrt(3) * j - 50 * math.sqrt(3)
            if r1 < 0 and r2 < 0:
                for m in range(-3, 4):
                    data += inc.print_line(index, center, (j, k, m))
                    index += 1
    return index, data


def writeshape(out_radius, index, data):
    inc.write_shape((out_radius * 2, out_radius * 2, out_radius * 2), index, data)


# examples of the usage of this module
# ----
# from ddshape import *
# index, data = triplate.triplate()
# triplate.writeshape((100, 100, 100), index, data)