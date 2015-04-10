from ddshape import *

index_1, data_1 = bsphere.bsphere(center=(-28, 0, 0), offset=(15, 0, 0))
index_2, data_2 = bsphere.bsphere(index=index_1, center=(28, 0, 0), offset=(-15, 0, 0))
index_3, data_3 = sphere.sphere(index=index_2, radius=4, center=(0, 0, 0))
inc.write_shape((106, 106, 106), index_3, data_1+data_2+data_3)
