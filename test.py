# -*- encoding:utf-8 -*-

from ddshape import *

index_1, data_1 = bsphere.bsphere(center=(-25, 0, 0), offset=(18, 0, 0))
index_2, data_2 = bsphere.bsphere(index=index_1, center=(25, 0, 0), offset=(-18, 0, 0))
bsphere.writeshape(25, index_2, data_1 + data_2)