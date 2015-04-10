# -*- encoding:utf-8 -*-

import ddshape.inc as inc


def hsphere(index=1, data="", center=(1, (0, 0, 0)), outr=25, shell=3, factor=1):
    """
    the main function to write hollow sphere
    :param index: a number which indicate the line numbers of main shape data
    :param data: string with all shape data combined
    :param center: center of the hollow sphere
    :param outr: out radius of sphere
    :param shell: shell thickness of sphere
    :param factor: which determine the precision of shape data
    :return: int, string
    """
    center_num = center[0]
    # main data body create
    for i in range(center_num):
        center_tmp = center[i + 1] * factor
        max_range = int(float(outr) * float(factor))
        max_shell = int(float(shell) * float(factor))
        for j in range(-1 * max_range, max_range + 1):
            for k in range(-1 * max_range, max_range + 1):
                for m in range(-1 * max_range, max_range + 1):
                    sqrt_acc = j ** 2 + k ** 2 + m ** 2
                    if (max_range - max_shell) ** 2 <= sqrt_acc <= max_range ** 2:
                        data += inc.print_line(index, center_tmp, (j, k, m))
                        index += 1
    return index, data



# examples of the usage of this module
# ----
# from ddshape import *
# index, data = hsphere.hsphere(center=(2, (-30, 0, 0), (30, 0, 0)), shell=3)
# inc.writeshape((100, 100, 100), index, data)

