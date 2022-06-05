import math
import numpy as np

def best_line(x,y):
    n = len(x)
    sum_x = sum(x)
    sum_x2 = sum(xi ** 2 for xi in x)
    sum_y = sum(y)
    sum_xy = sum(xi * yi for xi, yi in zip(x, y))
    A = [[n,sum_x], [sum_x,sum_x2]]
    B = [sum_y, sum_xy]
    return np.linalg.solve(A,B)




x = [0.0704, 0.1815, 0.3153, 0.3658, 0.5879, 0.6758, 0.7445, 0.9253, 0.9854, 1.2038, 1.2968, 1.4094, 1.4766, 1.5711, 1.7868, 1.8789, 1.999, 2.1104, 2.2252, 2.2951, 2.4188, 2.6433, 2.7295, 2.7994, 2.9847, 3.0628, 3.1605, 3.3232, 3.3877, 3.5207, 3.6616, 3.8498, 3.9284, 4.021, 4.209, 4.2504, 4.4246, 4.554, 4.5891, 4.7443, 4.8594, 4.99, 5.0752, 5.268, 5.3829, 5.4242, 5.6619, 5.7535, 5.7948, 5.9205, 6.0722, 6.1786, 6.323, 6.434, 6.6197, 6.6451, 6.8119, 6.9648, 7.0648, 7.22, 7.2351, 7.4445, 7.5723, 7.6118, 7.7732, 7.8473, 8.021, 8.0729, 8.1955, 8.401, 8.4503, 8.6034, 8.7741, 8.9106, 8.9915, 9.1255, 9.2461, 9.3131, 9.515, 9.6334, 9.6904, 9.799, 9.9891]
y = [4.9501, 4.9736, 5.2406, 5.4407, 7.4846, 5.8006, 6.4145, 6.5189, 6.5381, 6.8862, 6.7903, 7.4957, 7.8296, 7.8929, 7.9547, 8.2028, 8.7043, 8.6217, 8.9203, 9.1142, 9.5784, 10.0527, 9.1868, 10.2151, 9.6294, 9.745, 10.8757, 11.0779, 11.4187, 11.7959, 11.8589, 12.371, 12.4621, 11.948, 12.9549, 13.1681, 12.2439, 13.8358, 12.0227, 13.993, 12.4217, 14.3145, 14.5332, 15.0012, 15.2336, 15.2264, 15.5339, 16.1016, 15.9899, 16.2855, 16.5701, 16.9835, 16.9839, 17.2576, 17.7185, 17.5237, 18.0982, 18.5114, 18.601, 18.8187, 19.3979, 19.3669, 20.943, 19.7682, 19.3103, 20.1064, 20.1631, 21.3479, 19.0389, 20.2885, 20.7294, 21.6741, 22.5434, 21.9061, 22.3126, 22.6866, 22.7127, 23.3304, 22.8853, 24.6186, 23.7242, 23.5533, 24.5016]


a0, a1 = best_line(x,y)
print(a0, a1)