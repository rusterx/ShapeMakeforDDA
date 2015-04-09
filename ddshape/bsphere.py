# -*- encoding:utf-8 -*-

import ddshape.inc as inc


def bsphere(index=1, data="", center=(0, 0, 0), offset=(0, 0, 0), outr=25, shell=3):
    """
    main function to create data with a intersection operation of A sphere(main) and B sphere(used to bool with A)
    :param index: a number which indicate the line numbers of main shape data
    :param data: string with all shape data combined
    :param center: center of the break sphere
    :param offset: center of the sphere will be used in a bool operation with real sphere
    :param outr: the out radius of sphere
    :param shell: the thickness of the sphere
    :return: int, float
    """
    for j in range(-1 * outr, outr + 1):
        for k in range(-1 * outr, outr + 1):
            for m in range(-1 * outr, outr + 1):
                if verify((j, k, m), center, offset, outr, shell):
                    data += inc.print_line(index, center, (j, k, m))
                    index += 1
    return index, data


def verify(relative_point=(0, 0, 0), center=(0, 0, 0), offset_center=(0, 0, 0), out_radius=25, shell=3):
    """
    the function that check if the point can be write
    :param relative_point: the relative point of the A sphere without add center point
    :param center: center of A sphere(main sphere)
    :param offset_center: offset center means the center of B sphere
    :param out_radius: the out radius of A sphere
    :param shell: the thickness of A sphere
    :return: bool
    """
    sqrt_sum = relative_point[0] ** 2 + relative_point[1] ** 2 + relative_point[2] ** 2
    if not (out_radius - shell) ** 2 <= sqrt_sum <= out_radius ** 2:
        return False
    point = (relative_point[0] + center[0], relative_point[1] + center[1], relative_point[2] + center[2])
    offset_sum = (point[0] - offset_center[0]) ** 2 + (point[1] - offset_center[1]) ** 2 + \
                 (point[2] - offset_center[2]) ** 2
    if offset_sum <= out_radius ** 2:
        return False
    return True


def writeshape(out_radius, index, data):
    """
    write data into shape.dat
    :param out_radius: out radius of A sphere
    :param index: a number which indicate the line numbers of main shape data
    :param data: string with all shape data combined
    :return: null
    """
    inc.write_shape((out_radius * 2, out_radius * 2, out_radius * 2), index, data)



# examples of the usage of this module
# ----
# from ddshape import *
# index_1, data_1 = bsphere.bsphere(center=(-25, 0, 0), offset=(18, 0, 0))
# index_2, data_2 = bsphere.bsphere(index=index_1, center=(25, 0, 0), offset=(-18, 0, 0))
# bsphere.writeshape(25, index_2, data_1 + data_2)
